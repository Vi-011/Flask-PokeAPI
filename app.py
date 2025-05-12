from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():

    response = requests.get("https://ghibliapi.vercel.app/species")
    data = response.json()
    species_list = data['results']
    
  
    species = []
    
    for thing in species_list:
       
        url = thing['url']
        parts = url.strip("/").split("/")
        id = parts[-1]  
        
        # Create an image URL using the Pokémon's ID
        image_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{id}.png"
        
        species.append({
            'name': species['name'].capitalize(),
            'id': id,
            'image': image_url
        })
    
    # Send the Pokémon list to the index.html page
    return render_template("index.html", species=species)

# New route: When a user clicks a Pokémon card, this page shows more details and a stats chart
@app.route("/pokemon/<int:id>")
def pokemon_detail(id):
    # Get detailed info for the Pokémon using its id
    response = requests.get(f"https://ghibliapi.vercel.app/species{id}")
    data = response.json()
    
    # Extract extra details like types, height, and weight
    types = [t['type']['name'] for t in data['types']]
    name = data.get('name').capitalize()
    image_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{id}.png"
    
    # Extract base stats for the chart (e.g., hp, attack, defense, etc.)
    stat_names = [stat['stat']['name'] for stat in data['stats']]
    stat_values = [stat['base_stat'] for stat in data['stats']]
    
    # Send all details to the pokemon.html template
    return render_template("pokemon.html", pokemon={
        'name': name,
        'id': id,
        'image': image_url,
        'types': types,
    })

if __name__ == '__main__':
    app.run(debug=True)j

