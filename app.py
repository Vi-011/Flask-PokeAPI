from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index(): 
    response = requests.get("https://ghibliapi.vercel.app/species")
    species_data = response.json()


    species_lists = []
    for thing in species_data:
        url = thing['url']
        id = url.strip("/").split("/")[-1]
        classification = thing.get('classification', 'Unknown')
        name = thing.get('name', 'Unknown').capitalize()
        image = "https://banner2.cleanpng.com/20240413/qx/transparent-studio-ghibli-japanese-animation-hayao-miyazaki-my-character-from-my-neighbor-totoro-in-rain661ac59024a6e5.48137208.webp"

        species_lists.append({
            'name': name,
            'id': id,
            'classification': classification,
            'image': image
        })

    return render_template("index.html", species=species_lists)

@app.route("/species/<string:id>")
def species_detail(id):
    response = requests.get(f"https://ghibliapi.vercel.app/species/{id}")
    data = response.json()

    name = data.get('name', 'Unknown').capitalize()
    classification = data.get('classification', 'Unknown')
    image = "https://via.placeholder.com/150"

    return render_template("species.html", species={
        'name': name,
        'id': id,
        'classification': classification,
        'image': image
    })

if __name__ == '__main__':
    app.run(debug=True)