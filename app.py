from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    my_dict = [{
    "id": "b5a92d0e-5fb4-43d4-ba60-c012135958e4",
    "name": "Spirit",
    "classification": "Spirit",
    "eye_colors": "Red",
    "hair_colors": "Light Orange",
    "url": "https://ghibliapi.vercel.app/species/b5a92d0e-5fb4-43d4-ba60-c012135958e4",
    "people": [
      "https://ghibliapi.vercel.app/people/ca568e87-4ce2-4afa-a6c5-51f4ae80a60b"
    ],
    "films": [
      "https://ghibliapi.vercel.app/films/0440483e-ca0e-4120-8c50-4c8cd9b965d6"
    ]
  },
  {
    "id": "f25fa661-3073-414d-968a-ab062e3065f7",
    "name": "God",
    "classification": "God",
    "eye_colors": "Brown",
    "hair_colors": "White",
    "url": "https://ghibliapi.vercel.app/species/f25fa661-3073-414d-968a-ab062e3065f7",
    "people": [
      "Moro"
    ],
    "films": [
      "https://ghibliapi.vercel.app/films/0440483e-ca0e-4120-8c50-4c8cd9b965d6"
    ]
  }]
    

    return render_template("index.html", thing_species = thing_species)
if __name__ == '__main__':
    app.run(debug=True)
    

response = requests.get("https://ghibliapi.vercel.app/species")
data = response.json()
species_list = data['results']
    
  
species = []
    
for thing in species_list:
    movie = image_url 
    url = thing['url']
    parts = url.strip("/").split("/")
    id = parts[-1]  
        
        # Create an image URL using the Pokémon's ID
    image_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{id}.png"
        
    species.append({
        'name': species['name'].capitalize(),
        'movie': movie,
        'id': id,
        'image': image_url
        })
    
    return render_template("index.html", species=species)

@app.route("/species/<int:id>")
def species_detail(id):
    # Get detailed info for the Pokémon using its id
    response = requests.get(f"https://ghibliapi.vercel.app/species{id}")
    data = response.json()
    
    # Extract extra details like types, height, and weight
    types = [t['type']['name'] for t in data['types']]
    name = data.get('name').capitalize()
    image_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{id}.png"
    

    stat_names = [stat['stat']['name'] for stat in data['stats']]
    stat_values = [stat['base_stat'] for stat in data['stats']]

    return render_template("species.html", species={
        'name': name,
        'image': image_url,
        'id': id,       
        'types': types,
    })

if __name__ == '__main__':
    app.run(debug=True)j

