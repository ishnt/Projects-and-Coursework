import os
import pandas as pd
import chardet

# Define the folder containing the text files
folder_path = r'dataset\dataset\all'  # Use raw string or double backslashes

# Check if the folder exists
if not os.path.exists(folder_path):
    print(f"The folder {folder_path} does not exist.")
    exit()

# Initialize a list to store the contents of the files
urdu_poems = []

# Function to detect file encoding
def detect_encoding(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read()
    result = chardet.detect(raw_data)
    return result['encoding']

# Iterate over all the files in the folder
try:
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):  # Ensure it's a file, not a directory
            # Detect file encoding
            encoding = detect_encoding(file_path)
            print(f"Detected encoding for {filename}: {encoding}")  # Debugging output
            try:
                with open(file_path, 'r', encoding=encoding) as file:
                    content = file.read()
                    urdu_poems.append(content)
            except Exception as read_error:
                print(f"Could not read file {filename} with encoding {encoding}: {read_error}")
except Exception as e:
    print(f"An error occurred: {e}")
    exit()

def process_csv_column(csv_file_path, column_name, process_function):
    """
    Process each row in the specified column of a CSV file using the given process_function.

    Parameters:
        csv_file_path (str): The path to the CSV file.
        column_name (str): The name of the column to process.
        process_function (callable): A function that takes a text input and performs processing.

    Returns:
        None
    """
    # Read the CSV file
    df = pd.read_csv(csv_file_path)
    
    # Iterate over each row in the specified column
    for index, row in df.iterrows():
        text = row[column_name]
        process_function(text)
        
csv_file_path = 'urdu_poems.csv'  # Replace with the actual path to your CSV file
column_name = 'urdu_poems'  # Replace with the actual column name
process_csv_column(csv_file_path, column_name, example_process_function)        