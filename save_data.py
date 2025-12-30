import pandas as pd
import time
import random
import os

file = "data.csv"

# Création du CSV si n'existe pas
if not os.path.exists(file):
    df = pd.DataFrame(columns=["timestamp", "temperature", "humidity", "wind"])
    df.to_csv(file, index=False)

while True:
    data = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "temperature": round(random.uniform(12, 25), 1),
        "humidity": random.randint(40, 85),
        "wind": round(random.uniform(5, 30), 1)
    }

    df = pd.DataFrame([data])
    df.to_csv(file, mode='a', header=False, index=False)

    print("🔹 Data saved:", data)
    time.sleep(4)
