const form = document.getElementById("form");
const resultado = document.getElementById("resultado");

form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const data = {
        tenure: Number(document.getElementById("tenure").value),
        MonthlyCharges: Number(document.getElementById("MonthlyCharges").value),
        Contract: document.getElementById("Contract").value,
        InternetService: document.getElementById("InternetService").value,
        PaymentMethod: document.getElementById("PaymentMethod").value
    };

    try {
        const response = await fetch("https://churn-predictor-ml.onrender.com/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(data)
        });

        const result = await response.json();

        if (result.prediction === 1) {
            resultado.innerHTML = `⚠️ Cliente en riesgo (${(result.probability*100).toFixed(1)}%)`;
            resultado.style.color = "red";
        } else {
            resultado.innerHTML = `✅ Cliente estable (${(result.probability*100).toFixed(1)}%)`;
            resultado.style.color = "green";
        }

    } catch (error) {
        resultado.innerHTML = "Error conectando con API";
    }
});