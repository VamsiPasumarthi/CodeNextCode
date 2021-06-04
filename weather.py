import requests
import json

from sense_emu import SenseHat

sense = SenseHat()

c = [0, 0, 0]  # clear
k = [0, 31, 58]  # dark blue
w = [255, 255, 255]  # white
y = [255, 255, 0]  # yellow
b = [0, 0, 255]  # blue

# icons to display on sensehat
sun = [c, c, c, c, y, c, c, c,
       c, y, c, y, y, c, y, c,
       c, c, y, y, y, y, c, c,
       y, y, y, y, y, y, y, c,
       c, y, y, y, y, y, y, y,
       c, c, y, y, y, y, c, c,
       c, y, c, y, y, c, y, c,
       c, c, c, y, c, c, c, c]

few = [c, c, c, c, c, c, c, c,
       c, c, c, c, c, y, y, y,
       c, c, c, c, w, y, y, y,
       c, c, c, w, w, w, y, y,
       c, w, w, w, w, w, w, c,
       c, w, w, w, w, w, w, c,
       c, c, c, c, c, c, c, c,
       c, c, c, c, c, c, c, c]

cloud = [c, c, c, c, c, c, c, c,
         c, c, c, c, c, c, c, c,
         c, c, c, c, w, c, c, c,
         c, c, c, w, w, w, c, c,
         c, w, w, w, w, w, w, c,
         c, w, w, w, w, w, w, c,
         c, c, c, c, c, c, c, c,
         c, c, c, c, c, c, c, c]

broken = [c, c, c, c, c, c, c, c,
          c, c, c, c, k, c, c, c,
          c, c, c, k, w, k, c, c,
          c, c, k, w, w, w, k, k,
          c, w, w, w, w, w, w, k,
          c, w, w, w, w, w, w, c,
          c, c, c, c, c, c, c, c,
          c, c, c, c, c, c, c, c]

shower = [c, c, c, c, k, c, c, c,
          c, c, c, k, w, k, c, c,
          c, c, k, w, w, w, k, k,
          c, w, w, w, w, w, w, k,
          c, w, w, w, w, w, w, c,
          c, b, c, b, c, b, c, c,
          b, c, b, c, b, c, c, c,
          c, c, c, c, c, c, c, c]

rain = [c, c, c, c, c, y, y, y,
        c, c, c, c, w, y, y, y,
        c, c, c, w, w, w, y, y,
        c, w, w, w, w, w, w, c,
        c, w, w, w, w, w, w, c,
        c, b, c, b, c, b, c, c,
        b, c, b, c, b, c, c, c,
        c, c, c, c, c, c, c, c]

thunder = [c, c, c, c, k, c, c, c,
           c, c, c, k, w, k, c, c,
           c, c, k, w, w, w, k, k,
           c, w, w, w, w, w, w, k,
           c, w, w, w, w, w, w, c,
           c, c, c, c, y, c, c, c,
           c, c, c, y, y, c, c, c,
           c, c, c, y, c, c, c, c]

snow = [c, c, c, c, c, c, c, c,
        c, c, c, c, w, c, c, c,
        c, c, c, w, w, w, c, c,
        c, w, w, w, w, w, w, c,
        c, w, w, w, w, w, w, c,
        c, c, c, c, c, c, c, c,
        c, w, c, w, c, w, c, c,
        c, c, c, c, c, c, c, c]

mist = [c, c, c, c, k, c, c, c,
        c, c, c, c, c, k, c, c,
        k, k, k, k, k, c, c, c,
        c, c, c, c, k, k, k, k,
        c, c, c, k, c, c, c, c,
        c, k, c, c, k, c, c, c,
        k, c, c, c, c, c, c, c,
        c, k, k, k, k, k, k, c]

display = {'01d': sun, '02d': few, '03d': cloud,
           '04d': broken, '09d': shower, '10d': rain,
           '11d': thunder, '13d': snow, '50d': mist,
           '01n': sun, '02n': few, '03n': cloud,
           '04n': broken, '09n': shower, '10n': rain,
           '11n': thunder, '13n': snow, '50n': mist}


def Weather():
    # preliminary variables
    KEY = '54b830a89457a56f842e4ec6c19865c1'

    # can change latitude and longitude (Keep in mind that South and West are negative)
    # currently set to Atlanta, Georgia
    lat = "33.7490"
    lon = "-84.3880"
    url = "https://api.openweathermap.org/data/2.5/onecall?lat=%s&lon=%s&appid=%s&units=imperial" % (lat, lon, KEY)

    # pinging url for weather info
    response = requests.get(url)
    data = json.loads(response.text)
    print(data)

    # accessing current forecast
    current_data = data["current"]["weather"]
    print(current_data)

    # finding weather code to display
    for entry in current_data:
        code = entry["icon"]

    # using dictionary to display on sensehat
    icon = display[code]
    sense.set_pixels(icon)


Weather()


