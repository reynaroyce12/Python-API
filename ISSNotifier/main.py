from datetime import *
from smtplib import *
import time
import requests

MY_LAT = 10.786730
MY_LONG = 76.654793

my_email = 'gilfoylethegoldfoil@gmail.com'
to_address = 'reynaroyce.12@gmail.com'
password = 'testermail12!'


# ------------------------------- ISS POSITION API -------------------------
def iss_close():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()
    # print(data)

    iss_longitude = float(data['iss_position']['longitude'])
    iss_latitude = float(data['iss_position']['latitude'])

    if MY_LAT - 5 <= iss_latitude >= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude >= MY_LONG + 5:
        return True


# --------------------------------- SUNRISE AND SUNSET API ----------------------
def is_night_time():
    params = {
        "lat": 'MY_LAT',
        "lng": 'MY_LONG',
        "formatted": 0
    }
    response = requests.get(url='https://api.sunrise-sunset.org/json', params=params)
    response.raise_for_status()

    data = response.json()
    # print(data)
    sunrise = data['results']['sunrise'].split('T')[1].split(':')[0]
    sunset = data['results']['sunset'].split('T')[1].split(':')[0]
    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True


# --------------------------------- CHECKING ---------------------------------------

while True:
    time.sleep(60)                                                         # runs every 60 seconds to check
    if iss_close() and is_night_time():
        with SMTP('smtp.gmail.com') as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email,
                                to_addrs=to_address,
                                msg="Subject:ISS Overhead Notification 🛰️\n\n""The International space station is over "
                                    "your head today! Have a look at the sky. ")

