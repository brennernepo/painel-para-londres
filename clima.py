"""Previsão do tempo, histórico das mesmas datas e horários do sol.

Previsão e histórico vêm da Open-Meteo (gratuita, sem chave). Nascer e pôr do sol são calculados
aqui, com o algoritmo da NOAA, porque a API erra o horário no dia em que os relógios mudam.
"""

import math
from datetime import date, datetime, timedelta, timezone
from zoneinfo import ZoneInfo

import requests
import streamlit as st

FUSO = ZoneInfo("Europe/London")
URL_PREVISAO = "https://api.open-meteo.com/v1/forecast"
URL_HISTORICO = "https://archive-api.open-meteo.com/v1/archive"

# Códigos de tempo da OMM usados pela Open-Meteo
CONDICOES = {
    0: ("☀️", "Céu limpo"), 1: ("🌤", "Poucas nuvens"), 2: ("⛅", "Parcialmente nublado"), 3: ("☁️", "Nublado"),
    45: ("🌫", "Neblina"), 48: ("🌫", "Neblina com geada"),
    51: ("🌦", "Garoa fraca"), 53: ("🌦", "Garoa"), 55: ("🌧", "Garoa forte"),
    56: ("🌧", "Garoa congelante"), 57: ("🌧", "Garoa congelante"),
    61: ("🌧", "Chuva fraca"), 63: ("🌧", "Chuva"), 65: ("🌧", "Chuva forte"),
    66: ("🌧", "Chuva congelante"), 67: ("🌧", "Chuva congelante"),
    71: ("🌨", "Neve fraca"), 73: ("🌨", "Neve"), 75: ("🌨", "Neve forte"), 77: ("🌨", "Grãos de neve"),
    80: ("🌦", "Pancadas fracas"), 81: ("🌧", "Pancadas de chuva"), 82: ("⛈", "Pancadas fortes"),
    85: ("🌨", "Pancadas de neve"), 86: ("🌨", "Pancadas de neve"),
    95: ("⛈", "Trovoada"), 96: ("⛈", "Trovoada com granizo"), 99: ("⛈", "Trovoada com granizo"),
}


# ---------------------------------------------------------------------------
# Sol
# ---------------------------------------------------------------------------
def _minutos_utc(dia: date, lat: float, lon: float, zenite: float, nascer: bool) -> float:
    """Minutos desde 0h UTC em que o sol cruza o ângulo de zênite pedido (NOAA)."""
    jd = dia.toordinal() + 1721424.5 + 0.5 - lon / 360  # dia juliano no meio-dia solar aproximado
    t = (jd - 2451545.0) / 36525
    l0 = (280.46646 + t * (36000.76983 + t * 0.0003032)) % 360
    m = 357.52911 + t * (35999.05029 - 0.0001537 * t)
    e = 0.016708634 - t * (0.000042037 + 0.0000001267 * t)
    mr = math.radians(m)
    c = (math.sin(mr) * (1.914602 - t * (0.004817 + 0.000014 * t))
         + math.sin(2 * mr) * (0.019993 - 0.000101 * t) + math.sin(3 * mr) * 0.000289)
    omega = math.radians(125.04 - 1934.136 * t)
    lam = math.radians(l0 + c - 0.00569 - 0.00478 * math.sin(omega))
    eps0 = 23 + (26 + (21.448 - t * (46.815 + t * (0.00059 - t * 0.001813))) / 60) / 60
    eps = math.radians(eps0 + 0.00256 * math.cos(omega))
    dec = math.asin(math.sin(eps) * math.sin(lam))
    y = math.tan(eps / 2) ** 2
    l0r = math.radians(l0)
    eq_tempo = 4 * math.degrees(
        y * math.sin(2 * l0r) - 2 * e * math.sin(mr) + 4 * e * y * math.sin(mr) * math.cos(2 * l0r)
        - 0.5 * y * y * math.sin(4 * l0r) - 1.25 * e * e * math.sin(2 * mr)
    )
    latr = math.radians(lat)
    ha = math.degrees(math.acos(
        math.cos(math.radians(zenite)) / (math.cos(latr) * math.cos(dec)) - math.tan(latr) * math.tan(dec)
    ))
    meio_dia = 720 - 4 * lon - eq_tempo
    return meio_dia - 4 * ha if nascer else meio_dia + 4 * ha


