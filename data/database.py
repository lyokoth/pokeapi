import json
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData

# Create a database engine
engine = create_engine("sqlite:///kantopokemon.db", echo=True)

metadata = MetaData()


# Create a table
pokemon_table = Table(
    "pokemon",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("type", String),
    Column("abilities", String),
    Column("hidden_ability", String),
    Column("height", Integer),
    Column("weight", Integer),
    Column("hp", Integer),
    Column("attack", Integer),
    Column("defense", Integer),
    Column("sp_atk", Integer),
    Column("sp_def", Integer),
    Column("speed", Integer),
    Column("BST", Integer),
    Column("stage", Integer),
    Column("evolves_to", String),
    Column("evolves_from", String),
    Column("region", String)

)

metadata.create_all(engine)

# Insert data into the table
with open('kanto_pokemon_data.json') as f:
    pokemon_data = json.load(f)


# Connect to the database
    with engine.connect() as connection:
     for pokemon in pokemon_data["Kanto"]:
        insert_statement = pokemon_table.insert().values(
            id=pokemon["id"],
            name=pokemon["name"],
            type=", ".join(pokemon["type"]),
            ability=pokemon["abilities"][0],  # Assuming the first ability is the primary ability
            hidden_ability=pokemon["hidden_ability"],
            height=pokemon["height"],
            weight=pokemon["weight"],
            hp=pokemon["stats"]["hp"],
            attack=pokemon["stats"]["attack"],
            defense=pokemon["stats"]["defense"],
            sp_atk=pokemon["stats"]["sp_atk"],
            sp_def=pokemon["stats"]["sp_def"],
            speed=pokemon["stats"]["speed"],
            BST=pokemon["stats"]["BST"],
            stage=pokemon["evolution"]["stage"],
            evolves_to=pokemon["evolution"]["evolves_to"],
            evolves_from=pokemon["evolution"]["evolves_from"],
            region="Kanto"
        )
        connection.execute(insert_statement)



# Query the database
# Example: result = connection.execute(select([pokemon]))
# Example: for row in result:
# Example:     print(row)

