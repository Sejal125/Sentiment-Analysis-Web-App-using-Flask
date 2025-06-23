#  app.py — Main Flask App for Sentiment Analysis

from flask import Flask, render_template, request
import joblib  # ✅ use joblib instead of pickle

# Initialize the Flask application
app = Flask(__name__)

# Load pre-trained models using joblib
nb_model = joblib.load("naive_model.pkl")
lr_model = joblib.load("logistic_model.pkl")

# Define route for homepage
@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    model_choice = None

    if request.method == "POST":
        user_text = request.form.get("user_input")  #  Get text input from user
        model_choice = request.form.get("model")     #  Model selection

        # 📈 Choose model based on user input
        if model_choice == "naive_bayes":
            prediction = nb_model.predict([user_text])[0]
        elif model_choice == "logistic_regression":
            prediction = lr_model.predict([user_text])[0]

    return render_template("index.html", prediction=prediction, model=model_choice)


#  Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
