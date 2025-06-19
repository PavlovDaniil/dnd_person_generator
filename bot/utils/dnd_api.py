from requests import get
from json import loads

def get_classes():
    response = get("https://www.dnd5eapi.co/api/2014/classes/")
    items = loads(response.text)
    list_classes = []
    for item in items["results"]:
        list_classes.append(item['name'])
    return list_classes

def get_races():
    response = get("https://www.dnd5eapi.co/api/2014/races/")
    items = loads(response.text)
    list_races = []
    for item in items["results"]:
        list_races.append(item['name'])
    return list_races