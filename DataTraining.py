import torch
import torch.nn as nn
from transformers import GPT2LMHeadModel, GPT2Tokenizer
from torch.utils.data import DataLoader
from tqdm import tqdm
import os
import json
from torch.utils.data import Dataset
from torch.nn.utils.rnn import pad_sequence
from random import sample
from PersonaChatDataset import PersonaChatDataset

device = input("Enter the device (cuda/cpu): ").lower()
if device == "cuda" and not torch.cuda.is_available():
    device = "cpu"
elif device != "cpu" and device != "cuda":
    device = "cpu"
device = torch.device(device)

print(device)

output_dir = ".\Model"

# Find the last saved checkpoint in the output directory
saved_checkpoints = [dir for dir in os.listdir(output_dir) if dir.startswith('checkpoint_')]
last_checkpoint = sorted(saved_checkpoints)[-1] if saved_checkpoints else None

# Load tokenizer
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
tokenizer.add_special_tokens({'pad_token': '[PAD]'})
tokenizer.pad_token = tokenizer.eos_token

# Load pre-trained GPT-2 model or initialize a new one
model = GPT2LMHeadModel.from_pretrained("gpt2") if not last_checkpoint else GPT2LMHeadModel.from_pretrained(
    os.path.join(output_dir, last_checkpoint))
model.resize_token_embeddings(len(tokenizer))
model.to(device)

# Find two random JSON files from the EncodedJson folder
json_folder = ".\Data\Training"
file_paths = [os.path.join(json_folder, file) for file in os.listdir(json_folder) if file.endswith('.json')]
random_files = sample(file_paths, k=3)
print("Randomly picked JSON files:", random_files)

# Load encoded data
encoded_data = []
for file_path in random_files:
    with open(file_path, "r") as f:
        data = json.load(f)
        encoded_data.extend(data)

# Create the PersonaChat dataset from the encoded data
maxlen = 128
persona_col = 'input_ids'  # Replace with the actual column name for persona data
chat_col = 'attention_mask'  # Replace with the actual column name for chat data
dataset = PersonaChatDataset(encoded_data, tokenizer, maxlen, persona_col, chat_col)

# Create data loader
batch_size = 16
data_loader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

# Training setup
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-5)
criterion = nn.CrossEntropyLoss()

# Training loop
num_epochs = 100
save_interval = 50
total_steps = len(data_loader) * num_epochs
progress_bar = tqdm(total=total_steps, desc="Training", dynamic_ncols=True)

model.train()
for epoch in range(num_epochs):
    total_loss = 0
    for step, batch in enumerate(data_loader):
        # Extract input and target sequences from the batch
        input_ids = batch['input_ids']
        attention_mask = batch['attention_mask']

        # Move the data to the appropriate device
        input_ids = input_ids.to(device)
        attention_mask = attention_mask.to(device)

        # Clear the gradients
        optimizer.zero_grad()

        # Forward pass
        outputs = model(input_ids=input_ids, attention_mask=attention_mask, labels=input_ids)

        # Compute the loss
        loss = outputs.loss

        # Backward pass
        loss.backward()

        # Update the model parameters
        optimizer.step()

        total_loss += loss.item()

        progress_bar.update(1)

    # Compute the average loss for the epoch
    avg_loss = total_loss / len(data_loader)

    # Save the model checkpoint every save_interval epochs
    if (epoch + 1) % save_interval == 0:
        checkpoint_dir = os.path.join(output_dir, f"checkpoint_{epoch+1}")
        os.makedirs(checkpoint_dir, exist_ok=True)
        model.save_pretrained(checkpoint_dir)
        tokenizer.save_pretrained(checkpoint_dir)
        print(f"Saved checkpoint at epoch {epoch+1} to {checkpoint_dir}")

    print(f"Epoch {epoch + 1}/{num_epochs} - Average Loss: {avg_loss}")

progress_bar.close()
print("Training completed!")

# Save the final model
model.save_pretrained(output_dir)
tokenizer.save_pretrained(output_dir)
