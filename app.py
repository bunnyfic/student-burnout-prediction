from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import joblib
import os
import webbrowser
from threading import Timer

app = Flask(__name__)

# ==========================
# Load Models
# ==========================

burnout_model = joblib.load("burnout_model.pkl")
dropout_model = joblib.load("dropout_model.pkl")


# ==========================
# Home Page
# ==========================

@app.route("/")
def home():
    return render_template("index.html")


# ==========================
# Prediction
# ==========================

@app.route("/predict", methods=["POST"])
def predict():

    study_hours = float(request.form["study_hours"])
    exam_pressure = float(request.form["exam_pressure"])
    stress_level = float(request.form["stress_level"])
    anxiety_score = float(request.form["anxiety_score"])
    depression_score = float(request.form["depression_score"])
    sleep_hours = float(request.form["sleep_hours"])
    physical_activity = float(request.form["physical_activity"])
    social_support = float(request.form["social_support"])
    financial_stress = float(request.form["financial_stress"])
    family_expectation = float(request.form["family_expectation"])
    mental_health_index = float(request.form["mental_health_index"])


    # Create dataframe exactly like training data

    user_input = pd.DataFrame({

        "study_hours_per_day":[study_hours],

        "exam_pressure":[exam_pressure],

        "stress_level":[stress_level],

        "anxiety_score":[anxiety_score],

        "depression_score":[depression_score],

        "sleep_hours":[sleep_hours],

        "physical_activity":[physical_activity],

        "social_support":[social_support],

        "financial_stress":[financial_stress],

        "family_expectation":[family_expectation],

        "mental_health_index":[mental_health_index]

    })


    # =======================
    # Burnout Prediction
    # =======================

    burnout_score = burnout_model.predict(user_input)[0]


    # =======================
    # Dropout Prediction
    # =======================

    dropout_risk = dropout_model.predict([[burnout_score]])[0]

    dropout_risk = np.clip(dropout_risk,0,1)

    dropout_percentage = round(dropout_risk*100,2)


    # =======================
    # Risk Level
    # =======================

    if burnout_score < 3.5:
        risk_level = "LOW"

    elif burnout_score < 7:
        risk_level = "MEDIUM"

    else:
        risk_level = "HIGH"


    return render_template(

        "index.html",

        burnout_score=round(burnout_score,2),

        dropout_risk=dropout_percentage,

        risk_level=risk_level

    )


# ==========================
# Themed error pages
# ==========================

@app.errorhandler(404)
def not_found(e):
    return render_template("error.html", code=404,
                            message="That page doesn't exist. Head back and try the assessment again."), 404


@app.errorhandler(500)
def server_error(e):
    return render_template("error.html", code=500,
                            message="Something went wrong while processing that request."), 500


# ==========================
# Run Flask
# ==========================

def open_browser():
    webbrowser.open_new("http://127.0.0.1:5000")


if __name__ == "__main__":
    # Only auto-open once (avoids opening twice due to the debug reloader)
    if os.environ.get("WERKZEUG_RUN_MAIN") != "true":
        Timer(1, open_browser).start()
    app.run(debug=True)
