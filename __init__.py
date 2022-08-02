import os
import datetime as dt
import time

from dotenv import load_dotenv

import comm.rest
import comm.mail


def trigger_exception(status_code, msg):
    web = " see https://www.webfx.com/web-development/glossary/http-status-codes/"
    raise Exception(msg + ", http status code: " + str(status_code) + web)


def send_email(iss_latitude, iss_longitude):
    msg = "ISS is visible, check coordinates: " + str(iss_latitude) + ", " + str(iss_longitude)
    comm.mail.send_email(
        os.getenv('smtp'),
        int(os.getenv('smtp_port')),
        os.getenv('email'),
        os.getenv('password'),
        os.getenv('destination'),
        "ISS is visible!",
        msg)


if __name__ == '__main__':
    # load credentials from .env file
    load_dotenv()
    while True:

        my_lat = os.getenv('my_lat')
        my_lon = os.getenv('my_lon')
        my_lat_f = float(my_lat)
        my_lon_f = float(my_lon)
        time_now = dt.datetime.utcnow()
        now_h = time_now.hour

        (sunset, sunrise) = comm.rest.query_sunset(my_lat, my_lon)

        # if now_h >= sunset or now_h <= sunrise:
        iss_visible = False
        (lat, lon) = comm.rest.query_iss()
        if my_lat_f - 5 <= lat <= my_lat_f + 5:
            if my_lon_f - 5 <= lon <= my_lon_f + 5:
                iss_visible = True
                send_email(lat, lon)
        if iss_visible:
            print("ISS is visible")
        else:
            print("ISS is not visible")

        print("Will check again in an hour")
        time.sleep(3600)
