import streamlit as st
from transformers import AutoModelForSequenceClassification, AutoTokenizer, AutoConfig
import numpy as np
from scipy.special import softmax

# Preprocess text (username and link placeholders)
def preprocess(text):
    new_text = []
    for t in text.split(" "):
        t = '@user' if t.startswith('@') and len(t) > 1 else t
        t = 'http' if t.startswith('http') else t
        new_text.append(t)
    return " ".join(new_text)

MODEL = f"cardiffnlp/twitter-roberta-base-sentiment-latest"
tokenizer = AutoTokenizer.from_pretrained(MODEL)
config = AutoConfig.from_pretrained(MODEL)


def load_model():
    return AutoModelForSequenceClassification.from_pretrained(MODEL)

model = load_model()

st.title("Speech Sentiment Analysis")
markdown_content = """
## How Embeddings are Used in Sentiment Analysis

### Word Embeddings
Words are represented as dense vectors in a high-dimensional space. Pre-trained word embeddings like Word2Vec, GloVe, or FastText are commonly used. These embeddings are learned from large text corpora and capture semantic relationships between words.

### Sentence/Document Embeddings
Sentences or documents are represented as a combination of word embeddings. This can be achieved through techniques like averaging the embeddings of individual words or using more sophisticated methods like Doc2Vec or Universal Sentence Encoder.

### Calculating Sentiment
Once the text is represented as embeddings, sentiment analysis algorithms can be applied. This can involve techniques such as:

- **Classification:** Using machine learning algorithms like Support Vector Machines (SVM), Naive Bayes, or deep learning models like Convolutional Neural Networks (CNNs) or Recurrent Neural Networks (RNNs) to classify the sentiment of the text based on its embeddings.

- **Regression:** Predicting a continuous sentiment score for the text using regression techniques.

- **Lexicon-Based Methods:** Using sentiment lexicons or dictionaries to map words to sentiment scores and aggregating them to determine the sentiment of the text.
"""
text = st.text_input("Enter the Speech:")
# Input sentence

if text:
    text = preprocess(text)
    encoded_input = tokenizer(text, return_tensors='pt')
    print(encoded_input)
    output = model(**encoded_input)
    print(output)
    scores = output[0][0].detach().numpy()
    scores = softmax(scores)
    
    # Print labels and scores
    ranking = np.argsort(scores)
    ranking = ranking[::-1]
    st.subheader("Sentiment Scores:")
    for i in range(scores.shape[0]):
        label = config.id2label[ranking[i]]
        score = scores[ranking[i]]
        st.write(f"{label}: {np.round(float(score), 4)}")
st.markdown(markdown_content)

