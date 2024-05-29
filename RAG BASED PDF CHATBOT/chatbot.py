import fitz  # PyMuPDF
import streamlit as st
import io
from groq import Groq

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
                "content": f"You are a pdf chatbot which answers with pdf content \nHere's the pdf content \n\"{text}\""
            },
            {
                "role": "user",
                "content": query
            },
        ],
        temperature=1,
        max_tokens=1024,
        top_p=1,
        stream=True,
        stop=None,
    )
    
    response = ""
    for chunk in completion:
        content = chunk.choices[0].delta.content
        if content:  # Ensure content is not None
            response += content
    
    return response

def main():
    st.title("PDF to Text Converter")
    # File uploader
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")
    user_input = st.text_input("Enter Your Query")
    
    # Add a button to submit the file and convert it to text
    if st.button("Submit"):
        if uploaded_file is not None:
            # Convert PDF to text
            global text
            text = pdf_to_text(uploaded_file)
            if text:
                st.write("PDF content extracted successfully.")
                response = generate_response(text, user_input)
                st.write(response)
                if "messages" not in st.session_state:
                    st.session_state.messages = []
                for message in st.session_state.messages:
                    with st.chat_message(message["role"]):
                        st.markdown(message["content"])    
                if prompt := st.chat_input("What is up?"):
                     st.session_state.messages.append({"role": "user", "content": prompt})
                     with st.chat_message("user"):
                         st.markdown(prompt)
                     with st.chat_message("assistant"):
                         response = st.write_stream(generate_response(text, user_input))
                         st.session_state.messages.append({"role": "assistant", "content": response})        
                
            else:
                st.error("Failed to extract text from the PDF.")
        else:
            st.error("Please upload a PDF file.")
            
            
   
if __name__ == "__main__":
    main()
