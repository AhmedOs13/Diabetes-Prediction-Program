# ------------------------------------------------------------------------------------------------------
# Copyright 2024 Ahmed Osama
# Biomedical Engineer @ Minia University
# Email: ahmedosamaofficial13@gmail.com
# ------------------------------------------------------------------------------------------------------
# Title: Diabetes Prediction Program
# Data: Imported From: https://data.mendeley.com/datasets/wj9rwkp9c2/1
# Citation: Rashid, Ahlam (2020), “Diabetes Dataset”, Mendeley Data, V1, doi: 10.17632/wj9rwkp9c2.1
# ------------------------------------------------------------------------------------------------------

import csv
import numpy as np
import matplotlib.pyplot as plt
import requests
from io import StringIO

def open_csv_file(url):
    # Status -> X , Result -> Y
    Stats = []
    Result = []

    # Open CSV file and import data
    response = requests.get(url)
    csv_data = response.text
    csv_reader = csv.reader(StringIO(csv_data))
    next(csv_reader)  # Skip Headers
    for row in csv_reader:
        stats_row = [1] + [float(z) for z in row[2:12]]
        Stats.append(stats_row)
        if row[12] == 'Y':  # Diabetic
            result_val = 1.0
        elif row[12] == 'P':  # Pre-Diabetic
            result_val = 0.5
        else:  # Not Diabetic
            result_val = 0.0
        # Add Result Value to Results list
        Result.append(result_val)

    # Convert lists into array
    return np.array(Stats), np.array(Result).reshape(-1, 1)


file_path = "https://raw.githubusercontent.com/AhmedOs13/Diabetes-Prediction-Program/main/Dataset.csv?raw=true"
x, y = open_csv_file(file_path)

# Determining Constants from CSV file
m_examples, n_features = x.shape

# Add Parameters Vector
theta = np.zeros((n_features, 1))

gamma = 0.001  # Learning Rate
iterations = 10000  # Iteration Number

# Gradient Descent Algorithm
for _ in range(iterations):
    func_h = np.dot(x, theta)
    func_g = 1 / (1 + np.exp(-func_h))
    gradient = np.dot(x.T, (func_g - y)) / m_examples
    theta -= gamma * gradient

# Model is Ready!

# Now try to input data and make model predict the result

AGE = float(input("Age: "))
Urea = float(input("Urea (mg/dL): "))
Cr = float(input("Cr (mL/min/BSA): "))
HbA1c = float(input("HbA1c (%): "))
Chol = float(input("Chol (mmol/L): "))
TG = float(input("TG (mmol/L): "))
HDL = float(input("HDL (mmol/L): "))
LDL = float(input("LDL (mmol/L): "))
VLDL = float(input("VLDL (mmol/L): "))
BMI = float(input("BMI (Kg/m2): "))

# X & Y matrix
test = np.array([1.0, AGE, Urea, Cr, HbA1c, Chol, TG, HDL, LDL, VLDL, BMI])
result = 1 / (1 + np.exp(-np.dot(test, theta)))

# Prediction according to test and result
if 0.75 <= result <= 0.9:
    print("You are a Pre-Diabetic Patient")
elif 0.9 < result <= 1.0:
    print("You are a Diabetic Patient")
else:
    print("You are NOT a Diabetic Patient")

# Plotting Option
plot = input("Do you want to Plot BMI-AGE Indication?(Yes/No): ")

if plot == "Yes" or "YES" or "yes":
    plt.scatter(x[:, 10], x[:, 2], c=y, cmap=plt.cm.coolwarm, edgecolors='k', label='Training Data')
    plt.scatter(BMI, AGE, c='red', marker='x', label='Test Point')
    plt.xlabel('BMI')
    plt.ylabel('AGE')
    plt.title('Plot between BMI and AGE')
    plt.colorbar(label='Class')
    plt.legend()
    plt.show()
