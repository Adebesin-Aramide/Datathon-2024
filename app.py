import streamlit as st
import numpy as np
import joblib

# Load the trained model and the scaler
try:
    model = joblib.load('logistic_model.pkl')
    scaler = joblib.load('scaler.pkl')  # Ensure you have saved the scaler used during training
except FileNotFoundError:
    st.error("Model or scaler file not found. Please upload the necessary files.")

# Title and description of the app
st.title("Will the Student Pass? - Exam Performance Prediction")
st.write("""
This app predicts whether a student will pass or fail based on input features such as age, attendance rate, study hours, and more.
""")

# Sidebar for input features
st.sidebar.header("Input Features")

# Function to encode user input for model prediction
def encode_input(age, grade_level, attendance_rate, study_hours, quiet_study_space, internet_access, 
                 guardian_engagement, library_usage, teacher_support_hours, teacher_availability, 
                 extracurricular_impact, tutoring_support, average_score):
    
    # Encode the categorical features based on your encoding schema
    grade_level_dict = {"SSS1": 2, "SSS 2": 0, "SSS 3": 1}
    internet_access_dict = {"No internet": 0, "Reliable": 1, "Unreliable": 2}
    guardian_engagement_dict = {"Monthly": 1, "Weekly": 4, "Rarely": 3, "Daily": 0, "Never": 2}
    library_usage_dict = {"Rarely": 3, "Daily": 0, "Weekly": 4, "Monthly": 1, "Never": 2}
    teacher_availability_dict = {"Adequate": 0, "Inadequate": 1, "Somewhat adequate": 2}
    extracurricular_impact_dict = {"Agree": 0, "Strongly disagree": 4, "Disagree": 3, "Neutral": 2, "Strongly agree": 1}
    quiet_study_space_dict = {"Yes": 1, "No": 0}
    tutoring_support_dict = {"Yes": 1, "No": 0}

    # Encoding categorical inputs
    grade_level_encoded = grade_level_dict.get(grade_level, 0)
    internet_access_encoded = internet_access_dict.get(internet_access, 0)
    guardian_engagement_encoded = guardian_engagement_dict.get(guardian_engagement, 0)
    library_usage_encoded = library_usage_dict.get(library_usage, 0)
    teacher_availability_encoded = teacher_availability_dict.get(teacher_availability, 0)
    extracurricular_impact_encoded = extracurricular_impact_dict.get(extracurricular_impact, 0)
    quiet_study_space_encoded = quiet_study_space_dict.get(quiet_study_space, 0)
    tutoring_support_encoded = tutoring_support_dict.get(tutoring_support, 0)

    # Create a numpy array with the encoded features for prediction
    input_data = np.array([[age, grade_level_encoded, attendance_rate, study_hours, quiet_study_space_encoded,
                            internet_access_encoded, guardian_engagement_encoded, library_usage_encoded, 
                            teacher_support_hours, teacher_availability_encoded, extracurricular_impact_encoded,
                            tutoring_support_encoded, average_score]])
    
    return input_data

# User input features
def user_input_features():
    age = st.sidebar.slider('Age', 10, 15, 12)
    grade_level = st.sidebar.selectbox('Grade Level', ('SSS1', 'SSS 2', 'SSS 3'))
    attendance_rate = st.sidebar.slider('Attendance Rate (%)', 0, 100, 75)
    study_hours = st.sidebar.slider('Study Hours per Week', 0, 100, 75)
    quiet_study_space = st.sidebar.selectbox('Quiet Study Space', ('Yes', 'No'))
    internet_access = st.sidebar.selectbox('Internet Access', ('No internet', 'Reliable', 'Unreliable'))
    guardian_engagement = st.sidebar.selectbox('Guardian Engagement', ('Daily', 'Weekly', 'Monthly', 'Rarely', 'Never'))
    library_usage = st.sidebar.selectbox('Library Usage', ('Rarely', 'Daily', 'Weekly', 'Monthly', 'Never'))
    teacher_support_hours = st.sidebar.slider('Teacher Support Hours', 0, 50, 8)
    teacher_availability = st.sidebar.selectbox('Teacher Availability', ('Adequate','Inadequate', 'Somewhat adequate'))
    extracurricular_impact = st.sidebar.selectbox('Extracurricular Impact', ('Agree', 'Strongly disagree', 'Disagree', 'Neutral', 'Strongly agree'))
    tutoring_support = st.sidebar.selectbox('Tutoring Support', ('Yes', 'No'))
    average_score = st.sidebar.slider('Average Score', 0.0, 100.0, 70.0)
    
    return age, grade_level, attendance_rate, study_hours, quiet_study_space, internet_access, \
           guardian_engagement, library_usage, teacher_support_hours, teacher_availability, \
           extracurricular_impact, tutoring_support, average_score

# Get user input
inputs = user_input_features()

# Encode the input features
encoded_input = encode_input(*inputs)

# Scale the input features using the loaded scaler
scaled_input = scaler.transform(encoded_input)

# Model prediction
if st.button('Predict'):
    prediction = model.predict(scaled_input)
    prediction_proba = model.predict_proba(scaled_input)[0][1]  # Probability of passing
    
    # Display the prediction
    if prediction == 1:
        st.success(f"The model predicts that the student will pass.")
    else:
        st.error(f"The model predicts that the student will fail.")