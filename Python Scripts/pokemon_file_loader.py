# -*- coding: utf-8 -*-
"""
Created on Wed May  1 22:19:11 2024

@author: DD-Z3ro
"""

import csv

with open('pokemon.csv') as pokemon_file:
    csv_reader = csv.reader(pokemon_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'column names are {", ".join(row)}')
            line_count +=1
        else:
            print(f'\t Pokemon name is {row[0]} with a height of {row[1]} and a base experience of {row[2]} ')
            line_count+=1
    print(f'processed{line_count} lines.')