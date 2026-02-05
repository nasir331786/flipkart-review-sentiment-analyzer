# 🛒 Flipkart Product Review Sentiment Analysis

A real-time sentiment analysis application that classifies Flipkart product reviews as **Positive** or **Negative** using Natural Language Processing (NLP) and Machine Learning techniques.

## 🚀 Live Demo

**Try the app here:** [Flipkart Sentiment Analyzer](https://flipkart-sentiment-analysis-nypefhplen7wjr3db3336w.streamlit.app/)

## 📋 Project Overview

This project analyzes customer reviews from Flipkart to determine sentiment polarity. The application uses a machine learning model trained on product reviews to classify text as positive or negative sentiment, helping businesses understand customer feedback at scale.

## ✨ Features

- ✅ Real-time sentiment prediction
- ✅ User-friendly Streamlit web interface
- ✅ Pre-trained machine learning model
- ✅ TF-IDF vectorization for text processing
- ✅ Binary classification (Positive/Negative)
- ✅ Clean and intuitive UI with emoji indicators

## 🛠️ Tech Stack

- **Python 3.x**
- **Streamlit** - Web application framework
- **scikit-learn** - Machine learning library
- **pandas** - Data manipulation
- **pickle** - Model serialization

## 📂 Project Structure

```
Flipkart-Sentiment-Analysis/
│
├── sentiment_app.py              # Streamlit application
├── sentiment_model.pkl            # Trained ML model
├── tfidf_vectorizer.pkl           # TF-IDF vectorizer
├── sentimental_analysis.ipynb     # Jupyter notebook for model training
├── data.csv                       # Dataset
├── requirements.txt               # Python dependencies
└── README.md                      # Project documentation
```

## 🔧 Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Steps to Run Locally

1. **Clone the repository**
   ```bash
   git clone https://github.com/Vasanth4321/Flipkart-Sentiment-Analysis.git
   cd Flipkart-Sentiment-Analysis
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**
   ```bash
   streamlit run sentiment_app.py
   ```

4. **Open your browser**
   - The app will automatically open at `http://localhost:8501`

## 📊 Model Information

- **Algorithm:** Logistic Regression / Naive Bayes (based on model training)
- **Text Vectorization:** TF-IDF (Term Frequency-Inverse Document Frequency)
- **Classes:** Binary classification (Positive, Negative)
- **Training Data:** Flipkart product reviews dataset

## 🎯 How It Works

1. **User Input:** Enter a product review in the text area
2. **Text Preprocessing:** The review is cleaned and preprocessed
3. **Vectorization:** Text is converted to numerical features using TF-IDF
4. **Prediction:** Machine learning model classifies the sentiment
5. **Display Result:** Shows whether the review is Positive 😊 or Negative 😞

## 📸 Screenshots

### Application Interface
The application features a clean, dark-themed interface where users can:
- Enter product reviews
- Get instant sentiment predictions
- See color-coded results (Green for Positive, Red for Negative)

## 🧪 Example Usage

**Positive Review:**
```
Input: "This product is amazing! Great quality and fast delivery. Highly recommended!"
Output: ✅ Positive Review 😊
```

**Negative Review:**
```
Input: "Terrible product! Poor quality, delivery was late, and customer service was horrible."
Output: ❌ Negative Review 😞
```

## 📦 Dependencies

Key libraries used in this project:
```
streamlit
scikit-learn
pandas
numpy
pickle
```

For complete list, see `requirements.txt`

## 🔍 Model Training

The model was trained using the following pipeline:
1. Data collection from Flipkart reviews
2. Text preprocessing (cleaning, tokenization)
3. Feature extraction using TF-IDF
4. Model training and evaluation
5. Model serialization using pickle

For detailed training process, refer to `sentimental_analysis.ipynb`

## 🚀 Deployment

This application is deployed on **Streamlit Cloud** for easy access and sharing.

### Deploy Your Own Version
1. Fork this repository
2. Sign up at [Streamlit Cloud](https://streamlit.io/cloud)
3. Connect your GitHub repository
4. Deploy with one click!

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 👨‍💻 Author

**Vasanth**
- GitHub: [@Vasanth4321](https://github.com/Vasanth4321)

## 🙏 Acknowledgments

- Dataset sourced from Flipkart product reviews
- Built with Streamlit framework
- Machine learning powered by scikit-learn

## 📧 Contact

For any queries or feedback, please open an issue in this repository.

---

⭐ If you found this project helpful, please consider giving it a star!
