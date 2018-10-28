# -*- coding: utf-8 -*-

import passgetter, getid, requests
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
req = requests.patch(
        #"https://127.0.0.1:" + creds[0] + "/lol-champ-select/v1/session/actions/1",
        "https://127.0.0.1:53523/lol-champ-select/v1/session/actions/1",
        json={"championId":champId},
        verify=False,
        headers=headerjson,
        auth=('riot', creds[1]))