# 📊 Sentiment Analysis Web App using Flask

This project is a complete sentiment analysis web application built using Python and Flask. It classifies long Amazon product reviews into **Positive**, **Negative**, or **Neutral** sentiments. The goal was to build a real-world, production-style ML project with both frontend and backend integration.

---

## 🛠️ Technologies & Libraries Used

### 🧠 Machine Learning & NLP
- **pandas** – for data loading and manipulation  
- **numpy** – for numeric operations  
- **scikit-learn (sklearn)** – for model training and vectorization  
  - `TfidfVectorizer`, `MultinomialNB`, `LogisticRegression`, `Pipeline`, `train_test_split`
- **nltk** – for stopwords and text cleaning  
- **joblib** – for saving and loading trained models efficiently  
- **re** – for regex-based text cleaning

### 🌐 Web Framework & Frontend
- **Flask** – to create backend routes and handle HTTP requests  
- **Jinja2** – for rendering dynamic content in HTML templates  
- **HTML5**, **CSS3** – for designing a simple and clean UI  
- Custom styling with hover effects, box shadows, and a beige-brown color palette

---

## 📂 Dataset Source

I used the [Amazon Reviews Dataset from Kaggle](https://www.kaggle.com/datasets/bittlingmayer/amazonreviews). It consists of reviews with labels:

- `__label__1` → 1-2 star reviews (**Negative**)  
- `__label__2` → 4-5 star reviews (**Positive**)



## 🎓 What I Learned

- How to build a full ML pipeline from preprocessing to model deployment  
- How to process large `.bz2` compressed files  
- Trained and compared two models: **Naive Bayes** and **Logistic Regression**  
- Built a Flask backend integrated with real ML models  
- Saved and used models in production with `joblib`  
- Designed a clean, user-friendly interface with basic HTML and CSS
