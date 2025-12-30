import streamlit as st
import time
import random

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


# ===================== HEADER ===================== #
st.markdown("<h1>🌤 Dashboard Météo • Temps Réel</h1>", unsafe_allow_html=True)
st.write("Données rafraîchies automatiquement toutes les 4 secondes.")

placeholder = st.empty()

# ===================== LOOP UPDATE ===================== #
while True:
    data = get_weather_data()

    with placeholder.container():

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
