from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)

# Load your pre-trained machine learning model
with open("model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    # Get form data from the request
    form_data = request.json

    # Extract the features from the form data
    sex = int(form_data["sex"])
    cp = int(form_data["cp"])
    fbs = int(form_data["fbs"])
    restecg = int(form_data["restecg"])
    exang = int(form_data["exang"])
    slope = int(form_data["slope"])
    ca = int(form_data["ca"])
    thal = int(form_data["thal"])

    # Make predictions using the model
    prediction = model.predict([[sex, cp, fbs, restecg, exang, slope, ca, thal]])

    # Process the prediction result as needed
    prediction_text = "Heart Disease" if prediction[0] == 1 else "No Heart Disease"

    # Return the prediction as JSON
    return jsonify({"prediction": prediction_text})

if __name__ == "__main__":
    app.run(debug=True)
