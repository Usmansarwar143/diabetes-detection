import streamlit as st
import joblib
import numpy as np

# --- Load Model and Scaler ---
model = joblib.load('model.pkl')
scaler = joblib.load('scalar.pkl')

# --- Page Configuration ---
st.set_page_config(page_title="Diabetes Prediction Tool", page_icon="🩺", layout="wide")

# --- Apply Custom CSS for background and styling ---
st.markdown("""
    <style>
        body {
            background-color: #f5f7fa;
        }
        .stApp {
            background-image: linear-gradient(to left, grey, black);
            padding: 10px;
            border-radius: 15px;
        }
        .big-font {
            font-size:22px !important;
            font-weight: bold;
        }
        .result {
            font-size:20px;
            font-weight:bold;
            color: #1f77b4;
        }
    </style>
""", unsafe_allow_html=True)

# --- Sidebar for navigation ---
with st.sidebar:
    st.title("TechnoHacks Diabetes Prediction Tool")
    st.markdown("Steps to use this tool:")
    st.markdown("- Fill out the **Patient Details**")
    st.markdown("- Click on **Predict**")
    st.markdown("- View your **Result** below!")
    st.markdown("---")
    st.info("🌟 Tip: Accurate input improves prediction quality!")

# --- Title and Introduction ---
st.markdown('<p class="big-font">🩺 Welcome to TechnoHacks Diabetes Prediction Tool</p>', unsafe_allow_html=True)
st.write("""
This intelligent tool helps you predict the risk of diabetes based on key health parameters.
Please fill in the details carefully, and let the magic unfold! ✨
""")

# --- Input Form ---
with st.form("prediction_form"):
    st.subheader("🔍 Enter Patient Details")

    col1, col2 = st.columns(2)
    with col1:
        pregnancies = st.number_input('🤰 Number of Pregnancies', min_value=0, max_value=20, value=0)
        glucose = st.number_input('🍬 Glucose Level', min_value=0, max_value=200, value=0)
        blood_pressure = st.number_input('🩸 Blood Pressure (mm Hg)', min_value=0, max_value=150, value=0)
        skin_thickness = st.number_input('📏 Skin Thickness (mm)', min_value=0, max_value=100, value=0)
    with col2:
        insulin = st.number_input('💉 Insulin Level (mu U/ml)', min_value=0, max_value=1000, value=0)
        bmi = st.number_input('⚖️ BMI (Body Mass Index)', min_value=0.0, max_value=50.0, value=0.0, step=0.1)
        diabetes_pedigree = st.number_input('🧬 Diabetes Pedigree Function', min_value=0.0, max_value=2.5, value=0.0, step=0.01)
        age = st.number_input('🎂 Age (years)', min_value=18, max_value=120, value=18)

    submit = st.form_submit_button("🔮 Predict Now")

# --- Prediction Logic ---
if submit:
    with st.spinner('🔄 Crunching numbers... please wait'):
        input_features = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, diabetes_pedigree, age]])
        scaled_features = scaler.transform(input_features)
        prediction = model.predict(scaled_features)[0]

    # --- Result Display ---
    st.markdown("---")
    st.subheader("🧾 Your Prediction Result")

    if prediction == 1:
        st.error("⚠️ **High Risk Detected!** The model predicts that the patient may have **Diabetes**.")
        st.markdown('<p class="result">⚠️ Please consult a healthcare professional for further evaluation.</p>', unsafe_allow_html=True)
    else:
        st.success("🎉 **Good News!** The model predicts that the patient is **not likely to have Diabetes.**")
        st.markdown('<p class="result">✅ Stay healthy and maintain a good lifestyle!</p>', unsafe_allow_html=True)

# --- Footer ---
st.markdown("""---""")
st.caption("Built with ❤️ By Muhammad Usman | Powered by TechnoHacks")