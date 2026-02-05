# 🛒 Flipkart Product Review Sentiment Analysis

This project is a real-time sentiment analysis web application that predicts whether a Flipkart product review is **Positive** or **Negative** using Natural Language Processing (NLP) and Machine Learning.  
It is designed to help understand customer feedback and support better decision-making using data.

---

## 🚀 Live Demo

🔗 Try the application here:  
https://nasir331786-flipkart-review-sentiment-anal-sentiment-app-rr0odo.streamlit.app/

---

## 📌 Project Overview

Customer reviews play a major role in online shopping. This project analyzes Flipkart product reviews and classifies them based on sentiment (positive or negative).  
The system uses a trained machine learning model along with text processing techniques to automatically understand customer opinions.  
This project was built as part of my learning journey in **Data Science**, **NLP**, and **Model Deployment**.

---

## ✨ Key Features

- ✅ Real-time sentiment prediction  
- ✅ Simple and user-friendly Streamlit interface  
- ✅ Machine learning–based classification  
- ✅ TF-IDF–based text vectorization  
- ✅ Supports Positive and Negative reviews  
- ✅ Emoji-based result display 😊 😞  

---

## 🛠️ Technologies Used

- **Python 3**  
- **Streamlit** – Web framework  
- **scikit-learn** – Machine learning  
- **pandas** – Data handling  
- **numpy** – Numerical operations  
- **nltk** – Text preprocessing  
- **pickle / joblib** – Model storage  

---

## 📂 Project Structure

```text
Flipkart-Sentiment-Analysis/
│
├── sentiment_app.py             # Streamlit web application
├── sentiment_model.pkl          # Trained ML model
├── tfidf_vectorizer.pkl         # TF-IDF vectorizer
├── sentimental_analysis.ipynb   # Notebook for training and evaluation
├── data.csv                     # Flipkart reviews dataset
├── requirements.txt             # Python dependencies
└── README.md                    # Project documentation
```

---

## ⚙️ Installation & Setup

### Prerequisites

- Python 3.7+  
- `pip` installed

### Run Locally

1️⃣ **Clone the repository**

```bash
git clone https://github.com/nasir331786/flipkart-review-sentiment-analyzer
```

2️⃣ **Install dependencies**

```bash
pip install -r requirements.txt
```

3️⃣ **Run the app**

```bash
streamlit run sentiment_app.py
```

4️⃣ **Open in browser**

Go to: `http://localhost:8501`

---

## 📊 Model Details

- **Algorithm:** Logistic Regression / Naive Bayes  
- **Vectorization:** TF-IDF  
- **Type:** Binary Classification  
- **Labels:** Positive / Negative  
- **Training Data:** Flipkart Reviews Dataset  

---

## 🔄 How the System Works

1. User enters a product review.  
2. Text is cleaned and preprocessed.  
3. TF-IDF converts text into numerical features.  
4. The trained model predicts the sentiment.  
5. The result is displayed on screen with an emoji.

---

## 🧪 Sample Output

**Positive Review**

- Input: `This product is amazing and very useful.`  
- Output: ✅ Positive Review 😊  

**Negative Review**

- Input: `Very bad quality and waste of money.`  
- Output: ❌ Negative Review 😞  

---

## 📦 Dependencies

Main libraries:

- streamlit  
- scikit-learn  
- pandas  
- numpy  
- nltk  
- joblib  

See `requirements.txt` for the full list of dependencies.

---

## 📈 Model Training Process

The model was trained using the following steps:

1. Data collection  
2. Text cleaning and preprocessing  
3. Stopword removal and lemmatization  
4. TF-IDF feature extraction  
5. Model training and evaluation  
6. Saving the trained model  

Details are available in `sentimental_analysis.ipynb`.

---

## ☁️ Deployment

This project is deployed using **Streamlit Cloud**, making it accessible online without managing your own server.

### Deploy Your Own Version

1. Fork this repository.  
2. Create a Streamlit Community Cloud account.  
3. Connect your GitHub repository.  
4. Configure the app to run `sentiment_app.py`.  
5. Deploy with one click.

---

## 🚀 Future Enhancements

- BERT-based deep learning model  
- Multi-class sentiment analysis  
- Database integration for storing reviews  
- Advanced UI with analytics and charts  
- Docker setup and CI/CD pipeline  

---

## 👨‍💻 Developer

**Nasir Husain**  
Data Science & Machine Learning Enthusiast  

- GitHub: [https://github.com/nasir331786](https://github.com/nasir331786)

---

## 🙏 Acknowledgments

- Flipkart Reviews Dataset  
- Streamlit Community  
- scikit-learn Documentation  

---

## 📬 Contact

For suggestions or feedback, please open an issue on GitHub.

⭐ If you found this project useful, please consider giving it a star!
