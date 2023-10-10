import torch
from torch.utils.data import Dataset
from torch.nn.utils.rnn import pad_sequence

class PersonaChatDataset(Dataset):
    def __init__(self, encoded_data, tokenizer, maxlen, persona_col, chat_col):
        self.tokenizer = tokenizer
        self.maxlen = maxlen
        self.persona_col = persona_col
        self.chat_col = chat_col
        
        self.input_ids = []
        self.attention_masks = []
        
        for data in encoded_data:
            input_ids = data["input_ids"]
            attention_mask = data["attention_mask"]
            
            self.input_ids.append(torch.tensor(input_ids))  # Convert to tensor
            self.attention_masks.append(torch.tensor(attention_mask))  # Convert to tensor

        self.input_ids = pad_sequence(self.input_ids, batch_first=True, padding_value=tokenizer.pad_token_id)
        self.attention_masks = pad_sequence(self.attention_masks, batch_first=True, padding_value=0)

    def __len__(self):
        return len(self.input_ids)

    def __getitem__(self, idx):
        input_ids = self.input_ids[idx]
        attention_mask = self.attention_masks[idx]
        
        return {
            "input_ids": input_ids,
            "attention_mask": attention_mask
        }
