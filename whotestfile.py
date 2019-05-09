import bs4 as bs
import urllib.request
from pymongo import MongoClient

try: 
    conn = MongoClient() 
    print("Connected successfully!!!") 
except:   
    print("Could not connect to MongoDB")

db = conn.who
collection = db.who_database

for id in range (1,2385):
    try:
        print (id)
        fetchurl = "http://apps.who.int/gho/indicators/?id="+ str(id)
        source = urllib.request.urlopen(fetchurl).read()
        soup = bs.BeautifulSoup(source,'xml')

        

        for i in soup.find('Name'):
            print(i)
            nameofindicator = { 
            "name":i
            }
            recordofname = collection.insert_one(nameofindicator)



        for j in soup.find('Definition'):
            print(j)
            description ={
                "description": j
            }
            recordofdefinition = collection.insert_one(description)

        print('\n')
        print('\n')
    
    except:
        pass
