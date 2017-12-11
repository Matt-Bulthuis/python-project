import json
import requests
import turtle

url = 'http://api.open-notify.org/astros.json'
response = requests.get(url)
result = json.loads(json.dumps(response.json()))
print('people in Space: ', result['number'])

people = result['people']
for p in people:
    print(p['name'])

url = 'http://api.open-notify.org/iss-now.json'
response = requests.get(url)
result = json.loads(json.dumps(response.json()))
print(result)

location = result ['iss_position']
lat = location['latitude']
lon = location['longitude']
print('latitude: ', lat)
print('longitude: ', lon)

screen = turtle.Screen()
screen.setup(720, 360)
screen.setworldcoordinates(-180, -90, 180, 90)
screen.bgpic('U:/Shared/GIS/StuData/MFBULT1217/PYTHON_PROJ/iss-project-resources/iss/map.gif')

screen.register_shape('U:/Shared/GIS/StuData/MFBULT1217/PYTHON_PROJ/iss-project-resources/iss/iss.gif')
iss = turtle.Turtle()
iss.shape('U:/Shared/GIS/StuData/MFBULT1217/PYTHON_PROJ/iss-project-resources/iss/iss.gif')
iss.setheading(90)

iss.penup()
iss.goto(lon, lat)

