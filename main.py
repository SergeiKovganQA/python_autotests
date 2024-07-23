
import requests # type: ignore
URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '42a0f282026236b2c51265016eba7639'
HEADERS = {'Content-Type' : 'application/json',  'trainer_token': TOKEN}

#создание покемона
body = {

    "name": "пуж311",
    "photo": "https://dolnikov.ru/pokemons/albums/206.png"

}
response = requests.post(url = f'{URL}/pokemons', headers = HEADERS, json = body)
print(response.text)

#смена имени
body = {
    "pokemon_id": "28983",
    "name": "klefki",
    "photo": "https://dolnikov.ru/pokemons/albums/206.png"
}
response = requests.put(url = f'{URL}/pokemons', headers = HEADERS, json = body)

#поймать в покебол
body = {
    "pokemon_id": "28983",
}
response = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADERS, json = body)

print(response.text)





 