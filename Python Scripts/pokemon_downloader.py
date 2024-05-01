# -*- coding: utf-8 -*-
"""
Created on Wed May  1 21:32:07 2024

@author: DD-Z3ro
"""
import csv
import requests


def pokemon(pokemon):

    name = pokemon['name']

    pokemon_response = requests.get(pokemon['url'])
    if pokemon_response.status_code == 200:

        pokemon_data = pokemon_response.json()
        base_experience = pokemon_data['base_experience']
        height = pokemon_data['height']

        return [name, height, base_experience]


def get_pokemon():

    url = ('https://pokeapi.co/api/v2/pokemon/')

    params = {
        'param1': 'results'}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        results = data['results']
        return results


if __name__ == "__main__":
    data = get_pokemon()
    with open('pokemon.csv', mode='w', newline='') as pokemon_file:
        pokemon_writer = csv.writer(pokemon_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        pokemon_writer.writerow(['name', 'height', 'base_experience'])
        for p in data:
            row = pokemon(p)
            pokemon_writer.writerow(row)
        print("done!")
