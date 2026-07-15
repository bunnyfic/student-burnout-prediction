# student-burnout-prediction-system
live demo : https://student-burnout-prediction-kuvl.onrender.com/

> An AI-powered web application that predicts a student's **Burnout Score**, estimates **Dropout Risk**, and classifies the student's **Risk Level** using Machine Learning.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?logo=python">
  <img src="https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask">
  <img src="https://img.shields.io/badge/CatBoost-Regressor-orange">
  <img src="https://img.shields.io/badge/Scikit--Learn-ML-yellow?logo=scikitlearn">
  <img src="https://img.shields.io/badge/License-MIT-green">
</p>

---

## 📖 Overview

Student burnout has become an increasingly important issue in modern education. This project uses **Machine Learning** to predict a student's burnout score based on academic, psychological, and lifestyle factors.

The application also estimates the student's dropout risk using a mathematical regression model and classifies the overall burnout level into Low, Medium, or High.

the dataset i used is from kagle which had over 20 features and 1000000 records.
---

## ✨ Features

- 📊 Predicts **Student Burnout Score**
- 🎯 Estimates **Dropout Risk**
- 🚦 Classifies **Risk Level**
- 🧠 Powered by **CatBoost Regressor**
- 🌐 Interactive Flask Web Application
- 🎚️ User-friendly slider interface
- 📈 Feature Importance Analysis
- 💾 Trained model saved using Joblib

---

## 🛠 Tech Stack

### Machine Learning
- CatBoost Regressor
- Scikit-Learn
- Pandas
- NumPy

### Backend
- Flask
- Joblib

### Frontend
- HTML5
- CSS3
- JavaScript

### Deployment
- Render

---

## 📂 Project Structure

```text
student-burnout-prediction/
│
├── app.py
├── burnout_model.pkl
├── dropout_model.pkl
├── requirements.txt
├── Procfile
├── runtime.txt
│
├── templates/
│   ├── index.html
│   └── error.html
│
│
└── README.md
```

---

## 📊 Input Features

The model predicts burnout using the following features:

- Study Hours Per Day
- Exam Pressure
- Stress Level
- Anxiety Score
- Depression Score
- Sleep Hours
- Physical Activity
- Social Support
- Financial Stress
- Family Expectation
- Mental Health Index

---

## 🎯 Output

The application returns:

- Burnout Score
- Dropout Risk (%)
- Risk Level
  - 🟢 Low
  - 🟡 Medium
  - 🔴 High

---

## 🤖 Machine Learning Model

Several regression algorithms were evaluated before selecting the final model.

| Model | R² Score |
|--------|----------|
| **CatBoost** | **0.7406** ✅ |
| LightGBM | 0.7388 |
| XGBoost | 0.7379 |
| Random Forest | 0.7283 |

### Final Model

**CatBoost Regressor**

Performance Metrics

- **R² Score:** 0.7406
- **MAE:** 0.6382
- **RMSE:** 0.8426

---

## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/yourusername/student-burnout-prediction.git

cd student-burnout-prediction
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the application

```bash
python app.py
```

Open

```
http://127.0.0.1:5000
```

---

## 📸 Screenshots

### Home Page
<img width="1094" height="561" alt="image" src="https://github.com/user-attachments/assets/bdacc2ec-29fc-46e3-82ac-cfcc03e80f79" />

### Prediction Result
<img width="942" height="393" alt="image" src="https://github.com/user-attachments/assets/69814e30-2b91-4191-b32f-4c35d1389a30" />

## 👩‍💻 Author

**Maya**
M.Sc. Data Science

---

## ⭐ If you like this project

Please consider giving it a ⭐ on GitHub.
