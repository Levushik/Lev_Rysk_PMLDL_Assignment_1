import streamlit as st
import requests

# Define the API endpoint
API_URL = "http://api:8000/predict"

# Streamlit app UI
st.title("Student Performance Prediction")

# Define input fields for the model
hours_studied = st.number_input("Hours Studied", min_value=0, max_value=24, step=1)
attendance = st.number_input("Attendance", min_value=0, max_value=100, step=1)
parental_involvement = st.number_input("Parental Involvement", min_value=0, max_value=100, step=1)
access_to_resources = st.number_input("Access to Resources", min_value=0, max_value=100, step=1)
extracurricular_activities = st.number_input("Extracurricular Activities", min_value=0, max_value=100, step=1)
sleep_hours = st.number_input("Sleep Hours", min_value=0, max_value=24, step=1)
motivation_level = st.number_input("Motivation Level", min_value=0, max_value=100, step=1)
internet_access = st.number_input("Internet Access", min_value=0, max_value=100, step=1)
tutoring_sessions = st.number_input("Tutoring Sessions", min_value=0, max_value=100, step=1)
family_income = st.number_input("Family Income", min_value=0, max_value=100, step=1)
teacher_quality = st.number_input("Teacher Quality", min_value=0, max_value=100, step=1)
school_type = st.number_input("School Type", min_value=0, max_value=1, step=1)
peer_influence = st.number_input("Peer Influence", min_value=0, max_value=100, step=1)
physical_activity = st.number_input("Physical Activity", min_value=0, max_value=100, step=1)
learning_disabilities = st.number_input("Learning Disabilities", min_value=0, max_value=1, step=1)
parental_education_level = st.number_input("Parental Education Level", min_value=0, max_value=100, step=1)
distance_from_home = st.number_input("Distance from Home", min_value=0, max_value=100, step=1)
gender = st.number_input("Gender", min_value=0, max_value=1, step=1)
exam_score = st.number_input("Exam Score", min_value=0, max_value=100, step=1)

# Prediction button
if st.button("Predict Performance"):
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
    st.success(f"Predicted Performance: {result['predicted_score']}")
