from flask import Flask, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open('model/trained_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route("/predict", methods=["GET", "POST"])
def predict():
    if request.method == "POST":
        # Get data from the form
        data = request.form.to_dict()
        # Convert data to the format required by the model
        input_data = np.array([[float(data['feature1']), float(data['feature2']), float(data['feature3'])]])
        # Make prediction
        prediction = model.predict(input_data)
        return render_template("index.html", prediction=prediction[0])

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)