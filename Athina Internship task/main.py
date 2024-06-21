from pinecone import Pinecone
from langchain_community.embeddings import OllamaEmbeddings
from pinecone.grpc import PineconeGRPC as Pinecone
from groq import Groq
import streamlit as st
def answer(question,model_selector,temperature_,max_tokens_,top_p_,stream_,stop_,seed_):
    pc = Pinecone(api_key="72c738f8-0dd0-4c1d-b550-876aa044bdeb")
    index = pc.Index("internship")
    input=question
    embeddings = OllamaEmbeddings(model='llama3:latest')
    query_result = embeddings.embed_query(input)
    response_data = index.query(
         vector=query_result,
         top_k=3,
        include_metadata=True
    )
    first_match = response_data['matches'][0]
# Extract details from the first match
    match_id = first_match['id']
    match_score = first_match['score']
# Extract name from metadata if available
    match_metadata = first_match['metadata']
    name = match_metadata.get('text') if match_metadata is not None else None
    client = Groq()
    completion = client.chat.completions.create(
        model=model_selector,
         messages=[
            {
                 "role": "system",
                 "content": "You are a Friendly chatbot for a car insurance policy booklet for Churchill that answers the question according to the context.Question-"+question+"Context-"+name
            },
            {
                    "role": "user",
                "content": input
             },
        
        ],
        temperature=temperature_,
        max_tokens=max_tokens_,
        top_p=top_p_,
        stream=stream_,
        stop=stop_,
        seed=seed_
    )
    return completion.choices[0].message.content,name
    
def main():
    
    st.title("RAG Based PDF Chatbot for Athina AI")
    model_selector = "llama3-70b-8192"
    default_temperature = 0.9
    default_max_tokens = 8192
    default_top_p = 0.45
    default_stream = False
    default_stop = None
    default_seed = 1

    st.sidebar.header('Adjust LLM Parameters')

    model_selector= st.sidebar.selectbox('Model', options=[ "llama3-70b-8192","gemma-7b-it","llama3-8b-8192","mixtral-8x7b-32768"], index=0)
    if model_selector=="gemma-7b-it":
        default_max_tokens=8192
    if model_selector=="llama3-70b-8192":
        default_max_tokens=8192
    if model_selector=="llama3-8b-8192":
        default_max_tokens=8192
    if model_selector=="mixtral-8x7b-32768":
         default_max_tokens=32768 


    temperature = st.sidebar.slider('Temperature', min_value=0.0, max_value=2.0, value=default_temperature, step=0.01)
    max_tokens = st.sidebar.slider('Max Tokens', min_value=1, max_value=default_max_tokens, value=default_max_tokens, step=1)
    top_p = st.sidebar.slider('Top-p (nucleus sampling)', min_value=0.0, max_value=1.0, value=default_top_p, step=0.01)
    stream = st.sidebar.checkbox('Stream', value=default_stream)
    stop = st.sidebar.text_input('Stop sequence', value='' if default_stop is None else default_stop)
    seed = st.sidebar.number_input('Seed', min_value=0, max_value=1000000, value=default_seed, step=1)    

     # Initialize chat session state if not already done
    if "messages" not in st.session_state:
                st.session_state.messages = []
            
            # Display previous messages
    for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])
            
            # Handle new chat input
    if prompt := st.chat_input("Ask something about the Car Insurance Policy Booklet"):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
                    st.markdown(prompt)
                
        with st.chat_message("assistant"):
            response,name = answer(prompt,model_selector,temperature,max_tokens,top_p,stream,stop,seed)
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.markdown(response)
            st.markdown(name)
            
        

if __name__ == "__main__":
    main()       

                
