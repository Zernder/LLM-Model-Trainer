import os
import json
from transformers import GPT2Tokenizer, GPT2LMHeadModel
import torch
from torch.utils.data import Dataset, DataLoader
from tqdm import tqdm
from typing import List


# Define the PersonaChatDataset class
class PersonaChatDataset(Dataset):
    def __init__(self, data: List[str], tokenizer: GPT2Tokenizer, maxlen: int):
        self.data = data
        self.tokenizer = tokenizer
        self.maxlen = maxlen

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        input_text = self.data[index]
        encoded_input = self.tokenizer.encode_plus(
            input_text,
            truncation=True,
            max_length=self.maxlen - 1,
            padding='max_length',
            return_tensors='pt'
        )
        input_ids = encoded_input['input_ids'].squeeze()
        attention_mask = encoded_input['attention_mask'].squeeze()

        return {'input_ids': input_ids, 'attention_mask': attention_mask}

# Load tokenizer and model
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

# Set device (cuda/cpu)
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

metrics = 0

# Define evaluation metrics and functions
def compute_metrics(predictions, targets):
    # Implement your evaluation metrics
    # Calculate perplexity, BLEU score, etc.
    # Return the computed metrics
    return metrics

# Load and process validation or test data
def load_data(file_path):
    with open(file_path, "r") as f:
        data = json.load(f)
    return data

def process_data(data, tokenizer, maxlen):
    encoded_data = []
    for input_text in data:
        encoded_input = tokenizer.encode_plus(
            input_text,
            truncation=True,
            max_length=maxlen - 1,
            padding='max_length',
            return_tensors='pt'
        )
        input_ids = encoded_input['input_ids'].squeeze()
        attention_mask = encoded_input['attention_mask'].squeeze()
        encoded_data.append({'input_ids': input_ids, 'attention_mask': attention_mask})
    return encoded_data

# Set validation or test data paths
validation_data_path = "./Data/Validation"
# Or
test_data_path = "./Data/Testing"

# Set the maximum sequence length
maxlen = 128

# Load validation or test data
validation_data = load_data(validation_data_path)
# Or
test_data = load_data(test_data_path)

# Process validation or test data
processed_validation_data = process_data(validation_data, tokenizer, maxlen)
# Or
processed_test_data = process_data(test_data, tokenizer, maxlen)

# Create dataset and data loader
validation_dataset = PersonaChatDataset(processed_validation_data, tokenizer, maxlen)
# Or
test_dataset = PersonaChatDataset(processed_test_data, tokenizer, maxlen)

batch_size = 16
validation_data_loader = DataLoader(validation_dataset, batch_size=batch_size, shuffle=False)
# Or
test_data_loader = DataLoader(test_dataset, batch_size=batch_size, shuffle=False)

# Evaluation loop
model.eval()
total_metrics = 0

for batch in tqdm(validation_data_loader):
    # Extract input and target sequences from the batch
    input_ids = batch['input_ids'].to(device)
