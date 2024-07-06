import warnings
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import mean_squared_error, r2_score

warnings.filterwarnings('ignore')
file_path = '/mnt/data/diabetes.csv'
diabetes_data = pd.read_csv('diabetes.csv')

X = diabetes_data.drop('Outcome', axis=1)
y = diabetes_data['Outcome']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

lr_model = LinearRegression()
lr_model.fit(X_train, y_train)

y_pred = lr_model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse}')
print(f'R-squared Score: {r2}')

def predict_diabetes(user_input):
    user_input_scaled = scaler.transform([user_input])
    prediction = lr_model.predict(user_input_scaled)
    return prediction[0]

def get_user_input_and_predict():
    pregnancies = int(input("Enter number of pregnancies: "))
    glucose = float(input("Enter glucose level: "))
    blood_pressure = float(input("Enter blood pressure: "))
    skin_thickness = float(input("Enter skin thickness: "))
    insulin = float(input("Enter insulin level: "))
    bmi = float(input("Enter BMI: "))
    diabetes_pedigree_function = float(input("Enter diabetes pedigree function: "))
    age = int(input("Enter age: "))

    user_input = [pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree_function, age]
    prediction = predict_diabetes(user_input)
    outcome = "has diabetes" if prediction >= 0.5 else "does not have diabetes"
    print(f'The model predicts that the person {outcome}')

get_user_input_and_predict()

