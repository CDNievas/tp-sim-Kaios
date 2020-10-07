import requests
import urllib.parse
import json
from bs4 import BeautifulSoup
from Person import Person

def getFakePerson():
    
    personValues = getFakeData()

    name = personValues[1]["value"]
    street = personValues[5]["value"]
    city = personValues[6]["value"]
    state = personValues[7]["value"]

    if(state != "Buenos Aires"):
        raise PersonNotFromBsAsError("Persona no es de Bs. As.")

    coordLat, coordLong = getCoords(street,state)

    return Person(name, street, city, state, coordLat, coordLong)


def getFakeData():
    web = "https://www.fakeaddressgenerator.com/All_countries/address/country/Argentina"
    headers = {'User-Agent': 'Mozilla/5.0'}
    payload = {'country':'Argentina','abbr':'ar'}

    session = requests.Session()
    result = session.post(web,headers=headers,data=payload)

    html = result.text
    soup = BeautifulSoup(html, 'html.parser')

    return soup.find_all('input', {'type':'text'})


def getCoords(street, state):

    street = urllib.parse.quote(street) 

    web = "https://nominatim.openstreetmap.org/search.php?street={}&state={}&polygon_geojson=1&format=jsonv2".format(street,state)
    headers = {'User-Agent': 'Mozilla/5.0'}

    session = requests.Session()
    result = session.get(web,headers=headers)

    jObj = json.loads(result.text)

    try:
        place = jObj[0]
    except IndexError:
        raise AddressNotFoundError("No encontre esa direccion")

    return place["lat"],place["lon"]


class PersonNotFromBsAsError(Exception):
    pass

class AddressNotFoundError(Exception):
    pass



