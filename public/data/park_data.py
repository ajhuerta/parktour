import urllib.request, json
import csv
import os
import os.path
from datetime import datetime
import apikey as key # a file that stores api keys (should be modified accordingly)

# Set path
save_path = './CSV'
if not os.path.exists(save_path):
    os.makedirs(save_path)

# Set flags (set to true to construct CSV file)
build_Park = False
build_Activities = False
build_OpHours = False
build_Articles = False
build_Weather = False

if (build_Park):
    # Configure API request
    # Note limit parameter is arbitrary value greater than total number of NPS sites
    endpoint = "https://developer.nps.gov/api/v1/parks?limit=600" + "&api_key=" + key.npsKey
    HEADERS = {"Authorization":key.npsKey}
    req = urllib.request.Request(endpoint,headers=HEADERS)
    
    # Setup CSV file
    filename = 'Park.csv'
    completeName = os.path.join(save_path, filename)

    csvfile = open(completeName, 'w', newline='')
    fieldnames = ['ParkCode', 'ParkName', 'Location', 'EntranceFee']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Execute request and parse response
    response = urllib.request.urlopen(req).read()
    parkData = json.loads(response.decode('utf-8'))

    # Prepare and execute output
    for park in parkData["data"]:
        ParkCode = park["parkCode"]
        ParkName = park["fullName"]
        Location = park["latLong"]
        if (park["entranceFees"]):
            EntranceFee = park["entranceFees"][0]["cost"]
        else:
            EntranceFee = "0"
        # print(ParkName + " " + EntranceFee)
        writer.writerow({'ParkCode': ParkCode, 'ParkName': ParkName, 'Location': Location, 'EntranceFee':EntranceFee})
    csvfile.close()

if (build_Activities):
    # Configure API request
    # Note limit parameter is arbitrary value greater than total number of NPS sites
    endpoint = "https://developer.nps.gov/api/v1/parks?limit=600" + "&api_key=" + key.npsKey
    HEADERS = {"Authorization":key.npsKey}
    req = urllib.request.Request(endpoint,headers=HEADERS)
    
    # Setup CSV file
    filename = 'Activities.csv'
    completeName = os.path.join(save_path, filename)
    csvfile = open(completeName, 'w', newline='')
    fieldnames = ['ParkCode', 'ActivityID', 'ActivityName']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    
    # Execute request and parse response
    response = urllib.request.urlopen(req).read()
    parkData = json.loads(response.decode('utf-8'))
    # Prepare and execute output
    for park in parkData["data"]:
        ParkCode = park["parkCode"]
        if (park["activities"]):
            for act in park["activities"]:
                ActivityID = act["id"]
                ActivityName = act["name"]
                writer.writerow({'ParkCode': ParkCode, 'ActivityID': ActivityID, 'ActivityName': ActivityName})
        else:
            writer.writerow({'ParkCode': ParkCode, 'ActivityID': None, 'ActivityName': None})
    csvfile.close()

