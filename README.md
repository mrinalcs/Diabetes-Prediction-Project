# Diabetes-Prediction-Project

Predict diabetes using the Pima Indians Diabetes Dataset. The dataset contains medical records of female patients, including features like Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age, and the target variable Outcome (0 for non-diabetic, 1 for diabetic). The objective is to predict diabetes risk.

## Objectives
- Perform exploratory data analysis distributions and relationships
- Preprocess the data
- Train Logistic Regression
- Create a reproducible pipeline and save the model for deployment
---
  
### Steps:
1. Data loading and preprocessing
2. Feature selection and visualization
3. Data standardization
4. Train-test split
5. Model training
6. Model evaluation
7. Feature importance visualization
8. Deploy the model

## Model Summary
```
Accuracy: 0.8246753246753247

Confusion Matrix:
[[98  9]
 [18 29]]

Classification Report:
              precision    recall  f1-score   support

           0       0.84      0.92      0.88       107
           1       0.76      0.62      0.68        47

    accuracy                           0.82       154
   macro avg       0.80      0.77      0.78       154
weighted avg       0.82      0.82      0.82       154

```
### Feature Importance:

| Feature              | Coefficient | Effect    |
|----------------------|-------------|-----------|
| Glucose              | +1.0655     | Positive  |
| BMI                  | +0.6818     | Positive  |
| Diabetes Pedigree    | +0.2857     | Positive  |
| Age                  | +0.2621     | Positive  |
| Pregnancies          | +0.1324     | Positive  |
| Insulin              | -0.1979     | Negative  |
| Skin Thickness       | -0.2912     | Negative  |
| Blood Pressure       | -0.3581     | Negative  |

 
## 🚀 Deployment
 

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mrinalcs/Diabetes-Prediction-Project/blob/main/notebook.ipynb)   

[![View on GitHub](https://img.shields.io/badge/GitHub-View%20Notebook-black?logo=github)](https://github.com/mrinalcs/Diabetes-Prediction-Project/blob/main/notebook.ipynb) 

**Live App:** [Diabetes Prediction App (Streamlit)](https://diabetes-prediction-project-mrinalcs.streamlit.app/)
 [![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_white.svg)](https://diabetes-prediction-project-mrinalcs.streamlit.app/)

