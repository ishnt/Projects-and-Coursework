import fitz  # PyMuPDF
import streamlit as st
import io
from groq import Groq
import streamlit as st
import base64 
# Set default values for the parameters
default_model = "llama3-70b-8192"
default_temperature = 0.9
default_max_tokens = 8192
default_top_p = 0.45
default_stream = False
default_stop = None
default_seed = 1

# Create the sidebar
st.sidebar.header('Adjust LLM Parameters')

model = st.sidebar.selectbox('Model', options=[ "llama3-70b-8192","gemma-7b-it","llama3-8b-8192","mixtral-8x7b-32768"], index=0)
if model=="gemma-7b-it":
    default_max_tokens=8192
if model=="llama3-70b-8192":
    default_max_tokens=8192
if model=="llama3-8b-8192":
    default_max_tokens=8192
if model=="mixtral-8x7b-32768":
    default_max_tokens=32768       
    
temperature = st.sidebar.slider('Temperature', min_value=0.0, max_value=2.0, value=default_temperature, step=0.01)
max_tokens = st.sidebar.slider('Max Tokens', min_value=1, max_value=default_max_tokens, value=default_max_tokens, step=1)
top_p = st.sidebar.slider('Top-p (nucleus sampling)', min_value=0.0, max_value=1.0, value=default_top_p, step=0.01)
stream = st.sidebar.checkbox('Stream', value=default_stream)
stop = st.sidebar.text_input('Stop sequence', value='' if default_stop is None else default_stop)
seed = st.sidebar.number_input('Seed', min_value=0, max_value=1000000, value=default_seed, step=1)

def pdf_to_text(file):
    """
    Convert a PDF file to text.

    Args:
        file: A file-like object representing the PDF file.

    Returns:
        str: The extracted text from the PDF.
    """
    try:
        # Read the file into bytes
        pdf_data = file.read()
        
        # Open the PDF file from bytes
        document = fitz.open(stream=io.BytesIO(pdf_data), filetype="pdf")
        text = ""
        # Iterate through the pages and extract text
        for page_num in range(len(document)):
            page = document.load_page(page_num)
            text += page.get_text()

        return text
    except Exception as e:
        st.error(f"An error occurred: {e}")
        return None

def generate_response(text, query):
    if text is None:
        return "No text extracted from the PDF."
    
    client = Groq()
    completion = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[
            {
                "role": "system",
                "content": f"You are a pdf chatbot which answers with pdf content. Here is the PDF content: \"{text}\""
            },
            {
                "role": "user",
                "content": query
            },
        ],
        temperature=temperature,
        max_tokens=max_tokens,
        top_p=top_p,
        stream=stream,
        stop=stop,
        seed=seed
    )
    
   
    
    return completion.choices[0].message.content

def main():
    
    st.title("PDF Chatbot")
    st.write("Upload a PDF file and chat with the content.")
    
    # File uploader
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    
    if uploaded_file is not None:
        # Convert PDF to text
        text = pdf_to_text(uploaded_file)
        if text:
            st.write("PDF content extracted successfully.")
            
            # Initialize chat session state if not already done
            if "messages" not in st.session_state:
                st.session_state.messages = []
            
            # Display previous messages
            for message in st.session_state.messages:
                with st.chat_message(message["role"]):
                    st.markdown(message["content"])
            
            # Handle new chat input
            if prompt := st.chat_input("Ask something about the PDF..."):
                st.session_state.messages.append({"role": "user", "content": prompt})
                with st.chat_message("user"):
                    st.markdown(prompt)
                
                with st.chat_message("assistant"):
                    response = generate_response(text, prompt)
                    st.session_state.messages.append({"role": "assistant", "content": response})
                    st.markdown(response)
        else:
            st.error("Failed to extract text from the PDF.")
    

if __name__ == "__main__":
    main()
