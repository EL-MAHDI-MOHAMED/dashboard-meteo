import requests, json, time, csv, os
from kafka import KafkaProducer

API_KEY = "2e10d0bd88f543fdbf1200512252812"

CITIES = [
    "Tangier", "Tetouan", "Al Hoceima", "Nador", "Oujda", "Berkane", 
    "Fes", "Meknes", "Rabat", "Kenitra", "Casablanca", "El Jadida", 
    "Marrakech", "Essaouira", "Agadir", "Laayoune", "Dakhla"
]

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

CSV_FILE = "weather_history.csv"

# Initialize CSV with header if it doesn't exist
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["timestamp", "city", "temperature", "humidity", "wind", "condition"])

while True:
    for city in CITIES:
        try:
            url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}&aqi=yes"
            response = requests.get(url)
            
            if response.status_code == 200:
                data = response.json()
                if "current" in data:
                    # Kafka
                    producer.send("weather_topic", data)
                    print(f"📤 {city}: {data['current']['temp_c']}°C | 💧 {data['current']['humidity']}% | 🌬 {data['current']['wind_kph']} km/h")
                    
                    # CSV Append
                    with open(CSV_FILE, mode='a', newline='') as file:
                        writer = csv.writer(file)
                        writer.writerow([
                            time.strftime("%Y-%m-%d %H:%M:%S"),
                            city,
                            data['current']['temp_c'],
                            data['current']['humidity'],
                            data['current']['wind_kph'],
                            data['current']['condition']['text']
                        ])
            else:
                print(f"❌ Error fetching {city}")
                
        except Exception as e:
            print(f"⚠ Error: {e}")

    time.sleep(1)  # Refresh every 1 second (Fetching takes ~2s, total cycle ~3s)
