# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 23:23:19 2024

@author: DD-Z3ro
"""

import requests

pokemon = requests.get('https://pokeapi.co/api/v2/move')                        # we are hunting for the move : Pound
                                                                                

params = {                       
     'key1' : 'results'
     }                                                                           #got to here before having to look back at previous file
if pokemon.status_code == 200:
    move_data = pokemon.json()
    results = move_data['results']
    print(results)
    print("\n---Moves---")
    print("\nMove name :  " +results[0]['name'])
    print("\nlink : " + results[0]['url'])
    move_url = results[0]['url']
    
    split_move_url = move_url.split('/')
    print("\nno. : " + split_move_url[6])
    
    move_results = requests.get(move_url)
    if move_results.status_code == 200:
        move_info = move_results.json()
        #print(move_info)
        print("--accuracy--")
        print("\naccuracy value : " + str(move_info['accuracy']))
        print("\n--contest combos--")
        
        #print"--contest combos--"  TBC
        #print("\nnormal " + str(move_info['contest_type']['name']))
        
        print("\n--contest type--")
        print("name: " + str(move_info['contest_type']['name']))
        print("url: " + str(move_info['contest_type']['url']))
    
        print("\n--damage class--")
        print("name: " + str(move_info['damage_class']['name']))
        print("url: " +str(move_info['damage_class']['url']))
        
        print("\n--type--")
        print("name: " +(move_info)['type']['name'])
        print("url: " +(move_info)['type']['url'])