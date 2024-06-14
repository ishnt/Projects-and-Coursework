from pinecone import Pinecone
from langchain_community.embeddings import OllamaEmbeddings
from pinecone.grpc import PineconeGRPC as Pinecone
from groq import Groq
pc = Pinecone(api_key="72c738f8-0dd0-4c1d-b550-876aa044bdeb")
index = pc.Index("internship")
input="phone number and email address"
embeddings = OllamaEmbeddings(model='llama3:latest')
query_result = embeddings.embed_query(input)
response_data = index.query(
    vector=query_result,
    top_k=1,
    include_metadata=True
   )
first_match = response_data['matches'][0]
# Extract details from the first match
match_id = first_match['id']
match_score = first_match['score']
# Extract name from metadata if available
match_metadata = first_match['metadata']
name = match_metadata.get('text') if match_metadata is not None else None
print(name)
client = Groq()
completion = client.chat.completions.create(
    model="llama3-70b-8192",
    messages=[
        {
            "role": "system",
            "content": "You are a Friendly chatbot for a car insurance policy booklet for Churchill that gives answer according to the context-"+name
        },
        {
            "role": "user",
            "content": input
        },
        
    ],
    temperature=1,
    max_tokens=8192,
    top_p=1,
    stream=True,
    stop=None,
)

for chunk in completion:
    print(chunk.choices[0].delta.content or "", end="")
