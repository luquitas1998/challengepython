import requests

world_pop = 8045311447

country = input("Por favor elige un país: ")

url = f'https://restcountries.com/v3.1/name/{country}?fields=capital,population'

response = requests.get(url)

json_data = response.json()

requested_info = json_data[0]

capital = requested_info['capital'][0]
population = requested_info['population']

print(f"Capital: {capital}")
print(f"Población: {(population / world_pop) * 100:.4f}")