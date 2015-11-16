from flask import Flask, render_template
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map
import coordinate

app = Flask(__name__)
GoogleMaps(app)

    
@app.route('/')
def mapView():
     Gmap = Map(
         identifier = "Gmap",
         lat = 41.8500300, 
         lng = -87.6500500,
         style = "height:50%;width:100%;top:0;position:absolute;z-index:200;",
         zoom = '10',
         markers = [(41.8500300, -87.6500500)]
     )
     return render_template('example.html', Gmap = Gmap)
@app.route('/d')
def InsertDirections():
    try:
        
        return render_template('index.html')
    except Exception as e:
        print(e)
        print (type(e))


if __name__ == '__main__':
    app.run()