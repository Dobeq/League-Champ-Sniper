# -*- coding: utf-8 -*-
import requests
def getChampId(name):
    champs = requests.get("http://ddragon.leagueoflegends.com/cdn/6.24.1/data/en_US/champion.json")
    champs = champs.json()
    name = name.lower()
    name.split(" ")
    for word in name:
        word = word[0].upper() + word[1:]
    namecapped = ""
    for word in name:
        namecapped += word
    return champs["data"][namecapped]["key"]