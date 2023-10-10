# This File is called AStart.py #

import os
from progress.bar import Bar


# Define the files to choose from
file_options = {
    "1": ".\Data_Generator\DataGeneration.py",
    "2": ".\Encoding\DataEncoding.py",
    "3": ".\TrainingData\Training.py",
}

# Print the available options
print("Choose an option:")
print("1. Data Generation")
print("2. Data Encoding")
print("3. Data Training")
print("4. Run all files")

# Prompt for user input
choice = input("Enter your choice: ")

# Validate and execute the selected option
if choice == "4":
    files_to_run = list(file_options.values())
elif choice in file_options:
    files_to_run = [file_options[choice]]
else:
    print("Invalid choice. Exiting...")
    exit()

# Run each selected file with a progress bar
for file in files_to_run:
    print(f"Running {file}...")
    os.system(f"python {file}")
    print(f"{file} completed.")

    # Update the progress bar
    bar = Bar('Progress', max=len(files_to_run))
    bar.next()
    bar.finish()

print("All tasks completed.")