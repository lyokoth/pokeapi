## Pokémon API with SQLAlchemy

![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

This API is a RESTful web service that provides access to Pokémon data stored in a SQLite database using SQLAlchemy. It is a custom API for my front-end Pokedex project.


## Tech Stack

- Python
- SQLite
- SQLAlchemy
- Flask


## Endpoints

- The API exposes the following endpoints:

- `/pokemon` : Retrieves a list of all Pokemon species
- `/pokemon{id}`: Search a Pokemon by its ID
- `/pokemon{region}`: Search a Pokemon by the region it originates from.



## SQL

> A sample data table.

Table: pokemon
----------------------------------------
| Column          | Type    | Description |
----------------------------------------
| id              | Integer | Primary key, unique identifier for each Pokémon. |
| name            | String  | Name of the Pokémon species. |
| type            | String  | Primary type(s) of the Pokémon. |
| ability         | String  | Primary ability of the Pokémon. |
| hidden_ability  | String  | Hidden or secondary ability of the Pokémon. |
| height          | Integer | Height of the Pokémon in centimeters. |
| weight          | Integer | Weight of the Pokémon in kilograms. |
| hp              | Integer | Hit Points (HP) of the Pokémon. |
| attack          | Integer | Attack stat of the Pokémon. |
| defense         | Integer | Defense stat of the Pokémon. |
| sp_atk          | Integer | Special Attack stat of the Pokémon. |
| sp_def          | Integer | Special Defense stat of the Pokémon. |
| speed           | Integer | Speed stat of the Pokémon. |
| BST             | Integer | Base Stat Total (BST) of the Pokémon. |
| stage           | Integer | Evolution stage of the Pokémon (if applicable). |
| evolves_to      | String  | Pokémon species it evolves into (if applicable). |
| evolves_from    | String  | Pokémon species it evolves from (if applicable). |
| region          | String  | Region where the Pokémon species originates. |
----------------------------------------
