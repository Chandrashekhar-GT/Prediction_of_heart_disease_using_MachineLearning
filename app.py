
import streamlit as st
import pickle
import numpy as np
from sklearn.preprocessing import StandardScaler

# Load the trained model from the pickle file
with open('model2.pkl', 'rb') as file:
    model = pickle.load(file)
st.title("Prediction of Heart Disease")
st.image('heart.png',width=300)
# Define the input features
age = st.slider("Age", min_value=1, max_value=100, value=25, step=1)
sex = st.radio("Sex", options=["Male", "Female"])
if sex == "Male":
    sex = 1
else:
    sex = 0
cp = st.selectbox("Chest Pain Type", options=["Typical Angina", "Atypical Angina", "Non-anginal Pain", "Asymptomatic"])
if cp == "Typical Angina":
    cp = 1
elif cp == "Atypical Angina":
    cp = 2
elif cp == "Non-anginal Pain":
    cp = 3
else:
    cp = 4
trestbps = st.slider("Resting Blood Pressure (mm Hg)", min_value=50, max_value=200, value=120, step=1)
chol = st.slider("Cholesterol (mg/dl)", min_value=50, max_value=600, value=200, step=1)
fbs = st.radio("Fasting Blood Sugar > 120 mg/dl", options=["Yes", "No"])
if fbs == "Yes":
    fbs = 1
else:
    fbs = 0
restecg = st.selectbox("Resting Electrocardiographic Results", options=["Normal", "ST-T Wave Abnormality", "Left Ventricular Hypertrophy"])
if restecg == "Normal":
    restecg = 0
elif restecg == "ST-T Wave Abnormality":
    restecg = 1
else:
    restecg = 2
thalach = st.slider("Maximum Heart Rate Achieved", min_value=50, max_value=220, value=150, step=1)
exang = st.radio("Exercise Induced Angina", options=["Yes", "No"])
if exang == "Yes":
    exang = 1
else:
    exang = 0
oldpeak = st.slider("ST Depression Induced by Exercise Relative to Rest", min_value=0.0, max_value=10.0, value=0.0, step=0.1)
slope = st.selectbox("Slope of the Peak Exercise ST Segment", options=["Upsloping", "Flat", "Downsloping"])
if slope == "Upsloping":
    slope = 1
elif slope == "Flat":
    slope = 2
else:
    slope = 3
ca = st.selectbox("Number of Major Vessels Colored by Fluoroscopy", options=["0", "1", "2", "3"])
if ca == "0":
    ca = 0
elif ca == "1":
    ca = 1
elif ca == "2":
    ca = 2
else:
    ca = 3
thal = st.selectbox("Thalassemia", options=["Normal", "Fixed Defect", "Reversable Defect"])
if thal == "Normal":
    thal = 1
elif thal == "Fixed Defect":
    thal = 2
else:
    thal = 3

# Create a numpy array from the input features
s_scaler =StandardScaler()

input_data = np.array(s_scaler.fit_transform([[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])).reshape(1,-1)
    
 # Use the model to predict heart disease
prediction = model.predict(input_data)[0]
    

# Make the prediction when the user clicks the button
if st.button("Predict"):
  
     # Show the predicted output
    if prediction == 0:
        st.write("Congratulations! You do not have heart disease.")
    else:
        st.write("Sorry, you have heart disease. Please consult a doctor for further evaluation.")


