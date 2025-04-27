# 🩺 Diabetes Prediction Web App

Welcome, traveler! ✨  
This is a simple yet powerful **Machine Learning tool** that predicts whether a patient may have **Diabetes** based on medical parameters.

Built with the elegance of **Support Vector Machine (SVM)** and the art of **Streamlit** for a smooth web experience.

---

## 🛠️ How It Works

> **"Where science meets intuition."**

1. **Input Fields:**
   - Pregnancies
   - Glucose Level
   - Blood Pressure
   - Skin Thickness
   - Insulin
   - Body Mass Index (BMI)
   - Diabetes Pedigree Function
   - Age

2. **Model in the Background:**
   - Your input is pre-processed using **StandardScaler** (for consistent scaling).
   - The trained **SVM model** then predicts:
     - **"Diabetes Detected"** or
     - **"No Diabetes Detected."**

3. **Outcome Display:**
   - A friendly message displays the prediction result.
   - Users can adjust values and predict again!

---

## 🎯 About the Model

- **Algorithm**: Support Vector Machine (SVM)
- **Scaler**: StandardScaler (ensures input feature scaling)
- **Accuracy Achieved**: ⭐ **82%** ⭐
- **Dataset Used**: Pima Indians Diabetes Dataset
- **Model Files:**
  - `model.pkl` (saved SVM model)
  - `scaler.pkl` (saved StandardScaler)

---

## 🌐 How to Run the Project

1. Clone or download this repository.
2. Install the required libraries:
   ```bash
   pip install streamlit scikit-learn pandas joblib
3. Launch the Streamlit  Web App:
   ```bash
   streamlit run app.py
4. Open your browser and interact with the Diabetes Prediction tool!
