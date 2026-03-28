"""Модуль для работы с внешними API и запросов."""

import requests
from typing import Dict


def getIp() -> str:
    """Получает текущий IP-адрес.

    Returns:
        str: IP-адрес в формате строки
    """
    url = "https://ifconfig.me/ip"
    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    return response.text.strip()


def getTime(ip: str) -> Dict[str, str]:
    url = f"https://timeapi.io/api/Time/current/ip?ipAddress={ip}"

    headers = {
        "accept": "application/json"
    }

    response = requests.get(url, headers=headers)

    return response.json()


def getHoroscope(sign: str) -> Dict[str, str]:
    url = f"https://ohmanda.com/api/horoscope/{sign}"
    response = requests.get(url)
    return response.json()



def getZodiacSign(day: int, month: int) -> str:
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "aquarius"
    else:
        return "pisces"
