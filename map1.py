import folium
import pandas


myMap = folium.Map(location=[38,-100],zoom_start=6, TileLayer="Mapbox Bright")
data = pandas.read_csv("Volcanoes_USA.txt")

dLat = list(data["LAT"])
dLon = list(data["LON"])
dLev = list(data["ELEV"])

myFeatureGroup = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(dLat, dLon, dLev):

    if el > 3000 :
        pcolor = 'red'
    elif el > 2000 :
        pcolor = 'pink'
    else :
        pcolor = 'green'
        
    myFeatureGroup.add_child(folium.Marker(location=[lt,ln],popup=str(el)+" m",icon=folium.Icon(color=pcolor) ))

myMap.add_child(myFeatureGroup)

#myMap.add_child(folium.Marker(location=[38.2,-99.1],popup=" HI am a market",icon=folium.Icon(color='green') ))
myMap.save("Map1.html")