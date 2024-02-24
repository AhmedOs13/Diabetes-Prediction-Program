# Diabetes Prediction Program README
# Author: Ahmed Osama
# Affiliation: Biomedical Engineer @ Minia University
# Contact: ahmedosamaofficial13@gmail.com

# Title:
Diabetes Prediction Program

# Description:
This project implements a diabetes prediction program using logistic regression and batch gradient descent. The program takes input data related to various health parameters and predicts whether a person is diabetic, pre-diabetic, or not diabetic based on the provided features.

# Dataset Information:
- Dataset Source: [Diabetes Dataset](https://data.mendeley.com/datasets/wj9rwkp9c2/1)
- Citation: Rashid, Ahlam (2020), “Diabetes Dataset”, Mendeley Data, V1, doi: 10.17632/wj9rwkp9c2.1

# Algorithm:
- Logistic Regression
- Batch Gradient Descent

# Classification:
- N = Not Diabetic
- P = Pre-Diabetic
- Y = Diabetic

# Features:
- Number of Features: 10
- AGE, Urea, Cr, HbA1c, Chol, TG, HDL, LDL, VLDL, BMI

# Training Data:
- Number of Training Examples: 1000

# Prediction Accuracy:
- Achieved Prediction Accuracy: +80%

# Usage Instructions:
1. Run the provided Python script.
2. Input the required health parameters when prompted.
3. The program will predict the diabetic status of the input data.
4. Optionally, the program offers to plot a scatter plot indicating the relationship between BMI and Age, with the test point highlighted.

# Example Usage:
- Age: 40
- Urea (mg/dL): 60
- Cr (mL/min/BSA): 80
- HbA1c (%): 7
- Chol (mmol/L): 5.5
- TG (mmol/L): 2.2
- HDL (mmol/L): 1.2
- LDL (mmol/L): 3.5
- VLDL (mmol/L): 0.5
- BMI (Kg/m2): 28

# Output:
- "You are a Diabetic Patient"

# License:
None
