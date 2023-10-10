import pandas as pd
from transformers import GPT2Tokenizer, GPT2LMHeadModel
print("Find Frames")
# Store the names of DataFrames to be deleted
dataframe_names = []

# Find and store the names of existing DataFrames
for var_name, var_value in list(globals().items()):
    if isinstance(var_value, pd.DataFrame):
        dataframe_names.append(var_name)

print("Delete Frames")
# Delete existing DataFrames
for dataframe_name in dataframe_names:
    del globals()[dataframe_name]

print("Delete Model")
# Delete existing model if it exists
if 'model' in globals():
    del model


print("Create Model")
# Create a new model
model_name_or_path = 'gpt2'  # Replace with your desired model name or path
tokenizer = GPT2Tokenizer.from_pretrained(model_name_or_path)
model = GPT2LMHeadModel.from_pretrained(model_name_or_path)
