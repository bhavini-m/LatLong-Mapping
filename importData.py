# -*- coding: utf-8 -*-
"""
Created on Sat May 27 19:29:49 2023

@author: Piyush
"""

import pandas as pd
import folium

df= pd.read_csv("LatLng.csv")
df.head()

width = df.longitude.max() - df.longitude.min()
height = df.latitude.max() - df.latitude.min()


latMean = df["latitude"].mean()
longMean = df["longitude"].mean()

# Creating Basemap
from branca.element import Figure
fig3=Figure(width,height)
m3=folium.Map(location=[latMean, longMean],tiles='cartodbpositron',zoom_start=11)
fig3.add_child(m3)

# Add points to the map

    
for index, row in df.iterrows():
    print(row['longitude'], row['latitude'])
    #folium.Marker([row['longitude'], row['latitude']]).add_to(m3)
    folium.Marker(location=[row['latitude'], row['longitude']],popup='Default popup Marker1',tooltip='Click here to see Popup').add_to(m3)

    
#folium.Marker(location=[latMean, longMean],popup='Default popup Marker1',tooltip='Click here to see Popup').add_to(m3)

m3
m3.save("mymap_new.html")

print ('done')

