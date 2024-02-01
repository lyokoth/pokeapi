from flask import Flask, jsonify

app = Flask(__name__)


pokemon_data = [
    {"id": 1, "name": "Sprigatito", "type": "Grass"},
    {"id" :2, "name": "Floragato", "type": "Grass"},
    {"id": 3, "name": "Meowscarada", "type": "Grass/Dark"}

]

@app.route("/pokemon", methods=["GET"])
def get_all_pokemon():
     return jsonify(pokemon_data)

@app.route("/pokemon/<int:pokemon_id>", methods=["GET"])
def get_pokemon_by_id(pokemon_id):
    pokemon = next((p for p in pokemon_data if p["id"] == pokemon_id), None)
    if pokemon_data:
        return jsonify(pokemon)
    else:
        return jsonify({"message": "Pokemon not found"}), 404
    
if __name__ == "__main__":
    app.run(debug=True)

    
