import requests


def query_iss():
    """returns the iss (lat,lon) or null if there was an error"""

    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    # {'iss_position': {'latitude': '-37.0620', 'longitude': '169.4184'}, 'timestamp': 1659472283, 'message': 'success'}
    lat = response.json()["iss_position"]["latitude"]
    lon = response.json()["iss_position"]["longitude"]
    return float(lat), float(lon)


def query_sunset(lat, lon):
    """returns (sunrise, sunset) both are integer"""
    parameters = {
        "lat": lat,
        "lng": lon,
        "formatted": 0,
    }

    response = requests.get(url="http://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    # {'results': {'sunrise': '11:06:42 AM', 'sunset': '12:43:40 AM', 'solar_noon': '5:55:11 PM', 'day_length': '13:36:58', 'civil_twilight_begin': '10:42:00 AM', 'civil_twilight_end': '1:08:22 AM', 'nautical_twilight_begin': '10:10:50 AM', 'nautical_twilight_end': '1:39:32 AM', 'astronomical_twilight_begin': '9:38:11 AM', 'astronomical_twilight_end': '2:12:11 AM'}, 'status': 'OK'}
    sunrise = response.json()["results"]["sunrise"]
    sunset = response.json()["results"]["sunset"]

    sunrise_h = sunrise.split("T")[1].split(":")[0]
    sunset_h = sunset.split("T")[1].split(":")[0]
    # print(sunset_h)

    return int(sunrise_h), int(sunset_h)
