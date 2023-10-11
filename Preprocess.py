import os
import sqlite3
import spacy
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Initialize spaCy model for tokenization
nlp = spacy.load("en_core_web_sm")

# Function to perform text preprocessing
def preprocess_text(text):
    # Tokenization
    doc = nlp(text)
    tokens = [token.text for token in doc]

    # Lowercasing
    tokens = [token.lower() for token in tokens]

    # Removing punctuation
    tokens = [token.translate(str.maketrans('', '', string.punctuation)) for token in tokens]

    # Removing stopwords
    stopwords_list = set(stopwords.words("english"))
    tokens = [token for token in tokens if token not in stopwords_list]

    # Lemmatization
    lemmatizer = WordNetLemmatizer()
    tokens = [lemmatizer.lemmatize(token) for token in tokens]

    # Rejoin tokens into cleaned text
    cleaned_text = ' '.join(tokens)

    return cleaned_text

# Directory where your text files are located
data_folder = "Data"

# Connect to the SQLite database
conn = sqlite3.connect("conversation_data.db")
cursor = conn.cursor()

# Create a table to store conversation data if it doesn't exist
cursor.execute('''CREATE TABLE IF NOT EXISTS conversations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    original_text TEXT,
                    preprocessed_text TEXT
                )''')

# Iterate through the files in the "Data" folder
for filename in os.listdir(data_folder):
    if filename.endswith(".txt"):
        file_path = os.path.join(data_folder, filename)

        with open(file_path, "r", encoding="utf-8") as file:
            text = file.read()
            preprocessed_text = preprocess_text(text)

        # Insert the original and preprocessed text into the database
        cursor.execute("INSERT INTO conversations (original_text, preprocessed_text) VALUES (?, ?)", (text, preprocessed_text))
        conn.commit()

# Close the database connection
conn.close()

print("Data from text files in the 'Data' folder preprocessed and inserted into the database.")
