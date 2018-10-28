# -*- coding: utf-8 -*-
import requests
def getSummId(name):
    key = input("enter your api key: ")
    text = requests.get("https://na.api.pvp.net/api/lol/na/v1.4/summoner/by-name/" + name + "?api_key=" + key)
    text = text.json()
    return text["id"]
