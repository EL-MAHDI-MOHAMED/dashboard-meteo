# 🌤️ Real-Time Weather Dashboard with AI Predictions

A modern, real-time data engineering project that fetches live weather data for major Moroccan cities, processes it, and displays it on an interactive dashboard with AI-powered weather state predictions.

## 🚀 Features
- **Real-Time Data**: Fetches live weather metrics (Temperature, Humidity, Wind) every few seconds.
- **Multi-City Support**: Tracks 17 major cities including Tangier, Casablanca, Marrakech, and Dakhla.
- **AI Integration**: Uses a Machine Learning model to predict weather conditions based on live metrics.
- **Data Persistence**: Archives historical data to `weather_history.csv` for future analysis.
- **Interactive Dashboard**: Built with Streamlit, offering a sleek, dark-themed UI.

## 🏗️ Architecture
The pipeline consists of the following components:
1.  **Data Producer** (`producer_weather.py`): Fetches data from WeatherAPI.com, sends it to Kafka, and saves it to CSV.
2.  **Apache Kafka**: (Optional) Message broker for streaming data.
3.  **Apache Spark**: (Optional) For distributed data processing.
4.  **Weather Dashboard** (`dashboard.py`): Streamlit app that reads data and visualizes it.
5.  **ML Model** (`weather_ml_model.py`): Random Forest classifier for weather state prediction.

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.8+
- Docker & Docker Compose (for Kafka/Spark)
- A generic API Key from [WeatherAPI.com](https://www.weatherapi.com/)

### 1. Clone the Repository
```bash
git clone https://github.com/EL-MAHDI-MOHAMED/dashboard-meteo.git
cd dashboard-meteo
```

### 2. Install Dependencies
```bash
pip install requests kafka-python streamlit pandas scikit-learn
```

### 3. Start Infrastructure (Optional)
If you want to run the full Kafka/Spark stack:
```bash
docker compose up -d
```

### 4. Run the Producer
This script starts fetching data. Keep this terminal open.
```bash
python producer_weather.py
```

### 5. Launch the Dashboard
Open a new terminal and run:
```bash
streamlit run dashboard.py
```
Access the dashboard at: `http://localhost:8501`

## 📁 Project Structure
```
├── dashboard.py           # Main Streamlit application
├── producer_weather.py    # Data fetcher & CSV logger
├── weather_ml_model.py    # Machine Learning logic
├── weather_history.csv    # Historical data storage
├── docker-compose.yml     # Infrastructure (Kafka, Zookeeper, Spark)
└── Dockerfile             # Custom Spark image definition
```

## 🤝 Contributing
Feel free to submit issues or pull requests. 
Happy Coding! 🇲🇦✨
