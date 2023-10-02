################################
#NB it works only for pc games## 
###############################


#Importing the modules
import json 
import requests
from random import randint


url = "https://www.freetogame.com/api/games?platform="

#making request to the website 
def Requesting(url) :
    platform = input("please insert your platform")
    return requests.get(url+platform).json()

# An empty list to store data on it 
list_game = []

# Making a function to get data from the site and making data into json form and append it to the empty list(list_game) and returning the list      
def GetData(response) :
    #iterating through the data of the site 
    for i in response :
        data = {
            "id" : i["id"],
            "title": i["title"],
            "thumbnail": i["thumbnail"],
            "game_url": i['game_url'],
            "release_date" : i["release_date"]
        }
        list_game.append(data)
    return list_game

#caliing the function inner function (geting data from request)  
data = GetData(Requesting(url))

# value = random position from 0 to the length of the data list 
value = randint(1,len(data))


#Voila this is your random game
print(list_game[value]["title"])
