from fastapi import Request
import requests
from datetime import datetime, timedelta
import os
from dotenv import load_dotenv

load_dotenv()

weather_cache = {}

API_KEY = os.getenv("WEATHER_API_KEY")
BASE_URL = "https://api.weatherapi.com/v1/current.json"
LANG = "pt"
CACHE_DURATION = timedelta(minutes=15)

async def get_weather(request: Request):
    city = request.query_params.get("cidade")
    if not city:
        return {"error": "Falta o parâmetro ?cidade=CIDADE"}

    now = datetime.now()
    if city in weather_cache:
        cached = weather_cache[city]
        if now - cached["timestamp"] < CACHE_DURATION:
            return cached["data"]

    url = f"{BASE_URL}?key={API_KEY}&q={city}&aqi=no&lang={LANG}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        json_data = response.json()

        temp_c = json_data["current"]["temp_c"]
        cond = json_data["current"]["condition"]
        cond_text = cond["text"]
        cond_icon = cond["icon"]
        data = {
            "cidade": city,
            "temperatura": temp_c,
            "condicao": cond_text,
            "icone": cond_icon
        }

        weather_cache[city] = {
            "timestamp": now,
            "data": data
        }

        return data

    except Exception as e:
        return {"error": f"Error obtaining data from extern API: {str(e)}"}
