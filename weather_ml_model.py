"""
Script d'entraînement du modèle de prédiction météo
Utilise Random Forest pour classifier l'état de la météo basé sur:
- Température (°C)
- Humidité (%)
- Vitesse du vent (km/h)
"""
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, accuracy_score
import joblib
import os


def create_training_data():
    """
    Génère des données d'entraînement synthétiques pour le modèle
    États: Ensoleillé, Nuageux, Pluvieux
    """
    np.random.seed(42)
    
    data = []
    
    # Ensoleillé: Temp élevée, humidité basse, vent modéré
    for _ in range(500):
        data.append({
            'temperature': np.random.uniform(20, 35),
            'humidity': np.random.randint(20, 50),
            'wind': np.random.uniform(5, 15),
            'weather_state': 'Ensoleillé'
        })
    
    # Nuageux: Temp moyenne, humidité moyenne, vent variable
    for _ in range(500):
        data.append({
            'temperature': np.random.uniform(15, 25),
            'humidity': np.random.randint(45, 70),
            'wind': np.random.uniform(10, 25),
            'weather_state': 'Nuageux'
        })
    
    # Pluvieux: Temp basse/moyenne, humidité élevée, vent fort
    for _ in range(500):
        data.append({
            'temperature': np.random.uniform(10, 20),
            'humidity': np.random.randint(65, 95),
            'wind': np.random.uniform(15, 35),
            'weather_state': 'Pluvieux'
        })
    
    return pd.DataFrame(data)


def train_weather_model():
    """
    Entraîne le modèle Random Forest et le sauvegarde
    """
    print("📊 Création des données d'entraînement...")
    df = create_training_data()
    
    # Séparation des features et target
    X = df[['temperature', 'humidity', 'wind']]
    y = df['weather_state']
    
    # Split train/test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    print("🤖 Entraînement du modèle Random Forest...")
    model = RandomForestClassifier(
        n_estimators=100,
        max_depth=10,
        random_state=42,
        n_jobs=-1
    )
    
    model.fit(X_train, y_train)
    
    # Évaluation
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    print(f"✅ Précision du modèle: {accuracy * 100:.2f}%")
    print("\n📈 Rapport de classification:")
    print(classification_report(y_test, y_pred))
    
    # Sauvegarde du modèle
    model_path = "weather_model.pkl"
    joblib.dump(model, model_path)
    print(f"💾 Modèle sauvegardé dans: {model_path}")
    
    return model


def predict_weather_state(temperature, humidity, wind):
    """
    Prédit l'état de la météo à partir des paramètres
    
    Args:
        temperature: Température en °C
        humidity: Humidité en %
        wind: Vitesse du vent en km/h
    
    Returns:
        str: État prédit (Ensoleillé, Nuageux, Pluvieux)
    """
    model_path = "weather_model.pkl"
    
    # Charger le modèle ou l'entraîner si n'existe pas
    if not os.path.exists(model_path):
        print("⚠ Modèle non trouvé, entraînement en cours...")
        model = train_weather_model()
    else:
        model = joblib.load(model_path)
    
    # Prédiction
    features = np.array([[temperature, humidity, wind]])
    prediction = model.predict(features)[0]
    probabilities = model.predict_proba(features)[0]
    
    return prediction, probabilities


def get_weather_confidence(probabilities):
    """
    Retourne la confiance maximale de la prédiction
    """
    return max(probabilities) * 100


if __name__ == "__main__":
    # Entraîner le modèle
    train_weather_model()
    
    # Test de prédiction
    print("\n🧪 Tests de prédiction:")
    test_cases = [
        (28, 30, 8, "Ensoleillé"),
        (18, 60, 18, "Nuageux"),
        (12, 85, 25, "Pluvieux")
    ]
    
    for temp, hum, wind, expected in test_cases:
        prediction, probs = predict_weather_state(temp, hum, wind)
        confidence = get_weather_confidence(probs)
        print(f"Temp: {temp}°C, Humidité: {hum}%, Vent: {wind} km/h")
        print(f"  → Prédiction: {prediction} (Confiance: {confidence:.1f}%)")
        print(f"  → Attendu: {expected}\n")
