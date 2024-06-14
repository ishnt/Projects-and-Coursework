from content import text
import numpy as np
from langchain_community.embeddings import OllamaEmbeddings
from pinecone import Pinecone, ServerlessSpec
import pandas as pd
text1 =text  # your text
from langchain.text_splitter import RecursiveCharacterTextSplitter
text_splitter = RecursiveCharacterTextSplitter(
    # Set a really small chunk size, just to show.
    chunk_size = 5000,
    chunk_overlap  = 500
)
pc = Pinecone(api_key="72c738f8-0dd0-4c1d-b550-876aa044bdeb")
def embedder(text,counter):
    embeddings = OllamaEmbeddings(model='llama3')
    # Get the embedding of the text
    query_result = embeddings.embed_query(text)
    # Connect to the index
    index = pc.Index(name="internship")
    # Prepare the data for upserting
    embedding_id = counter
    embedding_vector = query_result  # Directly use the list
    metadata = {"text": text}  # Include the original text as metadata
    index.upsert([(embedding_id, embedding_vector, metadata)])
    
docs = text_splitter.create_documents([text1])
for i in range(24):
   embedder(docs[i].page_content,str(i))
   print(i)