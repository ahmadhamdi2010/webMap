import folium
import pandas


myMap = folium.Map(location=[38,-100],zoom_start=6, TileLayer="Mapbox Bright")
data = pandas.read_csv("Volcanoes_USA.txt")

dLat = list(data["LAT"])
dLon = list(data["LON"])
dLev = list(data["ELEV"])




FGV = folium.FeatureGroup(name="Volcanos")

for lt, ln, el in zip(dLat, dLon, dLev):

    if el > 3000 :
        pcolor = 'red'
    elif el > 2000 :
        pcolor = 'pink'
    else :
        pcolor = 'green'
        
    FGV.add_child(folium.Marker(location=[lt,ln],popup=str(el)+" m",icon=folium.Icon(color=pcolor) ))

myMap.add_child(FGV)
FGP = folium.FeatureGroup(name="Population")
FGP.add_child(folium.GeoJson(data=open("world.json", 'r', encoding='utf-8-sig').read(), style_function=lambda x : {'fillColor':'green' if x['properties']['POP2005']<10000000 else 'orange' if x['properties']['POP2005'] >10000000 else 'red '}))

myMap.add_child(FGP)
myMap.add_child(folium.LayerControl())
#myMap.add_child(folium.Marker(location=[38.2,-99.1],popup=" HI am a market",icon=folium.Icon(color='green') ))
myMap.save("Map1.html")