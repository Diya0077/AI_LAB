import pickle
import numpy as np
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

# Load your trained model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

@app.route("/predict", methods=["POST"])
def predict():
    data = request.get_json()
    # Example: expecting features as a list
    features = np.array(data["features"]).reshape(1, -1)
    prediction = model.predict(features)
    return jsonify({"prediction": int(prediction[0])})

@app.route("/")
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)

with open("model.pkl", "wb") as f:
    pickle.dump(model, f)