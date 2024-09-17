import pandas as pd
from collections import Counter
import re
import csv
from transformers import AutoTokenizer

# Task 1: Define the path to the CSV files and their respective text columns
csv_files = {
    "CSV1.csv": "SHORT-TEXT",  
    "CSV2.csv": "entites",  
    "CSV3.csv": "TEXT",  
    "CSV4.csv": "TEXT", 
}

# Function to consolidate text from each CSV file separately
def consolidate_text(csv_file, text_column):
    df = pd.read_csv(csv_file)
    if text_column in df.columns:
        return "\n".join(df[text_column].dropna())  # Drop NaN values and join the text
    else:
        print(f"Column '{text_column}' not found in {csv_file}. Available columns: {df.columns}")
        return ""

# Task 1: Consolidate text from each file and store separately
consolidated_texts = {}
for csv_file, text_column in csv_files.items():
    consolidated_texts[csv_file] = consolidate_text(csv_file, text_column)

# Merge all the separate texts into a single string
final_consolidated_text = "\n".join(consolidated_texts.values())

# Save the merged consolidated text to a .txt file
with open('consolidated_text.txt', 'w') as f:
    f.write(final_consolidated_text)

print("Text data from all CSV files has been successfully merged into 'consolidated_text.txt'.")

# Task 2: Load the consolidated text from the .txt file
with open('consolidated_text.txt', 'r') as f:
    text = f.read()

# Function to count word occurrences
def count_words(text):
    words = re.findall(r'\w+', text.lower())  # Extract words and convert to lowercase
    word_counts = Counter(words)
    return word_counts

# Count the words in the text
word_counts = count_words(text)

# Get the top 30 most common words
top_30_words = word_counts.most_common(30)

# Save the top 30 words to a CSV file
with open('top_30_words.csv', 'w', newline='') as csvfile:
    fieldnames = ['word', 'count']
    writer = csv.writer(csvfile)
    writer.writerow(fieldnames)
    writer.writerows(top_30_words)

print("Top 30 words have been saved to 'top_30_words.csv'.")

# Part 3: Tokenization and Top 30 Tokens
# Load the tokenizer for BERT
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# Function to count token occurrences
def count_tokens(text):
    tokens = tokenizer.tokenize(text, clean_up_tokenization_spaces=False)  # Set clean_up_tokenization_spaces to False
    token_counts = Counter(tokens)
    return token_counts

token_counts = count_tokens(text)
top_30_tokens = token_counts.most_common(30)

# Save the top 30 tokens to a CSV file
with open('top_30_tokens.csv', 'w', newline='') as csvfile:
    fieldnames = ['token', 'count']
    writer = csv.writer(csvfile)
    writer.writerow(fieldnames)
    writer.writerows(top_30_tokens)

print("Top 30 tokens have been saved to 'top_30_tokens.csv'.")
