import os
import getpass
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_pinecone import PineconeVectorStore
from langchain_community.document_loaders import PyMuPDFLoader
os.environ['PINECONE_API_KEY'] = '72c738f8-0dd0-4c1d-b550-876aa044bdeb'
# Load the document, split it into chunks, and embed each chunk.
loader = PyMuPDFLoader("policy-booklet-0923.pdf")
data = loader.load()
print(data[0])
text_splitter = CharacterTextSplitter(chunk_size=5000, chunk_overlap=1000)
docs = text_splitter.split_documents(data)

embeddings = OllamaEmbeddings(model='llama3')
index_name = "internship"
docsearch = PineconeVectorStore.from_documents(docs, embeddings, index_name=index_name)