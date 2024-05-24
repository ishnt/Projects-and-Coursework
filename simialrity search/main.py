import streamlit as st
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
st.set_option('deprecation.showPyplotGlobalUse', False)
def main():
    st.title("Sentence Embeddings Visualization")
    markdown_text = """
Cosine similarity is a metric used to measure the similarity between two vectors in a high-dimensional space. It calculates the cosine of the angle between the vectors, which is a measure of their alignment. Cosine similarity is widely used in various fields, including natural language processing, information retrieval, and recommendation systems.

In the context of natural language processing, cosine similarity is often used to compare the similarity between word embeddings or document embeddings. Word embeddings are dense vector representations of words, while document embeddings represent entire documents as vectors. By computing the cosine similarity between these embeddings, we can determine how similar two words or documents are in meaning or content.

Cosine similarity ranges from -1 to 1, where:
- A value of 1 indicates that the vectors are perfectly aligned and have the same orientation.
- A value of -1 indicates that the vectors are perfectly aligned but have opposite orientations.
- A value of 0 indicates that the vectors are orthogonal (i.e., perpendicular) to each other.
"""
    st.markdown(markdown_text)

    # Input sentences
    sentence1 = st.text_input("Enter sentence 1:")
    sentence2 = st.text_input("Enter sentence 2:")

    if sentence1 and sentence2:
        # Compute embeddings
        model = SentenceTransformer('sentence-transformers/all-MiniLM-L6-v2')
        embeddings1 = model.encode(sentence1)
        embeddings2 = model.encode(sentence2)

        # Compute cosine similarity
        similarity = cosine_similarity([embeddings1], [embeddings2])[0][0]
        # Show similarity
        st.write(f"Cosine Similarity: {similarity:.2f}")
        # Plot embeddings
        plt.figure(figsize=(8, 6))
        plt.scatter(range(len(embeddings1)), embeddings1, color='red', label='Sentence 1')
        plt.scatter(range(len(embeddings2)), embeddings2, color='blue', label='Sentence 2')
        plt.title("Sentence Embeddings Visualization")
        plt.xlabel("Index")
        plt.ylabel("Value")
        plt.legend()
        plt.grid(True, linestyle='--', alpha=0.7)

       

        # Show plot
        st.pyplot()

if __name__ == "__main__":
    main()