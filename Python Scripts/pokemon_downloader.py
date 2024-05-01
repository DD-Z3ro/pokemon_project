# -*- coding: utf-8 -*-
"""
Created on Wed May  1 21:32:07 2024

@author: DD-Z3ro
"""
import csv
import requests

def pokemon(pokemon):
    
        #print("name: " + pokemon['name'])
        #print("link: " + pokemon['url'])
        
        name = pokemon['name']
        
        pokemon_response = requests.get(pokemon['url'])
        if pokemon_response.status_code == 200:
            pokemon_data = pokemon_response.json()
            #print("base experience: " + str( pokemon_data['base_experience']))
            #print("\nAbilities:")
            #for ability in pokemon_data['abilities']:
            #    print("- " + ability['ability']['name'])
           # print("moves: ")
          #  for move in pokemon_data['moves']:
           #     print("\n- " + move['move']['name']) # create github and split the links provided from the moves and pull out the number and add more data
           #     move_url = move['move']['url']
                
            # --    NEW CODE BELOW -- #
            
                #split_move_url = move_url.split('/') # using the split function will split the url into sections, the target was number 6 in the list
                #print("- " + split_move_url[6])            # then in print using that number to print out the variable with that numbers
                #print("link: " + move_url)
            #print("\nStats:")
            #for stats in pokemon_data['stats']:
                #char_stats = stats['base_stat']['url']
                #print(char_stats)                                             <--- may be useless
                #print("\n stat: " + str( stats['stat']['name']))               # using string to get the stats name and values of those stats
                #print(" value: " + str( stats['base_stat']))                    # put together in a readable form
            #print("\nGame versions: \n")
            
            #for game_indices in pokemon_data['game_indices']:
                #print("Pokemon " + str( game_indices['version']['name']))
            #print("\nLocation area encounters:")
            #print("link: " + pokemon_data['location_area_encounters'])       #is there a way to peak into this link??
                                                                                #could be a bit much information to take out
                
            base_experience = pokemon_data['base_experience']
            height = pokemon_data['height']
            #print("height: " + str( pokemon_data['height']))
            #print("")
            
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
        with open('pokemon.csv', mode = 'w', newline='') as pokemon_file:
            pokemon_writer = csv.writer(pokemon_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            pokemon_writer.writerow(['name', 'height', 'base_experience'])
            for p in data:
                row = pokemon(p) 
                pokemon_writer.writerow(row)
            print("done!")