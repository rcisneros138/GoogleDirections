import json, urllib
from urllib.parse import urlencode
import urllib.request
# from googlemaps import Client as GoogleMaps
from bs4 import BeautifulSoup

class Directions:
    def __init__(self):
        self.startLatPos = "1"
        self.startLngPos = ""
        self.finishLatPos = ""
        self.finishLngPos = ""
        self.endGeoCode = ""
        self.start = ""
        self.finish = ""



    def getStartFinish(self):
        self.start = input(str("Please enter start adress:  "))
        self.finish = input(str("please enter your destination:  "))

    def geoCodeStart(self):
        startLocation = self.start.replace(' ', '+')
        
        geoURL = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s' % startLocation)
        response = urllib.request.urlopen(geoURL).read()
        result = json.loads(response.decode('utf-8'))

        self.startLatPos = (result['results'][0]['geometry']['location']['lat'])
        self.startLngPos = (result['results'][0]['geometry']['location']['lng'])

        print("done", self.startLatPos)


    def geoCodeFinish(self):
        finishLocation = self.finish.replace(' ', '+')

        geoURL = ('https://maps.googleapis.com/maps/api/geocode/json?address=%s' % finishLocation)
        response = urllib.request.urlopen(geoURL).read()
        result = json.loads(response.decode('utf-8'))

        self.finishLatPos = (result['results'][0]['geometry']['location']['lat'])
        self.finishLngPos = (result['results'][0]['geometry']['location']['lng'])

    def getDirections(self):
        url = 'http://maps.googleapis.com/maps/api/directions/json?%s' % urlencode((('origin', self.start),('destination', self.finish)))

        ur = urllib.request.urlopen(url).read()
        result = json.loads(ur.decode('utf-8'))
        self.loadDirections(result)


    def loadDirections(self, result):
        htmlFile = open("templates/index.html", "w")

        for i in range (0, len (result['routes'][0]['legs'][0]['steps'])):
            directionsTo = result['routes'][0]['legs'][0]['steps'][i]['html_instructions'] 
            htmlFile.write(directionsTo)

    def main(self):
        self.getStartFinish()
        self.geoCodeStart()
        self.geoCodeFinish()
        self.getDirections()

# d = Directions()
# d.main()