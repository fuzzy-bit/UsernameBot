# this requires "requests" package to run (pip install requests)
# yall dumbasses so if you don't know where to get pip here it is:
# https://pip.pypa.io/en/stable/installing/

from decimal import *
import string
import requests
import random
import time
import os
import io



LetterAmount = input("Character amount: ")
DelayTime = input("Delay time: ")
FoundUsernames = ""
FoundUsernamesCounter = 0
SearchedUsernamesCounter = 0
DuplicateUsernames = 0
TimeElapsed = 0

Chars = string.ascii_letters + string.digits
AllChars = string.ascii_letters + "_" + string.digits

UsernameListAppend = open("FoundUsernames.txt", "a+")
UsernameListRead = open("FoundUsernames.txt", "r+")



if Decimal(LetterAmount) <= 2:
    LetterAmount = 3

if Decimal(DelayTime) < 1:
    DelayTime = 1



def Clear():
    os.system("cls" if os.name == "nt" else 'clear')



while True:
    Clear()
    Username = ""

    for i in range(0, int(LetterAmount)):
        if i != 0 and i != int(LetterAmount):
            Username = Username + random.choice(AllChars)
        else:
            Username = Username + random.choice(Chars)
            
    print(Username)

    Payload = {
        "request.birthday": "08/09/2005",
        "request.context": "Unknown",
        "request.username": Username
    }

    RequestUrl = "https://auth.roblox.com/v1/usernames/validate"
    GetRequest = requests.get("https://auth.roblox.com/v1/usernames/validate", params = Payload)
    JsonResponse = GetRequest.json()
    
    print(JsonResponse["message"])
    print("\n-- STATS --\n")
    
    SearchedUsernamesCounter = SearchedUsernamesCounter + 1
    
    if JsonResponse["message"] != "Username is already in use" and JsonResponse["message"] != "Username not appropriate for Roblox" and JsonResponse["message"] != "Usernames can be 3 to 20 characters long":
        if not Username in UsernameListRead.read() and not Username in FoundUsernames:
            FoundUsernamesCounter = FoundUsernamesCounter + 1
            UsernameListAppend.write(Username + "\n")

            if FoundUsernamesCounter >= 2:
                FoundUsernames = FoundUsernames + ", " + Username
            else:
                FoundUsernames = FoundUsernames + Username
        else:
            DuplicateUsernames = DuplicateUsernames + 1
    
    print("Found usernames: " + FoundUsernames)
    print("Amount of usernames found: " + str(FoundUsernamesCounter))
    print("Amount of usernames searched for: " + str(SearchedUsernamesCounter))
    print("Duplicate usernames: " + str(DuplicateUsernames))
    print("Time elasped: " + str(TimeElapsed) + " (Not including yield)")
    
    time.sleep(int(DelayTime))
    
    TimeElapsed = TimeElapsed + Decimal(DelayTime)
