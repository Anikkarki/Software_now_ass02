import pandas as pd
from collections import Counter
import re
import csv
from transformers import AutoTokenizer
from multiprocessing import Pool, cpu_count

# Define the path to the CSV files and their respective text columns
csv_files = {
    "CSV1.csv": "SHORT-TEXT",  
    "CSV2.csv": "entites",  
    "CSV3.csv": "TEXT",  
    "CSV4.csv": "TEXT", 
}

# Load the tokenizer for BERT
tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

# Function to consolidate text from each CSV file separately
def consolidate_text(csv_file, text_column):
    df = pd.read_csv(csv_file)
    if text_column in df.columns:
        return "\n".join(df[text_column].dropna())
    else:
        print(f"Column '{text_column}' not found in {csv_file}. Available columns: {df.columns}")
        return ""

# Function to count word occurrences
def count_words(text):
    words = re.findall(r'\w+', text.lower())  # Extract words and convert to lowercase
    word_counts = Counter(words)
    return word_counts

# Function to count token occurrences
def count_tokens(text):
    tokens = tokenizer.tokenize(text)
    token_counts = Counter(tokens)
    return token_counts

# Process each file: consolidate, count tokens, and save to CSV
def process_file(csv_file, text_column):
    # Consolidate text
    csv_text = consolidate_text(csv_file, text_column)

    # Tokenize the text
    token_counts = count_tokens(csv_text)

    # Get the top 30 most common tokens
    top_30_tokens = token_counts.most_common(30)

    # Save the top 30 tokens to a separate CSV file
    token_output_file = f'top_30_tokens_{csv_file}.csv'
    with open(token_output_file, 'w', newline='') as csvfile:
        fieldnames = ['token', 'count']
        writer = csv.writer(csvfile)
        writer.writerow(fieldnames)
        writer.writerows(top_30_tokens)

    print(f"Top 30 tokens for {csv_file} have been saved to '{token_output_file}'.")
    return csv_file  # Return the processed file name

# Parallelize the file processing
if __name__ == "__main__":
    # Create a pool of workers equal to the number of CPU cores
    pool = Pool(cpu_count())

    # Parallel processing for all files
    results = pool.starmap(process_file, csv_files.items())

    # Close the pool
    pool.close()
    pool.join()

    print("Tokenization for all CSV files is complete.")
