import requests

def get_pokemon_data(name):
    url = f'https://pokeapi.co/api/v2/pokemon/{name.lower()}'
    response = requests.get(url)

    if response.status_code == 200:
        return response.json()
    else:
        print("Error: Pokémon not found.")
        exit(1)

def display_abilities(pokemon_data):
    name = pokemon_data['name'].capitalize()
    abilities = [ability['ability']['name'].replace('-', ' ').title() for ability in pokemon_data['abilities']]

    print(f"Name: {name}\nAbilities:")
    for ability in abilities:
        print(f"- {ability}")

def main():
    pokemon_name = input("Enter the name of a Pokémon: ")
    pokemon_data = get_pokemon_data(pokemon_name)
    display_abilities(pokemon_data)

if __name__ == "__main__":
    main()
