import requests
import json
from flask import Flask, render_template, request

app = Flask(__name__)

SWAPI_URL = 'https://swapi.py4e.com/api/'

@app.route('/')
def homepage():
    # returns results page on main page load
    return render_template('results.html')

@app.route('/results', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        character_id = request.form.get("character_index")
        response_character = requests.get(f"{SWAPI_URL}people/{character_id}")
        # if character_id == 17 or character_id <= 0 or character_id > 80:
        #     return render_template("error.html")

        name = json.loads(response_character.content).get("name")
        height = json.loads(response_character.content).get("height")
        mass = json.loads(response_character.content).get("mass")
        hair_color = json.loads(response_character.content).get("hair_color")
        eye_color = json.loads(response_character.content).get("eye_color")
        homeworld = json.loads(response_character.content).get("homeworld")
        films = json.loads(response_character.content).get("films")

        context = {
            "name" : name,
            "height" : height,
            "mass" : mass,
            "hair_color" : hair_color,
            "eye_color" : eye_color,
            "homeworld" : homeworld,
            "films" : films
        }

        return render_template('results.html', **context)

    else:
        return render_template('results.html', **context)


if __name__ == '__main__':
    app.config['ENV'] = 'development'
    app.run(debug=True)
