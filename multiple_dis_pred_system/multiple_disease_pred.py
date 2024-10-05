# -*- coding: utf-8 -*-
"""
Created on Tue May 14 23:37:34 2024


"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Load the saved models
diabetes_model = pickle.load(open('C:/Users/user/Desktop/Multiple_Disease/multiple_dis_pred_system/sav files/diabetes_model.sav', 'rb'))
heart_model = pickle.load(open('C:/Users/user/Desktop/Multiple_Disease/multiple_dis_pred_system/sav files/heart_model.sav', 'rb'))
parkinson_model = pickle.load(open('C:/Users/user/Desktop/Multiple_Disease/multiple_dis_pred_system/sav files/parkinson_model.sav', 'rb'))

st.markdown(
    """
    <style>
    .main {
        background-image: url('https://images.unsplash.com/photo-1516574187841-cb9cc2ca948b?w=500&auto=format&fit=crop&q=60&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxzZWFyY2h8M3x8dHJlYXRtZW50fGVufDB8fDB8fHww'); /* Replace with your medical-related background image URL */
        background-size: cover;
        background-position: center;
    }
    .stButton>button {
        background-color: #4CAF50; /* Green */
        border: none;
        color: white;
        padding: 15px 32px;
        text-align: center;
        text-decoration: none;
        display: inline-block;
        font-size: 16px;
        margin: 4px 2px;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    .stTextInput > div > input {
        background-color: #f0f0f0;
        color: #000;
        border-radius: 5px;
    }
    h1, h2, h3, h4, h5, h6 {
        color: #ffffff;
        text-shadow: 2px 2px 4px #000000;
        font-weight: bold;
    }
    p, label {
        color: #ffffff;
        font-weight: bold;
        text-shadow: 1px 1px 2px #000000;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# Sidebar for navigation
with st.sidebar:
    selected = option_menu(
        'Multiple Disease Prediction System',
        ['Diabetes Prediction', 'Heart Disease Prediction', 'Parkinson Prediction'],
        icons=['activity', 'heart', 'person'],
        default_index=0
    )

# Diabetes prediction page
if selected == "Diabetes Prediction":
    st.title('Diabetes Prediction using ML')
    
    # Getting the input data from the user
    cols1, cols2, cols3 = st.columns(3)
    
    with cols1:
        Pregnancies = st.number_input('Number of Pregnancies', min_value=0, max_value=20, step=1, format='%d')
        Glucose = st.number_input('Glucose Level', min_value=0, max_value=200, step=1, format='%d')
        BloodPressure = st.number_input('Blood Pressure', min_value=0, max_value=200, step=1, format='%d')
        
    with cols2:
        SkinThickness = st.number_input('Skin Thickness', min_value=0, max_value=100, step=1, format='%d')
        Insulin = st.number_input('Insulin Level', min_value=0, max_value=900, step=1, format='%d')
        BMI = st.number_input('BMI', min_value=0.0, max_value=70.0, step=0.1, format='%.1f')
        
    with cols3:
        DiabetesPedigreeFunction = st.number_input('Diabetes Pedigree Function', min_value=0.0, max_value=2.5, step=0.01, format='%.2f')
        Age = st.number_input('Age', min_value=0, max_value=120, step=1, format='%d')
        
    # Code for Prediction
    diab_diagnosis = ''
    
    # Creating a Button for Prediction
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        
        if diab_prediction[0] == 1:
            diab_diagnosis = '<p style="color:red; font-size: 20px;">The person is diabetic</p>'
        else:
            diab_diagnosis = '<p style="color:green; font-size: 20px;">The person is not diabetic</p>'
        
    st.markdown(diab_diagnosis, unsafe_allow_html=True)

# Heart disease prediction page
if selected == "Heart Disease Prediction":
    st.title('Heart Disease Prediction using ML')
    
    # Getting the input data from the user
    cols1, cols2, cols3 = st.columns(3)
    
    with cols1:
        Age = st.number_input("Age", min_value=0, max_value=120, step=1, format='%d')
        Sex = st.selectbox("Sex", options=[0, 1])  # Assuming 0 and 1 represent different sexes
        ChestPainType = st.number_input("Chest Pain Type", min_value=0, max_value=3, step=1, format='%d')
        
    with cols2:
        RestingBP = st.number_input("Resting Blood Pressure", min_value=0, max_value=300, step=1, format='%d')
        Cholesterol = st.number_input("Cholesterol", min_value=0, max_value=600, step=1, format='%d')
        FastingBS = st.selectbox("Fasting Blood Sugar > 120 mg/dl", options=[0, 1])
        
    with cols3:
       RestingECG = st.number_input("Resting ECG results", min_value=0, max_value=2, step=1, format='%d')
       MaxHR = st.number_input("Max Heart Rate", min_value=0, max_value=250, step=1, format='%d')
       ExerciseAngina = st.selectbox("Exercise Induced Angina", options=[0, 1])
        
        
    cols4, cols5 = st.columns(2)
    
    with cols4:
        Oldpeak = st.number_input("ST depression induced by exercise", min_value=0.0, max_value=10.0, step=0.1, format='%.1f')
        ST_Slope = st.number_input("Slope of the peak exercise ST segment", min_value=0, max_value=2, step=1, format='%d')
        
    with cols5:
        MajorVessels = st.number_input("Number of major vessels colored by fluoroscopy", min_value=0, max_value=4, step=1, format='%d')
        Thal = st.number_input("Thalassemia", min_value=0, max_value=3, step=1, format='%d')
    # Code for Prediction
    heart_diagnosis = ''
    
    # Creating a Button for Prediction
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_model.predict([[Age, Sex, ChestPainType, RestingBP, Cholesterol, FastingBS, RestingECG, MaxHR, ExerciseAngina, Oldpeak, ST_Slope, MajorVessels, Thal]])
        
        if heart_prediction[0] == 1:
            heart_diagnosis = '<p style="color:red; font-size: 20px;">The person has heart disease</p>'
        else:
            heart_diagnosis = '<p style="color:green; font-size: 20px;">The person does not have heart disease</p>'
        
    st.markdown(heart_diagnosis, unsafe_allow_html=True)

# Parkinson's disease prediction page
if selected == "Parkinson Prediction":
    st.title('Parkinson Prediction using ML')
    
    # Getting the input data from the user
    cols1, cols2, cols3 = st.columns(3)
    
    with cols1:
        MDVP_Fo_Hz = st.number_input('MDVP: Fundamental Frequency (Fo) in Hz', min_value=0.0, max_value=300.0, step=0.1, format='%.1f')
        MDVP_Fhi_Hz = st.number_input('MDVP: Maximum Fundamental Frequency (Fhi) in Hz', min_value=0.0, max_value=600.0, step=0.1, format='%.1f')
        MDVP_Flo_Hz = st.number_input('MDVP: Minimum Fundamental Frequency (Flo) in Hz', min_value=0.0, max_value=600.0, step=0.1, format='%.1f')
        
    with cols2:
        MDVP_Jitter_percent = st.number_input('MDVP: Jitter (%)', min_value=0.0, max_value=1.0, step=0.01, format='%.2f')
        MDVP_Jitter_Abs = st.number_input('MDVP: Jitter (Abs)', min_value=0.0, max_value=0.1, step=0.001, format='%.3f')
        MDVP_RAP = st.number_input('MDVP: Relative Amplitude Perturbation (RAP)', min_value=0.0, max_value=0.1, step=0.001, format='%.3f')
        
    with cols3:
        MDVP_PPQ = st.number_input('MDVP: Five-Point Period Perturbation Quotient (PPQ)', min_value=0.0, max_value=0.1, step=0.001, format='%.3f')
        Jitter_DDP = st.number_input('Jitter: Detrended Period Perturbation Quotient (DDP)', min_value=0.0, max_value=0.1, step=0.001, format='%.3f')
        MDVP_Shimmer = st.number_input('MDVP: Shimmer', min_value=0.0, max_value=1.0, step=0.01, format='%.2f')
       
        
    cols4, cols5 = st.columns(2)
    
    with cols4:
        Shimmer_APQ3 = st.number_input('Shimmer: Three-Point Amplitude Perturbation Quotient (APQ3)', min_value=0.0, max_value=1.0, step=0.01, format='%.2f')
        Shimmer_APQ5 = st.number_input('Shimmer: Five-Point Amplitude Perturbation Quotient (APQ5)', min_value=0.0, max_value=1.0, step=0.01, format='%.2f')
        MDVP_APQ = st.number_input('MDVP: Amplitude Perturbation Quotient (APQ)', min_value=0.0, max_value=1.0, step=0.01, format='%.2f')
        
    with cols5:
        Shimmer_DDA = st.number_input('Shimmer: Detrended Amplitude Perturbation Quotient (DDA)', min_value=0.0, max_value=1.0, step=0.01, format='%.2f')
        NHR = st.number_input('Noise-to-Harmonics Ratio (NHR)', min_value=0.0, max_value=1.0, step=0.01, format='%.2f')
        HNR = st.number_input('Harmonics-to-Noise Ratio (HNR)', min_value=0.0, max_value=100.0, step=0.1, format='%.1f')
        
    cols6, cols7 = st.columns(2)
    
    with cols6:
        RPDE = st.number_input('Recurrence Period Density Entropy (RPDE)', min_value=0.0, max_value=1.0, step=0.01, format='%.2f')
        DFA = st.number_input('Detrended Fluctuation Analysis (DFA)', min_value=0.0, max_value=2.0, step=0.01, format='%.2f')
        MDVP_Shimmer_dB = st.number_input('MDVP: Shimmer in dB', min_value=0.0, max_value=10.0, step=0.1, format='%.1f')
        
    with cols7:
        spread1 = st.number_input('Spread1', min_value=-10.0, max_value=10.0, step=0.1, format='%.2f')
        spread2 = st.number_input('Spread2', min_value=-10.0, max_value=10.0, step=0.1, format='%.2f')
        D2 = st.number_input('D2', min_value=0.0, max_value=5.0, step=0.01, format='%.2f')
        PPE = st.number_input('Pitch Period Entropy (PPE)', min_value=0.0, max_value=1.0, step=0.01, format='%.2f')
    
    # Code for Prediction
    parkinson_diagnosis = ''
    
    # Creating a Button for Prediction
    if st.button('Parkinson Test Result'):
        parkinson_prediction = parkinson_model.predict([[MDVP_Fo_Hz, MDVP_Fhi_Hz, MDVP_Flo_Hz, MDVP_Jitter_percent, MDVP_Jitter_Abs, MDVP_RAP, MDVP_PPQ, Jitter_DDP, MDVP_Shimmer, MDVP_Shimmer_dB, Shimmer_APQ3, Shimmer_APQ5, MDVP_APQ, Shimmer_DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
        
        if parkinson_prediction[0] == 1:
            parkinson_diagnosis = '<p style="color:red; font-size: 20px;">The person has Parkinson\'s disease</p>'
        else:
            parkinson_diagnosis = '<p style="color:green; font-size: 20px;">The person does not have Parkinson\'s disease</p>'
        
    st.markdown(parkinson_diagnosis, unsafe_allow_html=True)
