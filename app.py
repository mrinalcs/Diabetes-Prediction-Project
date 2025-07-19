# app.py
import streamlit as st
import numpy as np
import joblib
import matplotlib.pyplot as plt 
model = joblib.load('diabetes_pipeline.pkl')

# Page setup
st.set_page_config(page_title="🩺 Diabetes Predictor", layout="centered")
st.title("🩺 Diabetes Risk Predictor")




# Sidebar
st.sidebar.header("📌 About This App")
st.sidebar.markdown("""
This app uses a **logistic regression model** to predict the likelihood of diabetes.

👨‍⚕️ **Note**: This is not a medical diagnosis tool. Always consult a healthcare professional.

""")
st.sidebar.markdown("---")
 
input_mode = st.sidebar.radio("Input Method", ["Manual Input", "Slider"], index=1)


st.sidebar.markdown("---")
st.sidebar.markdown(
    "🔗 [View Project on GitHub](https://github.com/mrinalcs/Diabetes-Prediction-Project)",
    unsafe_allow_html=True
)

#  Inputs
def input_field(label, default, minval, maxval, step, help_text, key):
    if input_mode == "Manual Input":
        return st.number_input(label, min_value=minval, max_value=maxval, value=default,
                               step=step, help=help_text, key=key)
    else:
        return st.slider(label, min_value=minval, max_value=maxval, value=default,
                         step=step, help=help_text, key=key)

# form inputs
st.markdown("### 📋 Enter Patient Medical Information")
col1, col2 = st.columns(2)

with col1:
    pregnancies = input_field("Pregnancies", 1, 0, 20, 1, "Number of times pregnant", "preg")
    glucose = input_field("Glucose Level", 100, 0, 200, 1, "Plasma glucose concentration", "gluc")
    skin_thickness = input_field("Skin Thickness (mm)", 20, 0, 100, 1, "Triceps skin fold thickness", "skin")
    bmi = input_field("BMI", 25.0, 0.0, 70.0, 0.1, "Body Mass Index", "bmi")

with col2:
    blood_pressure = input_field("Blood Pressure (mm Hg)", 70, 0, 140, 1, "Diastolic blood pressure", "bp")
    insulin = input_field("Insulin (mu U/ml)", 80, 0, 900, 1, "2-hour serum insulin", "ins")
    dpf = input_field("Diabetes Pedigree Function", 0.5, 0.0, 3.0, 0.01, "Genetic risk factor", "dpf")
    age = input_field("Age", 30, 10, 100, 1, "Age in years", "age")

# --- Prediction ---
if st.button("🔍 Predict"):
    input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness,
                            insulin, bmi, dpf, age]])
    
    prediction = model.predict(input_data)[0]
    probabilities = model.predict_proba(input_data)[0]

    st.subheader("📊 Prediction Result")
    if prediction == 1:
        st.error("🛑 Likely Diabetic")
        st.markdown("Please consult a healthcare professional.")
    else:
        st.success("✅ Not Diabetic")
        st.markdown("Keep maintaining a healthy lifestyle!")

    # Confidence chart
    st.subheader("📈 Prediction Confidence")
    fig, ax = plt.subplots(figsize=(4, 2))
    ax.bar(["Not Diabetic", "Diabetic"], probabilities, color=["green", "red"])
    ax.set_ylim(0, 1)
    ax.set_ylabel("Probability")
    st.pyplot(fig)

    st.write(f"🔵 **Not Diabetic**: `{probabilities[0]:.2%}`")
    st.write(f"🔴 **Diabetic**: `{probabilities[1]:.2%}`")




