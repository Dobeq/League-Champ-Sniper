# -*- coding: utf-8 -*-
import requests
def getSummId(name):
    key = input("enter your api key: ")
    text = requests.get("https://na1.api.riotgames.com/lol/summoner/v4/summoners/by-name/" + name + "?api_key=" + key)
    text = text.json()
    return text["id"]
