# ISS Monitor
The ISS Monitor checks ISS public API every hour to verify if the ISS is visible from the location specified in the .env file. 
If the station is visible, this simple program sends an email to the destination specified in the .env file.

# .env file

```
    # smtp_sever used for transmission
    smtp = "smtp.gmail.com"
    smtp_port = 587
    # source email/user of the account used to send email
    email=
    # destination email
    destination=
    # app password of the application
    password=
    # Get your coordinates from https://www.latlong.net/
    my_lat=
    my_lon=
```

