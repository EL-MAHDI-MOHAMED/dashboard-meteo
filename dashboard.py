import streamlit as st
import pandas as pd
import time
import os

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


# ===================== DATA LOADING ===================== #
CSV_FILE = "weather_history.csv"

def get_latest_data(city_name):
    if os.path.exists(CSV_FILE):
        try:
            # Read CSV efficiently
            df = pd.read_csv(CSV_FILE)
            
            # Filter by city
            city_df = df[df['city'] == city_name]
            
            if not city_df.empty:
                # Return the last row as a dictionary
                return city_df.iloc[-1].to_dict()
        except:
            return None
    return None

# ===================== SIDEBAR ===================== #
st.sidebar.header("🌍 Configuration")
selected_city = st.sidebar.selectbox(
    "Choisir la ville",
    [
        "Tangier", "Tetouan", "Al Hoceima", "Nador", "Oujda", "Berkane", 
        "Fes", "Meknes", "Rabat", "Kenitra", "Casablanca", "El Jadida", 
        "Marrakech", "Essaouira", "Agadir", "Laayoune", "Dakhla"
    ]
)


# ===================== HEADER ===================== #
st.markdown("<h1>🌤 Dashboard Météo • Temps Réel</h1>", unsafe_allow_html=True)
st.write("Données rafraîchies automatiquement toutes les 4 secondes.")

placeholder = st.empty()

# ===================== LOOP UPDATE ===================== #
while True:
    data = get_latest_data(selected_city)
    
    if data is None:
        # Fallback simulation if no data found
        data = {
            "temperature": "--",
            "humidity": "--", 
            "wind": "--",
            "city": selected_city
        }

    with placeholder.container():

        st.markdown(f"<h2 style='text-align: center;'>📍 {data['city']}</h2>", unsafe_allow_html=True)

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
