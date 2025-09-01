// filepath: responsive-model-app/static/index.js

document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("prediction-form");
    const resultDiv = document.getElementById("result");

    form.addEventListener("submit", function(event) {
        event.preventDefault();
        
        const formData = new FormData(form);
        const data = {};
        formData.forEach((value, key) => {
            data[key] = value;
        });

        fetch("/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify(data),
        })
        .then(response => response.json())
        .then(data => {
            resultDiv.innerHTML = `Prediction: ${data.prediction}`;
        })
        .catch(error => {
            console.error("Error:", error);
            resultDiv.innerHTML = "An error occurred while making the prediction.";
        });
    });
});