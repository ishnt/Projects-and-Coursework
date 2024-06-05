import numpy as np
from langchain_community.embeddings import OllamaEmbeddings
from pinecone import Pinecone, ServerlessSpec
import pandas as pd
def embedder(text,counter):
    embeddings = OllamaEmbeddings(model='llama3')
    # Get the embedding of the text
    query_result = embeddings.embed_query(text)
    # Connect to the index
    index = pc.Index(name="quickstart")
    # Prepare the data for upserting
    embedding_id = counter
    embedding_vector = query_result  # Directly use the list
    metadata = {"text": text}  # Include the original text as metadata
    index.upsert([(embedding_id, embedding_vector, metadata)])

# Initialize Pinecone
pc = Pinecone(api_key="72c738f8-0dd0-4c1d-b550-876aa044bdeb")
# Define your text
def process_csv_column(csv_file_path, column_name):
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
    counter=1
    # Iterate over each row in the specified column
    for index, row in df.iterrows():
        
        text = row[column_name]
        embedder(text,str(counter))
        counter=counter+1
        print(counter)
        
        
csv_file_path = 'urdu_poems.csv'  # Replace with the actual path to your CSV file
column_name = 'urdu_poems'  # Replace with the actual column name
process_csv_column(csv_file_path, column_name)   





