import streamlit as st
import time
import random
import os

# Import du modèle de prédiction
try:
    from weather_ml_model import predict_weather_state
    MODEL_AVAILABLE = True
except ImportError:
    MODEL_AVAILABLE = False
    st.warning("⚠ Module de prédiction ML non disponible")

# ===================== CONFIG ===================== #
st.set_page_config(
    page_title="Dashboard Météo Temps Réel",
    page_icon="🌦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===================== CSS STYLE ===================== #
st.markdown("""
    <style>
    
    /* General UI */
    .main {
        background-color: #0d0f1a;
    }
    h1,h2,h3,h4,h5 {
        color: white;
        font-weight: 700;
    }
    p, .css-1y4p8pa, .css-q8sbsg {
        color: #c7c7c7 !important;
    }

    /* Cards */
    .card {
        background-color: #161a2d;
        padding: 25px;
        border-radius: 12px;
        text-align: center;
        box-shadow: 0px 0px 15px rgba(0,0,0,0.4);
        transition: 0.3s;
    }
    .card:hover {
        transform: scale(1.03);
        box-shadow: 0px 0px 25px rgba(0,0,0,0.7);
    }
    .value {
        font-size: 40px;
        font-weight: bold;
        color: #4cb4ff;
    }
    .unit {
        font-size: 16px;
        color: #8da9c4;
    }
    
    /* Weather prediction card */
    .prediction-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 30px;
        border-radius: 15px;
        text-align: center;
        box-shadow: 0px 5px 20px rgba(102, 126, 234, 0.4);
        margin: 20px 0;
    }
    .prediction-title {
        font-size: 24px;
        font-weight: bold;
        color: white;
        margin-bottom: 15px;
    }
    .prediction-state {
        font-size: 48px;
        font-weight: bold;
        color: #fff;
        margin: 10px 0;
    }
    .prediction-confidence {
        font-size: 18px;
        color: #e0e0e0;
    }
    .prediction-emoji {
        font-size: 80px;
        margin: 15px 0;
    }
    
    </style>
""", unsafe_allow_html=True)


# ===================== DATA SIMULATION ===================== #
# Remplace ici par tes valeurs réelles MQTT/Kafka/API
def get_weather_data():
    return {
        "temperature": round(random.uniform(12, 25), 1),
        "humidity": random.randint(40, 85),
        "wind": round(random.uniform(5, 30), 1)
    }


def get_weather_emoji(state):
    """Retourne l'emoji correspondant à l'état météo"""
    emojis = {
        "Ensoleillé": "☀️",
        "Nuageux": "☁️",
        "Pluvieux": "🌧️",
        "Inconnu": "❓"
    }
    return emojis.get(state, "❓")


def get_weather_prediction(temperature, humidity, wind):
    """Obtient la prédiction ML de l'état météo"""
    if not MODEL_AVAILABLE:
        return "N/A", 0
    
    try:
        prediction, probabilities = predict_weather_state(temperature, humidity, wind)
        confidence = max(probabilities) * 100
        return prediction, confidence
    except Exception as e:
        st.error(f"Erreur de prédiction: {e}")
        return "Erreur", 0


# ===================== HEADER ===================== #
st.markdown("<h1>🌤 Dashboard Météo • Temps Réel</h1>", unsafe_allow_html=True)
st.write("Données rafraîchies automatiquement toutes les 4 secondes.")

placeholder = st.empty()

# ===================== LOOP UPDATE ===================== #
while True:
    data = get_weather_data()

    with placeholder.container():
        
        # Prédiction ML
        if MODEL_AVAILABLE:
            prediction, confidence = get_weather_prediction(
                data['temperature'], 
                data['humidity'], 
                data['wind']
            )
            
            emoji = get_weather_emoji(prediction)
            
            st.markdown(f"""
                <div class="prediction-card">
                    <div class="prediction-title">🤖 Prédiction IA - État de la Météo</div>
                    <div class="prediction-emoji">{emoji}</div>
                    <div class="prediction-state">{prediction}</div>
                    <div class="prediction-confidence">Confiance: {confidence:.1f}%</div>
                </div>
            """, unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)

        with col1:
            st.markdown(f"""
                <div class="card">
                    <h3>🌡 Température</h3>
                    <div class="value">{data['temperature']}°C</div>
                    <p class="unit">Température actuelle</p>
                </div>
            """, unsafe_allow_html=True)

        with col2:
            st.markdown(f"""
                <div class="card">
                    <h3>💧 Humidité</h3>
                    <div class="value">{data['humidity']}%</div>
                    <p class="unit">Taux d'humidité</p>
                </div>
            """, unsafe_allow_html=True)

        with col3:
            st.markdown(f"""
                <div class="card">
                    <h3>🌬 Vent</h3>
                    <div class="value">{data['wind']} km/h</div>
                    <p class="unit">Vitesse du vent</p>
                </div>
            """, unsafe_allow_html=True)

    time.sleep(4)   # refresh interval