if (build_OpHours):
    # Configure API request
    # Note limit parameter is arbitrary value greater than total number of NPS sites
    endpoint = "https://developer.nps.gov/api/v1/parks?limit=600" + "&api_key=" + key.npsKey
    HEADERS = {"Authorization":key.npsKey}
    req = urllib.request.Request(endpoint,headers=HEADERS)
    
    # Setup CSV file
    filename = 'Operating_Hours.csv'
    completeName = os.path.join(save_path, filename)

    csvfile = open(completeName, 'w', newline='')
    fieldnames = ['ParkCode', 'Day', 'Hours']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Execute request and parse response
    response = urllib.request.urlopen(req).read()
    parkData = json.loads(response.decode('utf-8'))

    # Prepare and execute output
    for park in parkData["data"]:
        ParkCode = park["parkCode"]
        DayLst = ["sunday", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday"]
        for Day in DayLst:
            if (park["operatingHours"]):
                Hours = park["operatingHours"][0]["standardHours"][Day]
                # print(ParkCode + " " + Hours)
                writer.writerow({'ParkCode': ParkCode, 'Day': Day, 'Hours': Hours})
            # Should check this out (park with no operting hours info)
            else: 
                writer.writerow({'ParkCode': ParkCode, 'Day': None, 'Hours': None})
    csvfile.close()

if (build_Articles):
    # Configure API request
    # Note limit parameter is arbitrary value greater than total number of articles
    endpoint = "https://developer.nps.gov/api/v1/articles?limit=8000" + "&api_key=" + key.npsKey
    HEADERS = {"Authorization":key.npsKey}
    req = urllib.request.Request(endpoint,headers=HEADERS)
    
    # Setup CSV file
    filename = 'Articles.csv'
    completeName = os.path.join(save_path, filename)

    csvfile = open(completeName, 'w', newline='')
    fieldnames = ['ArticleID', 'ArticleTitle', 'URL', 'RelatedPark'] # RelatedPark in ParkCode
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Execute request and parse response
    response = urllib.request.urlopen(req).read()
    articleData = json.loads(response.decode('utf-8'))

    # Prepare and execute output
    for article in articleData["data"]:
        ArticleID = article["id"]
        ArticleTitle = article["title"]
        ArticleURL = article["url"]
        if article["relatedParks"]:
            for r_park in article["relatedParks"]:
                RelatedPark = r_park["parkCode"]
                writer.writerow({'ArticleID': ArticleID, 'ArticleTitle': ArticleTitle, 'URL': ArticleURL, 'RelatedPark':RelatedPark})
        # else:
        #     writer.writerow({'ArticleID': ArticleID, 'ArticleTitle': ArticleTitle, 'URL': ArticleURL, 'RelatedPark':None})
        
    csvfile.close()

if (build_Weather):
    # Configure API request
    # Note limit parameter is arbitrary value greater than total number of NPS sites
    p_endpoint = "https://developer.nps.gov/api/v1/parks?limit=600" + "&api_key=" + key.npsKey
    HEADERS = {"Authorization":key.npsKey}
    p_req = urllib.request.Request(p_endpoint,headers=HEADERS)
    # Execute request and parse response
    p_res = urllib.request.urlopen(p_req).read()
    parkData = json.loads(p_res.decode('utf-8'))

    # Setup CSV file
    filename = 'Weather.csv'
    completeName = os.path.join(save_path, filename)
    csvfile = open(completeName, 'w', newline='')
    fieldnames = ['ParkCode', 'Date', 'Temperature', 'Weather_Despcription']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Prepare and execute output
    for park in parkData["data"]:
        lat = int(float(park["latitude"]))
        lon = int(float(park["longitude"]))
        ParkCode = park["parkCode"]
        # print(ParkCode)
        # Configure API request
        excl_part = "current,minutely,hourly,alerts"
        w_endpoint = "https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&appid={key}".format(lat=lat, lon=lon, part=excl_part, key = key.openweatherKey)
        HEADERS = {"Authorization":key.openweatherKey}
        w_req = urllib.request.Request(w_endpoint,headers=HEADERS)
        # Execute request and parse response
        w_res = urllib.request.urlopen(w_req).read()
        weatherData = json.loads(w_res.decode('utf-8'))
        # write forecast output for each park
        for weather in weatherData["daily"]:
            # date = datetime.utcfromtimestamp(weather["dt"]).strftime('%Y-%m-%d')
            date = weather["dt"]
            temp = weather["temp"]["day"]
            # print(date)
            # print(temp)
            for _w in weather["weather"]:
                if (_w['description']):
                    des = _w["description"]
                else:
                    des = None
                # print(des)
                writer.writerow({'ParkCode': ParkCode, 'Date': date, 'Temperature': temp, 'Weather_Despcription': des})
    csvfile.close()