# Heart Disease Prediction Web Application

![WebApp](WebApp.jpg)

## Overview

In this machine learning project, I have collected the dataset from Kaggle ([Heart Disease UCI Dataset](https://www.kaggle.com/ronitf/heart-disease-uci)) and I will be using Machine Learning to predict whether any person is suffering from heart disease.

## Web Application Interface

The web application provides a user-friendly interface where users can input patient details through various input fields. After filling out the details, users can click the "Predict" button to trigger the prediction process. The application then displays a prediction indicating whether the patient is likely to have heart disease or not.

## Machine Learning Model

The machine learning model used in this project is a K-Nearest Neighbors (KNN) classifier. The model was trained on a Kaggle dataset containing various features related to heart health. The accuracy of the model was evaluated using cross-validation and achieved an accuracy of approximately 85%.

## Project Structure

The project is organized as follows:

- `index.html`: The HTML file containing the user interface for the web application.
- `app.py`: The Flask web application script responsible for serving the HTML, handling form submissions, and making predictions using the trained model.
- `model.pkl`: The serialized KNN model saved as a binary file.
- `WebApp.jpg`: A screenshot of the web application's user interface.

## Usage

1. Install the required Python packages using `pip install -r requirements.txt`.
2. Run the Flask application using `python app.py`.
3. Access the web application by navigating to `http://localhost:5000` in your web browser.
4. Fill out the patient details in the input fields.
5. Click the "Predict" button to receive the heart disease prediction.

## Screenshots

### Model Evaluation

![Random Forest Accuracy](RF.jpg)

*Figure 1: Random Forest Accuracy*

This image shows the accuracy achieved by the Random Forest algorithm during the model evaluation process. It demonstrates the model's performance on the heart disease prediction task.

![K-Nearest Neighbors (KNN) Accuracy](knn.jpg)

*Figure 2: K-Nearest Neighbors (KNN) Accuracy*

This image presents the accuracy achieved by the K-Nearest Neighbors (KNN) algorithm, which was chosen as the final model for the web application. It showcases the model's effectiveness in predicting heart disease.

## Acknowledgments

- Kaggle (Dataset source)
- Scikit-learn (Machine learning library)
- Flask (Web framework)

---

### Explanation of Input Fields

Here, we provide more detailed explanations for each input field, including where you can typically obtain this information:

1. **Gender (Sex):**
   - This field represents the gender of the individual.
   - "Female" (Select if the individual is female)
   - "Male" (Select if the individual is male)
   - This information is collected during a patient's medical history intake at healthcare facilities.

2. **Chest Pain Type (cp):**
   - This field relates to the type of chest pain experienced by the individual.
   - "Type 0" (Typical angina): Typically assessed during a medical evaluation.
   - "Type 1" (Atypical angina): Typically assessed during a medical evaluation.
   - "Type 2" (Non-anginal pain): Typically assessed during a medical evaluation.
   - "Type 3" (Asymptomatic): Typically assessed during a medical evaluation.

3. **Fasting Blood Sugar (fbs):**
   - This field indicates the fasting blood sugar level of the individual.
   - "Lower than 120 mg/dL" (Normal fasting blood sugar): Determined through blood tests in healthcare settings.
   - "Higher than 120 mg/dL" (Elevated fasting blood sugar): Determined through blood tests in healthcare settings.

4. **Resting ECG Results (restecg):**
   - This field represents the resting electrocardiographic results.
   - "Normal" (A normal resting ECG): Obtained through an electrocardiogram test conducted at healthcare facilities.
   - "Abnormality 1" (An abnormal resting ECG result): Obtained through an electrocardiogram test conducted at healthcare facilities.
   - "Abnormality 2" (Another type of abnormal resting ECG result): Obtained through an electrocardiogram test conducted at healthcare facilities.

5. **Exercise-Induced Angina (exang):**
   - This field indicates whether the individual experiences exercise-induced angina (chest pain).
   - "No" (No chest pain during exercise): Assessed during a stress test conducted at healthcare facilities.
   - "Yes" (Experiences chest pain during exercise): Assessed during a stress test conducted at healthcare facilities.

6. **Slope of Peak Exercise ST Segment (slope):**
   - This field relates to the slope of the peak exercise ST segment on an electrocardiogram during exercise.
   - "Slope 0" (A specific type of slope): Assessed during exercise stress tests conducted at healthcare facilities.
   - "Slope 1" (Another type of slope): Assessed during exercise stress tests conducted at healthcare facilities.
   - "Slope 2" (Yet another type of slope): Assessed during exercise stress tests conducted at healthcare facilities.

7. **Number of Major Vessels (ca):**
   - This field represents the number of major blood vessels colored by fluoroscopy.
   - "0" (No major vessels colored): Determined through medical imaging tests such as angiography.
   - "1" (One major vessel colored): Determined through medical imaging tests such as angiography.
   - "2" (Two major vessels colored): Determined through medical imaging tests such as angiography.
   - "3" (Three major vessels colored): Determined through medical imaging tests such as angiography.

8. **Thallium Stress Testing (thal):**
   - This field relates to the thallium stress testing, a nuclear medicine scan.
   - "Type 0" (No thallium stress test): Indicates the absence of this specific test.
   - "Type 1" (A normal thallium stress test result): Indicates a normal result from the thallium stress test.
   - "Type 2" (A result indicating a fixed defect): Indicates a specific result from the thallium stress test.
   - "Type 3" (A result indicating a reversible defect): Indicates a specific result from the thallium stress test.
   - Thallium stress testing is conducted at specialized cardiac centers and healthcare facilities.

These detailed explanations clarify the significance of each input type in assessing heart health and diagnosing potential heart disease.

