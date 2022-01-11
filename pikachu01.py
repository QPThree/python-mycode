#!/usr/bin/python3

import requests
import pandas

# define base URL
POKEURL = "http://pokeapi.co/api/v2/pokemon/"

def main():

    # Make HTTP GET request using requests, and decode
    # JSON attachment as pythonic data structure
    # Augment the base URL with a limit parameter to 1000 results
    pokemon = requests.get(f"{POKEURL}?limit=1000")
    pokemon = pokemon.json()
    
  
    names = []
    # Loop through data, and print pokemon names
    for poke in pokemon["results"]:
        # Display the value associated with 'name'
        #print(poke["name"])
        print(poke.get("name"))
        names.append(poke["name"])
    pokemon_dict = {"Name": names}
    print(f"Total number of Pokemon returned: {len(pokemon['results'])}")
 ## export to excel with pandas
    # make a dataframe from our data
    pokemonDF = pandas.DataFrame(pokemon_dict)
    # export to MS Excel XLSX format
    # run the following to export to XLSX
    # python -m pip install openpyxl
    # index=False prevents the index from our dataframe from
    # being written into the data
    pokemonDF.to_json("pokemon/allpokemon.json")
if __name__ == "__main__":
    main()
