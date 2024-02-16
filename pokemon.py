import json

with open('pokemon.json') as user_file:
  pokemon_json = json.load(user_file)

print(pokemon_json)


