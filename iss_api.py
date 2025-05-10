import json
import turtle
import urllib.request
import time
import webbrowser
import geocoder


# We get the current ISS data
url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())

# We save data to a text file using file function
file  = open("iss.txt", "w")
file.write("There are currently " + str(result["number"]) + " astronauts on the ISS: \n\n")
people = result["people"]

# We now save the crew names to the file iss.txt
for p in people:
    file.write(p['name'] + " - on board" + "\n")

# Here we get the current latitude and longitude
g = geocoder.ip('me')
file.write("\nYour current lat / long is: " + str(g.latlng))
file.close()

# Here we open the text file in the browser
webbrowser.open("iss.txt")

# Now we setup the world map in a turtle module
screen  = turtle.Screen()
screen.setup(1280, 720)
screen.setworldcoordinates(-180, -90, 180, 90)

# Load the world map image
screen.bgpic("images/map.gif")
screen.register_shape("images/iss.gif")
iss = turtle.Turle()
iss.shape("images/iss.gif")
iss.setheading(45)
iss.penup()

while True:
    # Get the current ISS position in real-time
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())

    # Extract the ISS location
    location = result["iss_position"]
    lat = lcoation['latitude']
    lon = location['longitude']

    # Output lon and lat to the terminal
    lat = float(lat)
    lon = float(lon)
    print("\nLatitude: " + str(lat))
    print("\nLongitude: " + str(lon))

    # Update the ISS location on the map
    iss.goto(lon, lat)

    # Refresh every 5 seconds
    time.sleep(5)