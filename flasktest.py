from flask import Flask, render_template
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
import coordinate
directions = coordinate.Directions()

app = Flask(__name__)
GoogleMaps(app)


@app.route('/')
def mapView():
    try:
        print()
        Gmap = Map(
        identifier = "Gmap",
        lat = directions.startLatPos, 
        lng = directions.startLngPos,
        style = "height:80%;width:100%;top:0;position:absolute;z-index:200;",
        zoom = '7',
        markers = {'http://maps.google.com/mapfiles/ms/icons/green-dot.png':[(directions.startLatPos, directions.startLngPos)],
                 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png':[(directions.finishLatPos, directions.finishLngPos)]}
        )
        return render_template('example.html', Gmap = Gmap)
    except Exception as e:
        print(e)
@app.route('/d')
def InsertDirections():
    try:

        return render_template('index.html')
    except Exception as e:
        print(e)
        print (type(e))


if __name__ == '__main__':
    directions = coordinate.Directions()
    directions.main()
    app.run()