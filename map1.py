import folium

myMap = folium.Map(location=[38,-100],zoom_start=6, TileLayer="Mapbox Bright")
myMap.save("Map1.html")