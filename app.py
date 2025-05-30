
from flask import Flask, render_template, url_for
import requests


app = Flask(__name__)


@app.route("/")
def index():
   response = requests.get("https://ghibliapi.vercel.app/species")
   species_data = response.json()


   image_map = {
       "Human": "images/Human.gif",
       "Cat": "images/cat.webp",
       "Spirit": "images/spirit.jpg",
       "God": "images/god.webp",
       "Totoro": "images/totoro.webp",
       "Dragon": "images/dragon.jpg",
       "Deer": "images/deer.webp",
   }


   species_lists = []
   for thing in species_data:
       url = thing['url']
       id = url.strip("/").split("/")[-1]
       name = thing.get('name', 'Unknown').capitalize()
       classification = thing.get('classification', 'Unknown')


       image_filename = image_map.get(name, "images/placeholder.jpg")
       image_url = url_for('static', filename=image_filename)


       species_lists.append({
           'name': name,
           'id': id,
           'classification': classification,
           'image': image_url
       })


   return render_template("index.html", species=species_lists)




@app.route("/species/<string:id>")
def species_detail(id):
   response = requests.get(f"https://ghibliapi.vercel.app/species/{id}")
   data = response.json()


   name = data.get('name', 'Unknown').capitalize()
   classification = data.get('classification', 'Unknown')
   eye_colors = data.get('eye_colors', 'Unknown')
   hair_colors = data.get('hair_colors', 'Unknown')
   people_links = data.get('people', [])
   film_links = data.get('films', [])


  
   people_names = []
   for person_url in people_links:
       person_response = requests.get(person_url)
       person_data = person_response.json()
       people_names.append(person_data.get('name', 'Unknown'))


  
   film_titles = []
   for film_url in film_links:
       film_response = requests.get(film_url)
       film_data = film_response.json()
       film_titles.append(film_data.get('title', 'Unknown'))


   image_map = {
       "Human": "images/Human.gif",
       "Cat": "images/cat.webp",
       "Spirit": "images/spirit.jpg",
       "God": "images/god.webp",
       "Totoro": "images/totoro.webp",
       "Dragon": "images/dragon.jpg",
       "Deer": "images/deer.webp"
   }


   image_filename = image_map.get(name, "images/placeholder.jpg")
   image_url = url_for('static', filename=image_filename)


   return render_template("species.html", species={
       'name': name,
       'id': id,
       'classification': classification,
       'eye_colors': eye_colors,
       'hair_colors': hair_colors,
       'people': people_names,
       'films': film_titles,
       'image': image_url
   })


if __name__ == '__main__':
   app.run(debug=True)
