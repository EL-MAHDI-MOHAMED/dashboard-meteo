import requests, json, time
from kafka import KafkaProducer

API_KEY = "2e10d0bd88f543fdbf1200512252812"   # <<--- mets TA clé ici
CITY = "Casablanca"

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",   # si tu lances le code SUR WINDOWS
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)



while True:
    url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={CITY}&aqi=yes"
    data = requests.get(url).json()

    print("🌤 API Response:", data)  # affichage console

    if "current" in data:
        producer.send("weather_topic", data)
        print(f"📤 Sent to Kafka -> Temp: {data['current']['temp_c']}°C  Humidity:{data['current']['humidity']}%")
    else:
        print("❌ No weather data returned. Verify API call or API key quota.")

    time.sleep(5)
query = weather.writeStream \
    .outputMode("append") \
    .format("csv") \
    .option("path", "/opt/spark/data/weather_csv") \
    .option("checkpointLocation", "/opt/spark/checkpoints") \
    .start()
if data["current"]["temp_c"] > 30:
    print("⚠ Alerte chaleur !")
    # email/sms webhook possible ici
