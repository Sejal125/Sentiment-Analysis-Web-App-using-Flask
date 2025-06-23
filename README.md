📊 Sentiment Analysis Web App using Flask
This project is a complete sentiment analysis web application built using Python and Flask. It classifies long Amazon product reviews into Positive, Negative, or Neutral sentiments. The goal was to build a real-world, production-style ML project with both frontend and backend integration.

🛠️ Technologies & Libraries Used
🧠 Machine Learning & NLP
pandas – for data loading and manipulation

numpy – for numeric operations

sklearn – for model training and vectorization

TfidfVectorizer, MultinomialNB, LogisticRegression, Pipeline, train_test_split

nltk – for stopwords and text cleaning

joblib – for saving and loading trained models efficiently

re – for regex-based text cleaning

🌐 Web Framework & Frontend
Flask – to create backend routes and handle HTTP requests

Jinja2 – for rendering dynamic content in HTML templates

HTML5, CSS3 – for designing a simple and clean UI

Custom styling with hover effects, box shadows, and beige-brown color palette

📂 Dataset Source
I used the Amazon Reviews Dataset from Kaggle. It consists of reviews with labels:

__label__1 → 1-2 star reviews (Negative)

__label__2 → 4-5 star reviews (Positive)

Neutral sentiment (3-star reviews) was not in the original dataset but I retained neutral-like reviews during preprocessing wherever relevant.

🎓 What I Learned
Full ML pipeline development and deployment

Handling and preprocessing large datasets in .bz2 format

Training two classifiers: Naive Bayes and Logistic Regression

Building a clean Flask web app from scratch

Saving models with joblib and integrating them with Flask

Designing responsive and elegant user interfaces with plain HTML/CSS
