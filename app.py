
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

#for your use only use this following code:
#if __name__ == "__main__":
 #   app.run(debug=True)

#for deploying it to render :
import os

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use Render-assigned port
    app.run(debug=False, host="0.0.0.0", port=port)



    # .\myenv\Scripts\Activate
