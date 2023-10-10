import torch
from transformers import AutoTokenizer, AutoModelForCausalLM
import subprocess
import sys
import os
import logging
import spacy
import os
import pickle

logging.getLogger("transformers").setLevel(logging.ERROR)

# Load the large model
nlp = spacy.load('en_core_web_lg')

def install_dependencies():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"],
                          stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)


# Install dependencies
install_dependencies()

def generate_response(model, tokenizer, input_text):
    model.eval()

    input_tokens = tokenizer.encode(input_text, return_tensors='pt')
    input_length = input_tokens.shape[1]

    # Check if the user wants to set a calendar event
    if "set event" in input_text.lower():
        # Prompt the user for event details
        event_title, start_time, end_time, location, description = extract_event_details(input_text)

        if event_title and start_time and end_time and location:
            # Create the event
            event = {
                'summary': event_title,
                'start': {'dateTime': start_time},
                'end': {'dateTime': end_time},
                'location': location,
                'description': description,
            }
            created_event = create_event(calendar_service, event)
            return f"Event created: {created_event['summary']}"

        else:
            return "Please provide valid event details."


    with torch.no_grad():
        output_tokens = model.generate(
            input_tokens,
            attention_mask=torch.ones_like(input_tokens),
            max_length=max_length + input_length,
            num_return_sequences=1,
            no_repeat_ngram_size=2,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            temperature=0.8
        )

    response = tokenizer.decode(output_tokens[0, input_length:], skip_special_tokens=True)

    return response



# Get the absolute path of the script
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the relative path to the model directory
model_dir = os.path.join(script_dir, "model")

# Load the saved tokenizer and model


tokenizer = AutoTokenizer.from_pretrained("PygmalionAI/pygmalion-6b")

model = AutoModelForCausalLM.from_pretrained("PygmalionAI/pygmalion-6b")

print("Welcome Master! How may I be of assistance?")
print("To leave, just type quit!")

while True:
    user_input = input("\nYou: ")
    if user_input.lower() == 'quit':
        break

    # Added code to check input
    if len(user_input.strip()) == 0:
        print("Input is empty, please try again.")
        continue

    # Prepare the input_text
    input_text = f"{user_input}"

    # Generate the response using the loaded tokenizer and model
    ai_response = generate_response(model, tokenizer, input_text)

    print(f"\nBot: {ai_response}")
