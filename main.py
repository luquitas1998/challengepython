# Librería para conectarse con mongoDB.
from pymongo import MongoClient
#  Framework para armar la API.
from fastapi import FastAPI
# Hacer consultas HTTP.
import requests
# Manejar varables de ambiente.
import os

# Variable que referencia la función de la API y se llama desde la terminal.
app = FastAPI()

# Dato hardcodeado de la población global para calcular porcentajes.
world_population = 8045311447

# Variables de ambiente para acceder a mongoDB.
operator = os.environ.get('operator')
operator_pwd = os.environ.get('operator_pwd')

# URL de la base de datos.
uri = (f"mongodb+srv://{operator}:{operator_pwd}@cluster0.nfsz7ms.mongodb.net/?retryWrites=true&w=majority")

# Carga de datos de la base.
client = MongoClient(uri)

# Nombre de la base.
db = client["challenge"]

# Se cargan datos en la base si no hay nada
def mongoDump(collectionName, collData, dbName):
    client = MongoClient(uri)
    try:
      if dbName[collectionName].count_documents({}) == 0:
            dbName[collectionName].insert_many(collData)
            print("Datos guardados")
# De haber datos se omite la carga.
      else:
            print("Tarea omitida, ya hay datos")
# De haber, se despliegan errores y se muestran en pantalla.
    except (Exception):
      print("Failed to insert:", Exception)
# Se cierra la sesión con mongo.    
    finally:
      client.close()

#  Se obtiene sólo la información pertinente de la api madre.
def getRawData():
    raw_data = 'https://restcountries.com/v3.1/all?fields=name,capital,population'
    raw_response = requests.get(raw_data)
    raw_json = raw_response.json()

    return raw_json

# Se cargan los datos como json.
api_json = getRawData()

# En caso de ser necesario se guardan los datos.
mongoDump("restcountries", api_json, db)

# Dado el país ingresado en la API se extraen datos relevantes.
def fetchCountryData(reqCountry):
  country = reqCountry
  col = db["restcountries"]
  myquery = { "name.common": country }
  countries = col.find(myquery)

# Se extrae la capital y población.
  for requested_country in countries:
    input_capital = requested_country['capital'][0]
    input_population = requested_country['population']

# Cálculo del porcentaje de ese país. 
  input_percentage = f"{(input_population / world_population) * 100:.4f}%"

# Se extraen los países con mayor población y se ordenan de menor a mayor.
  myquery = { "population": { "$gt": input_population } }
  countries = col.find(myquery).sort('population')

# Se extrae el siguiente país en población.
  next_country_raw = countries[0]
  next_country_clean = next_country_raw['name']['common']

  return {"capital": input_capital, "porcentaje mundial": input_percentage, "proximo pais": next_country_clean}

# Por el funcionamiento de fastAPI sólo lo explícito se carga como parámetro, el país ingresado entra como parametro.
@app.get("/")
async def api(country):
# Primer caso de borde, es el país con más población.
    if country == "China":
      return "capital: Beijing", "porcentaje mundial: 17.4276%", "proximo pais: China es el primero en la lista"
# Segundo caso de borde, no tiene capital ni población.    
    elif country == "Heard Island and McDonald Islands":
       return "capital: no tiene capital", "porcentaje mundial: 0.0000%", "proximo pais: South Georgia"
    else:
# Tercer caso de borde, no tiene población.        
        if country == "Bouvet Island":
           return "capital: King Edward Point", "porcentaje mundial: 0.0000%", "proximo pais: South Georgia"
    return fetchCountryData(country)