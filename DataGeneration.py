import os
import json
import openai
import random
from tqdm import tqdm
import Traits
import time

# Retrieve OpenAI API key from a text file
api_key_path = "OpenAIKey.txt"
with open(api_key_path, "r") as file:
    api_key = file.read().strip()

# Set the OpenAI API key
openai.api_key = api_key

# Set the parent directory for "GeneratedData" and "GeneratedDataJson" folders
parent_directory = "DataGeneration"
os.makedirs(parent_directory, exist_ok=True)

# Set the directory for the "GeneratedDataJson" folder
json_files_folder = os.path.join(parent_directory, "GeneratedDataJson")
os.makedirs(json_files_folder, exist_ok=True)

# Check if there is a saved list of previously selected traits
previous_traits_path = os.path.join(json_files_folder, "previous_traits.txt")
if os.path.isfile(previous_traits_path):
    with open(previous_traits_path, "r") as file:
        previous_traits = file.read().splitlines()
else:
    previous_traits = []

# Define the number of iterations
num_iterations = 23

# Run the loop for the specified number of iterations
for iteration in range(num_iterations):
    # Filter out previously selected traits from the available traits
    available_traits = [trait for trait in Traits.traits if trait not in previous_traits]
    print("Available Traits:")
    print(available_traits)
    time.sleep(5)

    if not available_traits or len(available_traits) < 3:
        # Clear the previous_traits list and reset the previous_traits.txt file
        previous_traits = []
        with open(previous_traits_path, "w") as file:
            file.write("")

        # Set available_traits to include all traits from Traits.traits
        available_traits = Traits.traits

    # Randomly select 3 traits from the available_traits list
    random_traits = random.sample(available_traits, 1)

    # Append the current traits to the previous traits for the next run
    with open(os.path.join(json_files_folder, "previous_traits.txt"), "a") as file:
        file.write("\n")
        file.write("\n".join(random_traits))

    # Print the chosen traits
    print("Chosen Traits:")
    for trait in random_traits:
        print(trait)

    def generate_text(prompt):
        response = openai.Completion.create(
            engine="text-davinci-002",  # You can also use other engines, like "text-curie-002"
            prompt=prompt,
            max_tokens=50,  # Adjust this number to control the length of the generated text
            n=1,
            stop=None,
            temperature=0.8,
            top_p=1,
        )
        return response.choices[0].text.strip()

    def generate_data(filename, num_samples, trait):
        # Use the json_files_folder path for saving the JSON file
        json_file_path = os.path.join(json_files_folder, filename)

        progress_bar = tqdm(total=num_samples, desc=f"Generating {filename}")

        data = []
        for i in range(num_samples):
            # Get the prompt for the selected trait from Traits module
            prompt = Traits.prompt_dict[trait]

            # Generate a random message text using OpenAI
            generated_text = generate_text(prompt)

            # Create a dictionary to save the generated data
            sample_dict = {
                "trait": trait,
                "prompt": prompt,
                "generated_text": generated_text
            }

            # Add the sample dictionary to the data list
            data.append(sample_dict)

            # Update the progress bar
            progress_bar.update(1)

        # Save the generated data to a JSON file
        with open(json_file_path, "w") as file:
            json.dump(data, file)

        # Close the progress bar
        progress_bar.close()

        # Return the generated data
        return data

    # Generate data samples for the chosen traits
    num_samples = 1000
    for trait in random_traits:
        filename = f"{trait}.json"
        data = generate_data(filename, num_samples, trait)
        print(f"Generated {len(data)} samples for {trait}.")
        print(f"Saved data to {filename}.")

    # Loop through the chosen traits to generate text using the prompts
    for trait in random_traits:
        prompt = random.choice(Traits.prompt_dict[trait])
        generated_text = generate_text(prompt)
        print(f'Trait: {trait}\nGenerated Text: {generated_text}\n')
