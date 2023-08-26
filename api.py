from pymongo import MongoClient
from pymongo.server_api import ServerApi
from fastapi import FastAPI
import requests
import json

world_population = 8045311447
app = FastAPI()
uri = "mongodb+srv://sade:smoothoperator@cluster0.nfsz7ms.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(uri)
db = client["challenge"]

def MongoDump(collectionName, collData, dbName):
    client = MongoClient(uri)
    try:
      if dbName[collectionName].count_documents({}) == 0:
            dbName[collectionName].insert_many(collData)
            print("Datos guardados")
      else:
            print("Tarea omitiida, ya hay datos")
    except (Exception):
      print("Failed to insert:", Exception)
    finally:
      client.close()

def get_raw_data():
    raw_data = 'https://restcountries.com/v3.1/all?fields=name,capital,population'
    raw_response = requests.get(raw_data)
    raw_json = raw_response.json()

    return raw_json

api_json = get_raw_data()
MongoDump("restcountries", api_json, db)

country = "Brazil"

col = db["restcountries"]
myquery = { "name.common": country }
countries = col.find(myquery)

for requested_country in countries:
  input_capital = requested_country['capital'][0]
  input_population = requested_country['population']

input_percentage = f"{(input_population / world_population) * 100:.4f}%"

myquery = { "population": { "$gt": input_population } }
countries = col.find(myquery).sort('population')

next_country_raw = countries[0]
next_country_clean = next_country_raw['name']['common']

print(input_capital)
print(input_percentage)
print(next_country_clean)

#@app.get("/")
#async def buscar(country):
#    return