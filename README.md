# 🩺 Diabetes Prediction with Linear Regression

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.0%2B-orange?logo=scikit-learn)
![Status](https://img.shields.io/badge/status-Completed-brightgreen)

> Predicts the likelihood of diabetes using a **Linear Regression** model on the Pima Indians Diabetes dataset.

---

## ✨ Features

- 🔍 Loads and scales data using `StandardScaler`
- 📊 Splits data into training and testing sets
- 📈 Trains a **Linear Regression** model
- ✅ Evaluates model performance (Mean Squared Error & R² score)
- 🧪 Allows interactive prediction from user input

---

## 📦 Requirements

- Python 3.8+
- pandas
- scikit-learn

Install dependencies:
```bash
pip install pandas scikit-learn
```

## 📁 Dataset
Uses ```diabetes.csv```

### Contains features like:

- Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age

- **Target:** Outcome (1 = has diabetes, 0 = does not have diabetes)

## ▶️ How to Run
1. Place diabetes.csv in the same folder.

2. Run the script:
   ```bash
   python main.py

3. Enter values interactively when prompted:
   ```bash
   Enter number of pregnancies: 2
   Enter glucose level: 120
   Enter blood pressure: 70
   Enter skin thickness: 20
   Enter insulin level: 79
   Enter BMI: 24.5
   Enter diabetes pedigree function: 0.5
   Enter age: 30
   The model predicts that the person does not have diabetes
   ```
## ✅ Example Output
   ```bash
Mean Squared Error: 0.173
R-squared Score: 0.27
```
Note: R² may be low because Linear Regression is not ideal for binary classification.

## 🧠 How It Works
- Scales features for better model performance

- Fits Linear Regression to predict probabilities

- Predicts: if predicted value ≥ 0.5 → person has diabetes, else → does not have diabetes

## ✏️ Author

Built and documented by [nandhini1424]("https://github.com/nandhini1424")


