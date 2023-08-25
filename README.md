# Heart Disease Prediction Web Application

![Web App Screenshot](web_app_screenshot.png)

## Overview

This project involves the development of a web application that predicts the likelihood of heart disease based on user-provided patient details. The application utilizes a machine learning model trained on a Kaggle dataset. The model was evaluated using the Random Forest and K-Nearest Neighbors (KNN) algorithms. The KNN algorithm was chosen as the final model for the web application.

## Web Application Interface

The web application provides a user-friendly interface where users can input patient details through various input fields. After filling out the details, users can click the "Predict" button to trigger the prediction process. The application then displays a prediction indicating whether the patient is likely to have heart disease or not.

## Machine Learning Model

The machine learning model used in this project is a K-Nearest Neighbors (KNN) classifier. The model was trained on a Kaggle dataset containing various features related to heart health. The accuracy of the model was evaluated using cross-validation and achieved an accuracy of approximately 85%.

## Project Structure

The project is organized as follows:

- `index.html`: The HTML file containing the user interface for the web application.
- `app.py`: The Flask web application script responsible for serving the HTML, handling form submissions, and making predictions using the trained model.
- `model.pkl`: The serialized KNN model saved as a binary file.
- `web_app_screenshot.png`: A screenshot of the web application's user interface.

## Usage

1. Install the required Python packages using `pip install -r requirements.txt`.
2. Run the Flask application using `python app.py`.
3. Access the web application by navigating to `http://localhost:5000` in your web browser.
4. Fill out the patient details in the input fields.
5. Click the "Predict" button to receive the heart disease prediction.

## Screenshots

### Model Evaluation

![Random Forest Accuracy](random_forest_accuracy.png)
![KNN Accuracy](knn_accuracy.png)

### Web Application

![Web App Screenshot](web_app_screenshot.png)

## Acknowledgments

- Kaggle (Dataset source)
- Scikit-learn (Machine learning library)
- Flask (Web framework)

## License

This project is licensed under the [MIT License](LICENSE).
