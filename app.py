
from flask import Flask, render_template, request
import joblib

app = Flask(__name__)

# Load pre-trained models
nb_model = joblib.load("naive_model.pkl")
lr_model = joblib.load("logistic_model.pkl")

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    model_choice = None

    if request.method == "POST":
        user_text = request.form.get("review")  # ✅ matched with HTML
        model_choice = request.form.get("model_choice")  # ✅ matched with HTML

        if user_text and model_choice:
            if model_choice == "naive":
                prediction = nb_model.predict([user_text])[0]
            elif model_choice == "logistic":
                prediction = lr_model.predict([user_text])[0]

    return render_template("index.html", prediction=prediction, model=model_choice)

if __name__ == "__main__":
    app.run(debug=True)



    # .\myenv\Scripts\Activate
