import os
import json
from transformers import GPT2Tokenizer
from PersonaChatDataset import PersonaChatDataset

# Replace `validation_folder` with the path to your validation folder
validation_folder = "./Data/Validation"

# Replace `tokenizer` and `maxlen` with your actual tokenizer and maximum length values
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
maxlen = 512

# Process your validation data
processed_validation_data = []

# Iterate over the JSON files in the validation folder
for filename in os.listdir(validation_folder):
    file_path = os.path.join(validation_folder, filename)
    
    # Load the JSON data from the file
    with open(file_path, "r") as file:
        data = json.load(file)
    
    # Access persona data for each instance
    for instance in data:
        persona_input_ids = instance['input_ids']
        persona_attention_mask = instance['attention_mask']

        # Process the persona data as needed
        # ...
        
        # Print the persona input IDs and attention mask
        print(persona_input_ids)
        print(persona_attention_mask)

        # Process the data and append it to the processed validation data list
        processed_validation_data.append({
            'persona': {
                'input_ids': persona_input_ids,
                'attention_mask': persona_attention_mask
            },
            'chat': {
                'input_ids': chat_input_ids,
                'attention_mask': chat_attention_mask
            }
        })

# Replace `persona_col` and `chat_col` with the appropriate column names from your data
persona_col = 'persona'  # Column name for the persona data
chat_col = 'chat'  # Column name for the chat data

# Create validation dataset using the processed validation data
validation_dataset = PersonaChatDataset(processed_validation_data, tokenizer, maxlen, persona_col, chat_col)
