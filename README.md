**Students Performance Prediction App**

**Overview**

The Students Performance Prediction App is a machine learning-based web application designed to predict whether a student will pass or fail their final exams. It leverages a variety of academic, social, and environmental features to make predictions and provide actionable insights. The app is built using Streamlit, and the machine learning model is trained using Logistic Regression after extensive feature engineering and data analysis.

The app offers educators, students, and administrators a powerful tool to identify students who may need additional support, enabling timely intervention to improve overall academic performance.

`*Try it here:* https://students-performance-predictions.streamlit.app/`

**Features**

Predicts whether a student will pass or fail based on input features.

Allows users to input various academic and socio-economic data, such as study habits, guardian engagement, and internet access.

Provides real-time predictions with a clear indication of the probability of passing.

Built using Streamlit for an easy-to-use interface and deployed on Streamlit Cloud.

**Table of Contents**
- Project Structure
- Installation
- Usage
- Process
  - Data Collection
  - Data Preparation
  - Data Analysis
  - Data Preprocessing
  - Feature Engineering
  - Model Building
  - Evaluation
  - Deployment

The project repository includes the following files:


`my-streamlit-app/`
`│`
`├── app.py                        # Main Streamlit app script `
`├── plot_folder                   # the plots generated are stored`
`├── Datafest - Sheet1.csv         # the data collected via a digital questionaire`
`├── student.ipynb                 # Jupyter notebook for data analysis and model building`
`├── logistic_model.pkl            # Trained Logistic Regression model`
`├── scaler.pkl                    # Scaler used for feature scaling`
`├── requirements.txt              # Python dependencies`
`└── README.md                     # Project documentation`

**Installation**

To run the project locally, follow these steps:

Clone the repository:

`git clone https://github.com/Adebesin-Aramide/Datathon-2024.git`
`cd Datathon-2024`

**Install the dependencies:**

`pip install -r requirements.txt`

**Usage**

*Run the app locally:*

After installing the dependencies, run the following command to start the Streamlit app locally:

`streamlit run app.py`
This will open the app in your default browser.

**App Interface:**

Input features such as age, grade level, attendance rate, study hours, and other factors into the sidebar.
Click the "Predict" button to see whether the student will pass or fail the exam, along with the probability of passing.


**PROCESS**

1. **Data Collection**

Data was collected through a digital questionnaire that gathered information on student demographics, study habits, internet access, guardian engagement, and academic performance. This comprehensive dataset formed the foundation for the predictive model.
More contribution can still be made.
Fill this link if you're a secondary school student in Africa. 
`https://docs.google.com/forms/d/e/1FAIpQLScGMcEnTsgEVaVIGTraMjqO7M-annqRdJRI2DYeuUiOW29Gvg/viewform`

*Key features:*

Age
Study Hours per Week
Guardian Engagement
Internet Access
Library Usage
Average Academic Scores ....

2. **Data Preparation**

Once the data was collected, it was cleaned and organized to ensure consistency. Missing values were handled, especially for students who didn’t offer all subjects.

3. **Data Analysis**

Exploratory data analysis (EDA) was performed to understand the relationships between features. The key focus was on visualizing distributions, such as:

The correlation between Study Hours and Average Score.
The impact of Guardian Engagement on student performance.
The plot can be viewed in the plot_folder

4. **Data Preprocessing**

The data was preprocessed to be suitable for machine learning algorithms. The following steps were applied:
*Scaling:* Numerical features were scaled using StandardScaler to ensure uniformity.
*Encoding: *Categorical features were encoded into numerical representations (e.g., Yes/No -> 1/0).
*Train-Test Split:* The dataset was split into training and testing sets for proper evaluation of model performance.

5. **Feature Engineering**

During feature engineering, additional features were derived to improve model performance:

*Average Score*: An aggregate score was calculated by averaging the subject scores.
*Target Variable (Pass/Fail):* The target was created by setting a threshold at 50, where an average score below 50 was marked as "Fail", and above or equal to 50 was marked as "Pass."

6. **Model Building**

Several machine learning algorithms were evaluated, but Logistic Regression was chosen due to its performance and simplicity. Hyperparameter tuning was applied to optimize the model's predictive power. Other models like Decision Trees and Random Forests were tested for comparison.
Outcome: A well-tuned Logistic Regression model capable of predicting student performance accurately.

7. Evaluation
The model was evaluated using key performance metrics:

Accuracy: 92%
F1 Score: 94%
Cross-validation was employed to ensure the model generalizes well across different data splits.
F1 score was the key metrics used because the dataset has its target variable to be imbalanced

8. **Deployment**
The app was deployed using Streamlit Cloud to provide real-time predictions. Educators, administrators, and students can use the app to input key features and get predictions on student performance.
