from requests import get
from json import loads

def main():
    getclasses()

def getclasses():
    response = get("https://www.dnd5eapi.co/api/2014/classes/")
    items = loads(response.text)
    for item in items["results"]:
        print(f"{item["name"]}")

if __name__ == "__main__":
    main()