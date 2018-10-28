# -*- coding: utf-8 -*-
def getCreds():
    path = input("enter the league path: ")
    if path == "":
        path = "C:/Riot Games/League of Legends"
    with open(path + "/lockfile", 'r+') as file:
        text = file.read()
        split = text.split(':')
        port=split[2]
        pw=split[3]
    return [port, pw]
