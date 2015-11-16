import json, urllib
from urllib.parse import urlencode
import urllib.request
import googlemaps
from bs4 import BeautifulSoup

class Directions:
    def __init__(self):
        self.startGeoCode = ""
        self.endGeoCode = ""




    def getStartFinish(self):
        start = input(str("Please enter sart adress:  "))
        finish = input(str("please enter your destination:  "))


        self.getDirections(start, finish)


    def getDirections(self, start, finish):
        url = 'http://maps.googleapis.com/maps/api/directions/json?%s' % urlencode((
            ('origin', start),
            ('destination', finish)))

        ur = urllib.request.urlopen(url).read()
        result = json.loads(ur.decode('utf-8'))
        self.loadDirections(result)

    def loadDirections(self, result):
        htmlFile = open("templates/index.html", "w")

        for i in range (0, len (result['routes'][0]['legs'][0]['steps'])):
            directionsTo = result['routes'][0]['legs'][0]['steps'][i]['html_instructions'] 
            htmlFile.write(directionsTo)

d = Directions()
d.getStartFinish()