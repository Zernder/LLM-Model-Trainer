import os
import sqlite3
import spacy
import string
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import openai
from config import OPENAI


openai.api_key = OPENAI


# Load spaCy model for tokenization
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

# Connect to or create an SQLite database
database_file = "conversation_data.db"

try:
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()

    # Create a table to store conversation data if it doesn't exist
    cursor.execute('''CREATE TABLE IF NOT EXISTS conversations (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        original_text TEXT,
                        preprocessed_text TEXT
                    )''')

    # Sample data for preprocessing
    sample_data = [
        "Hello, how are you? This is an example sentence with stop words and some punctuation!",
        "Another example text with punctuation and stop words.",
        "Yet another sentence to preprocess."
    ]

    # Preprocess and store data in the database
    for text in sample_data:
        preprocessed_text = preprocess_text(text)
        # Insert the original and preprocessed text into the database
        cursor.execute("INSERT INTO conversations (original_text, preprocessed_text) VALUES (?, ?)", (text, preprocessed_text))
        conn.commit()

    print("Data inserted successfully.")

except sqlite3.Error as e:
    print(f"SQLite error: {e}")

finally:
    # Close the database connection
    if conn:
        conn.close()
