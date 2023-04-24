import folium

myMap = folium.Map(location=[38,-100],zoom_start=6, TileLayer="Mapbox Bright")

myFeatureGroup = folium.FeatureGroup(name="My Map")
myFeatureGroup.add_child(folium.Marker(location=[38.2,-99.1],popup=" HI am a market",icon=folium.Icon(color='green') ))
myMap.add_child(myFeatureGroup)

#myMap.add_child(folium.Marker(location=[38.2,-99.1],popup=" HI am a market",icon=folium.Icon(color='green') ))
myMap.save("Map1.html")