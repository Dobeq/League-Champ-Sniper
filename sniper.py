# -*- coding: utf-8 -*-

import passgetter, getid, requests, getsummid
#summId = getsummid.getSummId(input("Enter your account name: "))
summId = 0
creds = passgetter.getCreds()
champId = getid.getChampId(input("Enter champ name: "))
headerjson={"Accept": "application/json"}
checkStart = False
while not checkStart:
    testStart = requests.get(
        "https://127.0.0.1:" + creds[0] + "/lol-champ-select/v1/session",
        verify=False,
        headers=headerjson,
        auth=('riot', creds[1]))
    if testStart.status_code == 200:
        checkStart = True
testStart = testStart.json()
for player in testStart["myTeam"]:
    print(player['summonerId'])
    if player["summonerId"] == summId:
        cellId = player["cellId"]
for actor in testStart["actions"][0]:
    if actor["actorCellId"] == cellId:
        selectId = actor["id"]
req = requests.patch(
        "https://127.0.0.1:" + creds[0] + "/lol-champ-select/v1/session/actions/" + str(selectId) + "",
        json={"championId":champId},
        verify=False,
        headers=headerjson,
        auth=('riot', creds[1]))