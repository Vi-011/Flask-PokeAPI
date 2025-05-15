from flask import Flask, render_template
import requests 

app = Flask(__name__)

response = requests.get("https://ghibliapi.vercel.app/species")
species_lists = response.json()
print(species_lists)



@app.route("/")
def index(): 
    
  response = requests.get("https://ghibliapi.vercel.app/species")
  species_lists = response.json()
  print(species_lists)

  
  data = response.json()

    
  species_lists = []
      
  for thing in species_lists:
      movie = image_url 
      url = thing['url']
      parts = url.strip("/").split("/")
      id = parts[-1]
      classification = thing[classification]
          
      
      image_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{id}.png"
          
      species_lists.append({
          'name': species_lists['name'].capitalize(),
          'movie': movie,
          'id': id,
          'image': image_url,
          'classification': classification
          })
      
      return render_template("index.html", species=species)

@app.route("/species/<int:id>")
def species_detail(id):

    response = requests.get(f"https://ghibliapi.vercel.app/species{id}")
    data = response.json()
      
    types = [t['type']['name'] for t in data['types']]
    name = data.get('name').capitalize()
    image_url = f"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/{id}.png"
      

    return render_template("species.html", species={
        'name': name,
        'image': image_url,
        'id': id,       
        'types': types,
      })

if __name__ == '__main__':
      app.run(debug=True)

