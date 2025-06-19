from requests import get
from json import loads

def get_classes():
    response = get("https://www.dnd5eapi.co/api/2014/classes/")
    items = loads(response.text)
    list_classes = []
    for item in items["results"]:
        list_classes.append(item['name'])
    return list_classes

