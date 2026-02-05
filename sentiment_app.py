import streamlit as st
import joblib
import re
import nltk
import os

from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer


# download nltk data (one time)
if not os.path.exists("nltk_data"):

    nltk.download("stopwords")
    nltk.download("wordnet")


# load model and vectorizer
try:

    model = joblib.load("sentiment_model.pkl")
    vectorizer = joblib.load("tfidf_vectorizer.pkl")

except:

    st.error("Model files not found. Please upload .pkl files.")
    st.stop()


# setup text processing tools
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()


# function to clean review text
def clean_text(text):

    if text is None:
        return ""

    text = str(text).lower()

    text = re.sub(r"[^a-zA-Z ]", " ", text)

    words = text.split()

    final_words = []

    for word in words:

        if word not in stop_words:

            word = lemmatizer.lemmatize(word)

            final_words.append(word)

    return " ".join(final_words)


# page settings
st.set_page_config(
    page_title="Flipkart Sentiment Analyzer",
    page_icon="🛒"
)


# sidebar
st.sidebar.title("Project Info")

st.sidebar.write("Flipkart Review Sentiment Analysis")
st.sidebar.write("Machine Learning + NLP")
st.sidebar.write("Deployed using Streamlit")
st.sidebar.write("Developer: Nasir Husain")


# main title
st.title("🛒 Flipkart Product Review Analyzer")

st.write("This tool predicts whether a product review is positive or negative.")


# input area
review = st.text_area(
    "Enter product review",
    height=150
)


# predict button
if st.button("Analyze Review"):


    if review.strip() == "":

        st.warning("Please enter a review first.")


    else:

        with st.spinner("Analyzing review..."):

            clean_review = clean_text(review)

            vector = vectorizer.transform([clean_review])

            prediction = model.predict(vector)[0]


        if prediction == 1:

            st.success("✅ Positive Review")

            st.write("Customer is satisfied with the product😊.")


        else:

            st.error("❌ Negative Review")

            st.write("Customer is unhappy with the product😞.")


# footer
st.write("This project was built to strengthen my Data Science skills")
 
st.write("Powered by Python, NLP and Machine Learning")
