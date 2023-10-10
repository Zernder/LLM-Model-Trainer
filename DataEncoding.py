import os
import pandas as pd
import json
from transformers import GPT2Tokenizer
import torch
from torch.utils.data import Dataset
from torch.nn.utils.rnn import pad_sequence
import random
from typing import Tuple, List
from PersonaChatDataset import PersonaChatDataset
import shutil



def load_data_from_json_folder(folder_path: str, num_files: int = 2) -> Tuple[pd.DataFrame, List[str]]:
    file_paths = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.json')]
    random_files = random.sample(file_paths, min(num_files, len(file_paths)))
    dfs = []
    file_names = []
    for file_path in random_files:
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        with open(file_path, 'r') as f:
            try:
                data = json.load(f)
                df = pd.DataFrame(data)
                dfs.append(df)
                file_names.append(file_name)
            except json.JSONDecodeError:
                print(f"Error loading JSON file: {file_path}")
    if dfs:
        df_combined = pd.concat(dfs, ignore_index=True)
        return df_combined, file_names
    else:
        print("No JSON files found in the specified folder.")
        return pd.DataFrame(), []

def tokenize_data(data: pd.Series, tokenizer: GPT2Tokenizer, maxlen: int) -> pd.DataFrame:
    encoded_data = []
    for input_text in data:
        encoded_input = tokenizer.encode_plus(input_text, truncation=True, max_length=maxlen - 1, padding='max_length', return_tensors='pt')
        input_ids = encoded_input['input_ids'].flatten()
        attention_mask = encoded_input['attention_mask'].flatten()
        encoded_data.append((input_ids, attention_mask))

    encoded_df = pd.DataFrame(encoded_data, columns=['input_ids', 'attention_mask'])
    return encoded_df

if __name__ == '__main__':
    # Set tokenizer and maximum sequence length
    tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
    tokenizer.add_special_tokens({'pad_token': '[PAD]'})
    maxlen = 128

    # Set the JSON folder path
    json_folder = "./Data/Generated"

    # Load two random JSON files from the specified folder
    data_df, file_names = load_data_from_json_folder(json_folder, num_files=2)

    # Extract the "generated_text" column
    generated_text = data_df['generated_text']

    # Tokenize and encode the generated text using the GPT-2 tokenizer
    encoded_data_df = tokenize_data(generated_text, tokenizer, maxlen)

    # Convert encoded data to dictionary and serialize
    encoded_data_dict = encoded_data_df.to_dict(orient='records')
    serialized_data = []
    for item in encoded_data_dict:
        serialized_data.append({k: v.tolist() if isinstance(v, torch.Tensor) else v for k, v in item.items()})

    # Encode dictionary as JSON
    json_data = json.dumps(serialized_data)

    # Write JSON data to file
    for i, file_name in enumerate(file_names):
        encoded_data_file = f"{file_name}_encoded.json"
        with open(encoded_data_file, 'w') as f:
            f.write(json_data)

    # Path to the directory containing the encoded JSON files
    encoded_data_dir = "./Data/Encoded"

    # Create directories for training, validation, and testing
    train_dir = "./Data/Training"
    validation_dir = "./Data/Validation"
    test_dir = "./Data/Testing"
    os.makedirs(train_dir, exist_ok=True)
    os.makedirs(validation_dir, exist_ok=True)
    os.makedirs(test_dir, exist_ok=True)

    # Randomly split the encoded JSON files into train/validation/test sets
    encoded_files = [f for f in os.listdir(encoded_data_dir) if f.endswith('.json')]
    random.shuffle(encoded_files)

    train_files = encoded_files[:int(0.8 * len(encoded_files))]
    validation_files = encoded_files[int(0.8 * len(encoded_files)):int(0.9 * len(encoded_files))]
    test_files = encoded_files[int(0.9 * len(encoded_files)):]

    # Move the files to the corresponding directories
    for file in train_files:
        shutil.move(os.path.join(encoded_data_dir, file), os.path.join(train_dir, file))
    for file in validation_files:
        shutil.move(os.path.join(encoded_data_dir, file), os.path.join(validation_dir, file))
    for file in test_files:
        shutil.move(os.path.join(encoded_data_dir, file), os.path.join(test_dir, file))

    print("Data encoding and splitting completed successfully.")
