import requests
from datetime import datetime
import smtplib

my_email = "email"
my_password = "password"


def send_mail():
    with smtplib.SMTP("smtp mail server") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg="Subject:ISS Alert!!\n\n ISS is above you.Go outside before you miss it."
        )


parameters = {
    "lat": 18.520430,
    "lng": 73.856743,
    "time_format": 24
}


def check():

    response = requests.get("http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    iss_lat = data["iss_position"]["latitude"]
    iss_lng = data["iss_position"]["longitude"]
    #print(data)




    response = requests.get("https://api.sunrisesunset.io/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    #print(data)

    sunrise = data["results"]["sunrise"].split(":")[0]
    sunset = data["results"]["sunset"].split(":")[0]


    currnt_time = datetime.now().hour


    if(iss_lat == parameters["lat"] and iss_lng == parameters["lng"] and (currnt_time > sunset or currnt_time < sunrise)):
        send_mail()

check()