import requests

world_population = 8045311447

country = input("Por favor elige un país: ")

input_api = f'https://restcountries.com/v3.1/name/{country}?fields=capital,population'

response_input = requests.get(input_api)

json_input = response_input.json()

input_data = json_input[0]

input_capital = input_data['capital'][0]
input_population = input_data['population']

print(f"Capital: {input_capital}")
print(f"Porcentaje mundial: {(input_population / world_population) * 100:.4f}%")

population_api = "https://restcountries.com/v3.1/all?fields=name,population"

response_population = requests.get(population_api)

json_population = response_population.json()

population_data = json_population

country_list_sorted = []

for each_country in population_data:
    other_name = each_country['name']['common']
    other_population = each_country['population']

    if other_population > input_population:
        country_list_sorted = country_list_sorted + [[other_name, other_population]]

country_list_sorted = sorted(country_list_sorted, key=lambda e: e[1])

print(country_list_sorted[0][0])