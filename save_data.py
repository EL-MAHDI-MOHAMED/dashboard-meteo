import pandas as pd
import time
import random
import os
import sys

# Import du modèle de prédiction
try:
    from weather_ml_model import predict_weather_state
except ImportError:
    print("⚠ Module weather_ml_model non trouvé. Les prédictions météo ne seront pas disponibles.")
    predict_weather_state = None

file = "data.csv"

# Création du CSV si n'existe pas
if not os.path.exists(file):
    df = pd.DataFrame(columns=["timestamp", "temperature", "humidity", "wind", "weather_state", "confidence"])
    df.to_csv(file, index=False)

while True:
    data = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "temperature": round(random.uniform(12, 25), 1),
        "humidity": random.randint(40, 85),
        "wind": round(random.uniform(5, 30), 1)
    }
    
    # Prédiction de l'état météo avec le modèle ML
    if predict_weather_state:
        try:
            prediction, probabilities = predict_weather_state(
                data["temperature"], 
                data["humidity"], 
                data["wind"]
            )
            data["weather_state"] = prediction
            data["confidence"] = round(max(probabilities) * 100, 1)
        except Exception as e:
            print(f"❌ Erreur de prédiction: {e}")
            data["weather_state"] = "Inconnu"
            data["confidence"] = 0
    else:
        data["weather_state"] = "N/A"
        data["confidence"] = 0

    df = pd.DataFrame([data])
    df.to_csv(file, mode='a', header=False, index=False)

    print(f"🔹 Data saved: {data}")
    time.sleep(4)
