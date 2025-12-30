# 🌦️ Dashboard Météo avec Machine Learning

## 📋 Description du Projet

Ce projet collecte des données météorologiques en temps réel et utilise un **modèle de Machine Learning** pour prédire l'état de la météo (Ensoleillé ☀️, Nuageux ☁️, Pluvieux 🌧️).

### Architecture du Système

1. **Producer Kafka** (`producer_weather.py`) : Récupère les données de l'API WeatherAPI
2. **Spark Consumer** (`spark_consumer.py`) : Traite les données via Apache Spark
3. **Générateur de Données** (`save_data.py`) : Génère des données aléatoires avec prédictions ML
4. **Modèle ML** (`weather_ml_model.py`) : Random Forest Classifier pour prédire l'état météo
5. **Dashboard Streamlit** (`dashboard.py`) : Visualisation en temps réel avec prédictions IA

---

## 🤖 Modèle de Machine Learning

### Caractéristiques
- **Algorithme** : Random Forest Classifier
- **Précision** : ~97%
- **Features utilisées** :
  - 🌡️ Température (°C)
  - 💧 Humidité (%)
  - 🌬️ Vitesse du vent (km/h)

### Classes Prédites
1. **Ensoleillé** ☀️ : Température élevée, humidité basse
2. **Nuageux** ☁️ : Température moyenne, humidité modérée
3. **Pluvieux** 🌧️ : Humidité élevée, vent fort

---

## 🚀 Installation et Lancement

### 1. Installer les dépendances
```bash
pip install -r requirements.txt
```

### 2. Entraîner le modèle ML (première fois)
```bash
python weather_ml_model.py
```

Cela créera le fichier `weather_model.pkl` contenant le modèle entraîné.

### 3. Lancer le générateur de données (optionnel)
```bash
python save_data.py
```

Cela générera des données dans `data.csv` avec les prédictions météo.

### 4. Lancer le dashboard Streamlit
```bash
streamlit run dashboard.py
```

Le dashboard sera accessible sur `http://localhost:8501`

---

## 📊 Fonctionnalités du Dashboard

### Métriques Affichées
- 🌡️ **Température actuelle** en °C
- 💧 **Humidité** en %
- 🌬️ **Vitesse du vent** en km/h
- 🤖 **Prédiction IA** avec confiance en %

### Mise à Jour
Les données se rafraîchissent automatiquement toutes les 4 secondes.

---

## 🔧 Configuration

### API WeatherAPI
Si vous voulez utiliser de vraies données météo, modifiez `producer_weather.py` :
```python
API_KEY = "votre_clé_api_ici"
CITY = "Votre_Ville"
```

### Docker (Optionnel)
Pour lancer Kafka et Spark avec Docker :
```bash
docker-compose up -d
```

---

## 📁 Structure des Fichiers

```
dashboard-meteo/
├── weather_ml_model.py      # 🤖 Modèle ML (entraînement + prédiction)
├── weather_model.pkl         # 💾 Modèle entraîné (généré)
├── dashboard.py              # 📊 Interface Streamlit
├── save_data.py              # 💾 Génération de données avec ML
├── producer_weather.py       # 📡 Producer Kafka
├── spark_consumer.py         # ⚡ Consumer Spark
├── data.csv                  # 📁 Données générées
├── requirements.txt          # 📦 Dépendances Python
├── docker-compose.yml        # 🐳 Config Docker
└── README_ML.md              # 📖 Documentation
```

---

## 🧪 Tests du Modèle

Le modèle a été testé avec différents scénarios :

| Température | Humidité | Vent | Prédiction | Confiance |
|-------------|----------|------|------------|-----------|
| 28°C | 30% | 8 km/h | ☀️ Ensoleillé | 100% |
| 18°C | 60% | 18 km/h | ☁️ Nuageux | 97% |
| 12°C | 85% | 25 km/h | 🌧️ Pluvieux | 98% |

---

## 📈 Améliorations Futures

- [ ] Intégration avec vraies données Kafka en temps réel
- [ ] Ajout de prédictions sur plusieurs jours
- [ ] Graphiques historiques des prédictions
- [ ] Modèle de Deep Learning (LSTM) pour séries temporelles
- [ ] Alertes météo automatiques
- [ ] Export des prédictions en base de données

---

## 🛠️ Technologies Utilisées

- **Python 3.x**
- **Streamlit** - Dashboard interactif
- **scikit-learn** - Machine Learning
- **pandas** - Manipulation de données
- **Apache Kafka** - Streaming de données
- **Apache Spark** - Traitement distribué
- **Docker** - Containerisation

---

## 👨‍💻 Auteur

Projet BigData avec Machine Learning pour prédiction météorologique

---

## 📝 Notes

- Le modèle doit être entraîné une fois avant utilisation
- Les prédictions sont basées sur des patterns statistiques
- La précision peut varier selon les données réelles utilisées
