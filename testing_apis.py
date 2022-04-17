from random import randint, random
import pymongo
import time

CONNECTION_STRING = "mongodb://group6api:YXeNbRRXMlCbDuHPyCG10sQARbUllgR4tmazMeDu946ZagcBAWlHu9qAXCoRrjOiuFCaR8glsmYr5CM1v42RLg==@group6api.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@group6api@"
DB_NAME = "EuropeDB"


# Populate Tester collections with tester info randomly - email, region, country
def add_athletes_to_collections():

    db = client = pymongo.MongoClient(CONNECTION_STRING)
    db = client[DB_NAME]

    collection_prefix = ["NA", "EU", "AU", "AS"]
    regions = ["North America", "Europe", "Australia", "Asia"]
    countries = [['America','Canada'], ['France', 'Ireland', 'England'], ["Australia"], ['China', 'India', 'Japan']]



    random_names = ["conor", "ankana", "yuki", "aryan", "sedat", "john", "mark", "paul"]
    
    num_of_requests = 1

    while True: 


        random_day = randint(17,26)
        random_hour = randint(0,23)
        random_minute = randint(0,59)
        month = "04"
        year = "2022"
        day = ""
        minute = ""
        hour = ""

        if(random_day < 10):
            day = "0"+str(random_day)
        else:
            day = str(random_day)

        if(random_minute < 10):
            minute = "0"+str(random_minute)
        else:
            minute = str(random_minute)

        if(random_hour < 10):
            hour = "0"+str(random_hour)
        else:
            hour = str(random_hour)


        timestamp = time.mktime(time.strptime( day+"-"+month+"-"+year+" "+hour+":"+minute, '%d-%m-%Y %H:%M'))



        random_num = randint(0,3)
        random_country = 0
        random_name = randint(0,7)
        random_email = randint(0,42)

        if random_num == 1 or random_num == 3:
            random_country = randint(0,2)
        elif random_num == 0:
            random_country = randint(0,1)
        else:
            random_country = 0


        data = {"athelete_email": random_names[random_name]+str(random_email)+"@gmail.com", "region": regions[random_num], "location": "SLS", "country": countries[random_num][random_country], "date": day+"/"+month+"/"+year, "time": hour+":"+minute, "timestamp": timestamp, "city": "City in "+countries[random_num][random_country], "isScheduled": "false"}
        db[collection_prefix[random_num]+"-athletes"].insert_one(data).inserted_id

        print("Sent " + str(num_of_requests) + " requests")
        num_of_requests += 1




def main():
    add_athletes_to_collections()


if __name__ == '__main__':
    main()
