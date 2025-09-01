document.getElementById('predictForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    const feature1 = parseFloat(document.querySelector('input[name="feature1"]').value);
    const feature2 = parseFloat(document.querySelector('input[name="feature2"]').value);
    const feature3 = parseFloat(document.querySelector('input[name="feature3"]').value);

    const response = await fetch('/predict', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ features: [feature1, feature2, feature3] })
    });
    const result = await response.json();
    document.getElementById('result').textContent = `Prediction: ${result.prediction}`;
});