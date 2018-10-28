# -*- coding: utf-8 -*-
import requests
def getChampId(name):
    champs = requests.get("http://ddragon.leagueoflegends.com/cdn/6.24.1/data/en_US/champion.json")
    champs = champs.json()
    name = name.lower()
    name = name[0].upper() + name[1:]
    return champs["data"][name]["key"]