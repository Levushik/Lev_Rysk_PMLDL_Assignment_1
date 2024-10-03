import streamlit as st
import requests

# Define the API endpoint
API_URL = "http://api:8000/predict"

# Streamlit app UI
st.title("Student Performance Prediction")

st.write("This app predicts a student's performance based on several factors.")

# Define input fields for the model
hours_studied = st.slider("Hours Studied (1-24)", min_value=1, max_value=24, value=6)
attendance = st.slider("Attendance (%)", min_value=60, max_value=100, value=80)
parental_involvement = st.slider("Parental Involvement (0-100)", min_value=0, max_value=100, value=50)
access_to_resources = st.selectbox("Access to Resources", options=[0, 1], format_func=lambda x: "High" if x == 1 else "Low")
extracurricular_activities = st.selectbox("Extracurricular Activities", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
sleep_hours = st.slider("Sleep Hours (4-9)", min_value=4, max_value=9, value=7)
motivation_level = st.slider("Motivation Level (0-100)", min_value=0, max_value=100, value=70)
internet_access = st.selectbox("Internet Access", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
tutoring_sessions = st.slider("Tutoring Sessions (0-5)", min_value=0, max_value=5, value=1)
family_income = st.slider("Family Income (scaled 0-100)", min_value=0, max_value=100, value=50)
teacher_quality = st.slider("Teacher Quality (0-100)", min_value=0, max_value=100, value=75)
school_type = st.selectbox("School Type", options=[0, 1], format_func=lambda x: "Public" if x == 0 else "Private")
peer_influence = st.slider("Peer Influence (0-100)", min_value=0, max_value=100, value=50)
physical_activity = st.slider("Physical Activity Level (0-5)", min_value=0, max_value=5, value=2)
learning_disabilities = st.selectbox("Learning Disabilities", options=[0, 1], format_func=lambda x: "Yes" if x == 1 else "No")
parental_education_level = st.slider("Parental Education Level (0-100)", min_value=0, max_value=100, value=60)
distance_from_home = st.slider("Distance from Home (0-100)", min_value=0, max_value=100, value=30)
gender = st.selectbox("Gender", options=[0, 1], format_func=lambda x: "Male" if x == 0 else "Female")
exam_score = st.slider("Exam Score (55-85)", min_value=55, max_value=85, value=70)

# Prediction button
if st.button("Predict Performance"):
    # Prepare input data as a dictionary
    input_data = {
        "Hours_Studied": hours_studied,
        "Attendance": attendance,
        "Parental_Involvement": parental_involvement,
        "Access_to_Resources": access_to_resources,
        "Extracurricular_Activities": extracurricular_activities,
        "Sleep_Hours": sleep_hours,
        "Motivation_Level": motivation_level,
        "Internet_Access": internet_access,
        "Tutoring_Sessions": tutoring_sessions,
        "Family_Income": family_income,
        "Teacher_Quality": teacher_quality,
        "School_Type": school_type,
        "Peer_Influence": peer_influence,
        "Physical_Activity": physical_activity,
        "Learning_Disabilities": learning_disabilities,
        "Parental_Education_Level": parental_education_level,
        "Distance_from_Home": distance_from_home,
        "Gender": gender,
        "Exam_Score": exam_score
    }

    # Send POST request to FastAPI
    response = requests.post(API_URL, json=input_data)
    result = response.json()

    # Display prediction result
    st.success(f"Predicted Performance: {result['predicted_score']:.2f}")
