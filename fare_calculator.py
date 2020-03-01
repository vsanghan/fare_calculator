
import requests
import json
from datetime import datetime



def fare_calculator():

    origin = input("Enter the origin : ")
    destination = input("Enter the destination : ")
    mode = input("Enter the travel mode (rick or taxi or bus): ")
    if mode == 'bus':
        bus_type = input("Enter the type of bus(ac or nonac): ")
    key = '<Enter_Your_Key_Here>'
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=matric&origins="+ origin +"&destinations="+ destination +"&key="+key
    
    req = requests.get(url)
    j_req = json.loads(req.text)
    j_km = (j_req['rows'][0]['elements'][0]['distance']['text'])
    km = (float(j_km.split(' ')[0]))

    # To define time of the day
    st_now_time = (str(datetime.now())[11:-7])
    now_time = ((st_now_time.split(':')))
    # now_time = ["00","00","00"]
    if ((int(now_time[0])<=4 or int(now_time[0])>24) and int(now_time[1])<=59) and int(now_time[2])<=59:
        time = 'nightFare'
    else:
        time = 'dayFare'

    # Fare calculator    
    if mode == 'rick':
        if time == 'dayFare':
            fare = (int(round((11.33*km),0)))
        else:
            fare = (int(round((15.33*km),0)))
    elif mode == 'taxi':
        if time == 'dayFare':
            fare = (int(round((14.8*km),0))) 
        else:
            fare = (int(round((18.66*km),0)))
    elif mode == 'bus':
        if  bus_type == 'nonac':
            if km <= 5:
                fare = 5
            elif km > 5 and km <= 10:
                fare = 10
            elif km > 10 and km <= 15:
                fare = 15
            elif km > 15:
                fare = 20 
        elif bus_type == 'ac':
            if km <= 5:
                fare = 6
            elif km > 5 and km <= 10:
                fare = 13
            elif km > 10 and km <= 15:
                fare = 19
            elif km > 15:
                fare = 25

    if time == 'dayFare':
        return ("The Fare between "+ origin +' and '+ destination + ' is Rs.' + str(fare) + ' by '+ mode + '.')
    else:
        return ("The Fare between "+ origin +' and '+ destination + ' is Rs.' + str(fare) + ' (Night Charges) by '+ mode + '.')


print(fare_calculator())