def _hora_local(dia: date, minutos: float) -> datetime:
    base = datetime(dia.year, dia.month, dia.day, tzinfo=timezone.utc)
    return (base + timedelta(minutes=minutos)).astimezone(FUSO)


def sol(dia: date, lat: float, lon: float) -> dict:
    """Nascer, pôr do sol, fim do crepúsculo civil (quando escurece de fato) e horas de luz."""
    nascer = _hora_local(dia, _minutos_utc(dia, lat, lon, 90.833, True))
    por = _hora_local(dia, _minutos_utc(dia, lat, lon, 90.833, False))
    escuro = _hora_local(dia, _minutos_utc(dia, lat, lon, 96.0, False))
    return {"nascer": nascer, "por": por, "escuro": escuro, "luz": por - nascer}


# ---------------------------------------------------------------------------
# Open-Meteo
# ---------------------------------------------------------------------------
@st.cache_data(ttl=3600, show_spinner=False)
def previsao(lat: float, lon: float) -> dict:
    """Previsão diária dos próximos 16 dias, indexada pela data (AAAA-MM-DD). Dias sem dado ficam de fora."""
    resp = requests.get(URL_PREVISAO, timeout=10, params={
        "latitude": lat, "longitude": lon, "timezone": "Europe/London", "forecast_days": 16,
        "daily": "weather_code,temperature_2m_max,temperature_2m_min,precipitation_probability_max,precipitation_sum",
    })
    resp.raise_for_status()
    d = resp.json()["daily"]
    dias = {}
    for i, dia in enumerate(d["time"]):
        if d["weather_code"][i] is None or d["temperature_2m_max"][i] is None:
            continue
        dias[dia] = {
            "codigo": d["weather_code"][i],
            "max": d["temperature_2m_max"][i],
            "min": d["temperature_2m_min"][i],
            "chance": d["precipitation_probability_max"][i],
            "chuva_mm": d["precipitation_sum"][i],
        }
    return dias


@st.cache_data(ttl=7 * 86400, show_spinner=False)
def historico(lat: float, lon: float, inicio: date, fim: date, anos: int = 10) -> dict:
    """Média das mesmas datas nos últimos `anos` anos, indexada por MM-DD."""
    ultimo_ano = date.today().year - 1
    resp = requests.get(URL_HISTORICO, timeout=20, params={
        "latitude": lat, "longitude": lon, "timezone": "Europe/London",
        "start_date": inicio.replace(year=ultimo_ano - anos + 1).isoformat(),
        "end_date": fim.replace(year=ultimo_ano).isoformat(),
        "daily": "temperature_2m_max,temperature_2m_min,precipitation_sum",
    })
    resp.raise_for_status()
    d = resp.json()["daily"]
    datas = {(inicio + timedelta(days=i)).strftime("%m-%d") for i in range((fim - inicio).days + 1)}
    grupos: dict[str, list] = {}
    for dia, tmax, tmin, chuva in zip(d["time"], d["temperature_2m_max"], d["temperature_2m_min"], d["precipitation_sum"]):
        if dia[5:] in datas and None not in (tmax, tmin, chuva):
            grupos.setdefault(dia[5:], []).append((tmax, tmin, chuva))
    return {
        md: {
            "max": sum(v[0] for v in vals) / len(vals),
            "min": sum(v[1] for v in vals) / len(vals),
            "anos_chuva": sum(v[2] >= 1 for v in vals),
            "anos": len(vals),
        }
        for md, vals in grupos.items()
    }
