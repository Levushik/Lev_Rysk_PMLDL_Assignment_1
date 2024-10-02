from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load the CatBoost model
model_path = '../../models/catboost_student_performance_model.pkl'
model = joblib.load(model_path)

# Initialize FastAPI app
app = FastAPI()

# Define the input data format
class StudentPerformanceInput(BaseModel):
    Hours_Studied: int
    Attendance: int
    Parental_Involvement: int
    Access_to_Resources: int
    Extracurricular_Activities: int
    Sleep_Hours: int
    Motivation_Level: int
    Internet_Access: int
    Tutoring_Sessions: int
    Family_Income: int
    Teacher_Quality: int
    School_Type: int
    Peer_Influence: int
    Physical_Activity: int
    Learning_Disabilities: int
    Parental_Education_Level: int
    Distance_from_Home: int
    Gender: int
    Exam_Score: int

# Define the prediction endpoint
@app.post("/predict")
def predict_performance(data: StudentPerformanceInput):
    input_data = np.array([[
        data.Hours_Studied, data.Attendance, data.Parental_Involvement, data.Access_to_Resources,
        data.Extracurricular_Activities, data.Sleep_Hours, data.Motivation_Level, data.Internet_Access,
        data.Tutoring_Sessions, data.Family_Income, data.Teacher_Quality, data.School_Type,
        data.Peer_Influence, data.Physical_Activity, data.Learning_Disabilities,
        data.Parental_Education_Level, data.Distance_from_Home, data.Gender, data.Exam_Score
    ]])

    prediction = model.predict(input_data)
    return {"predicted_score": prediction[0]}
