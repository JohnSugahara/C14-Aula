#test_exemplo.py

import requests
import pytest



def main():
    pokemon = input("Digite o nome de um Pokémon: ")
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon.lower()}"

    resposta = requests.get(url)

    if resposta.status_code == 200:
        dados = resposta.json()
        print(f"\nNome: {dados['name'].title()}")
        print(f"Altura: {dados['height']} dm")
        print(f"Peso: {dados['weight']} hg")
        print("Habilidades:")
        for habilidade in dados["abilities"]:
            print(f" - {habilidade['ability']['name']}")
    else:
        print(f"Erro: Pokémon '{pokemon}' não encontrado.")

if __name__ == "__main__":
    main()

def test_pikachu_existe():
    pokemon_digitado = "pikachu"   # simula entrada do usuário
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_digitado.lower()}"
    resposta = requests.get(url)

    # 1. Verifica se a API respondeu OK
    assert resposta.status_code == 200  

    # 2. Verifica se o nome retornado é igual ao digitado
    dados = resposta.json()
    assert dados["name"] == pokemon_digitado
    
    
    
    
    
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#|||||||||||||||||||||  TESTES SEGUINDO DADOS DA API POKEMON |||||||||||||||||||||||||||
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||


    
#########################################################################################
#### PIKACHU ############################################################################
#########################################################################################

def test_pikachu_altura_existe():
    pokemon_digitado = "pikachu"   # simula entrada do usuário
    altura_esperada = 4
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_digitado.lower()}"
    resposta = requests.get(url)

    # 1. Verifica se a API respondeu OK
    assert resposta.status_code == 200  

    # 2. Verifica o peso do pokemon.
    dados = resposta.json()
    assert dados["height"] == altura_esperada
    
def test_pikachu_peso_existe():
    pokemon_digitado = "pikachu"   # simula entrada do usuário
    peso_esperado = 60
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_digitado.lower()}"
    resposta = requests.get(url)

    # 1. Verifica se a API respondeu OK
    assert resposta.status_code == 200  

    # 2. Verifica o peso do pokemon.
    dados = resposta.json()
    assert dados["weight"] == peso_esperado
    
def test_pikachu_habilidade_existe():
    pokemon_digitado = "pikachu"   # simula entrada do usuário
    habilidade_esperada = 'static'
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_digitado.lower()}"
    resposta = requests.get(url)

    # 1. Verifica se a API respondeu OK
    assert resposta.status_code == 200  

    # 2. Verifica as habilidades do pokemon.
    dados = resposta.json()
    for habilidade in dados["abilities"]:
        if not habilidade["is_hidden"]:
            assert habilidade['ability']['name'] == habilidade_esperada

def test_pikachu_habilidade_escondida_existe():
    pokemon_digitado = "pikachu"   # simula entrada do usuário
    habilidade_escondida_esperada = 'lightning-rod'
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_digitado.lower()}"
    resposta = requests.get(url)

    # 1. Verifica se a API respondeu OK
    assert resposta.status_code == 200  

    # 2. Verifica as habilidades escondidas do pokemon.
    dados = resposta.json()
    for habilidade in dados["abilities"]:
        if habilidade["is_hidden"]:
            assert habilidade['ability']['name'] == habilidade_escondida_esperada

#########################################################################################
#### CHARMANDER #########################################################################
#########################################################################################    

def test_charmander_altura_existe():
    pokemon_digitado = "charmander"   # simula entrada do usuário
    altura_esperada = 6
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_digitado.lower()}"
    resposta = requests.get(url)

    # 1. Verifica se a API respondeu OK
    assert resposta.status_code == 200  

    # 2. Verifica o peso do pokemon.
    dados = resposta.json()
    assert dados["height"] == altura_esperada
    
def test_charmander_peso_existe():
    pokemon_digitado = "charmander"   # simula entrada do usuário
    peso_esperado = 85
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_digitado.lower()}"
    resposta = requests.get(url)

    # 1. Verifica se a API respondeu OK
    assert resposta.status_code == 200  

    # 2. Verifica o peso do pokemon.
    dados = resposta.json()
    assert dados["weight"] == peso_esperado
    
def test_charmander_habilidade_existe():
    pokemon_digitado = "charmander"   # simula entrada do usuário
    habilidade_esperada = 'blaze'
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_digitado.lower()}"
    resposta = requests.get(url)

    # 1. Verifica se a API respondeu OK
    assert resposta.status_code == 200  

    # 2. Verifica as habilidades do pokemon.
    dados = resposta.json()
    for habilidade in dados["abilities"]:
        if not habilidade["is_hidden"]:
            assert habilidade['ability']['name'] == habilidade_esperada

def test_charmander_habilidade_escondida_existe():
    pokemon_digitado = "charmander"   # simula entrada do usuário
    habilidade_escondida_esperada = 'solar-power'
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_digitado.lower()}"
    resposta = requests.get(url)

    # 1. Verifica se a API respondeu OK
    assert resposta.status_code == 200  

    # 2. Verifica as habilidades escondidas do pokemon.
    dados = resposta.json()
    for habilidade in dados["abilities"]:
        if habilidade["is_hidden"]:
            assert habilidade['ability']['name'] == habilidade_escondida_esperada
            
            

#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#||||||||||||  TESTES SEGUINDO CM e KG POKEMON E ESCRITO IGNORANDO CS ||||||||||||||||||
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||

def test2_pikachu_altura_existe():
    pokemon_digitado = "pikachu"   # simula entrada do usuário
    altura_esperada = 40
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_digitado.lower()}"
    resposta = requests.get(url)

    # 1. Verifica se a API respondeu OK
    assert resposta.status_code == 200  

    # 2. Verifica o peso do pokemon.
    dados = resposta.json()
    assert dados["height"] == altura_esperada
    
def test2_pikachu_peso_existe():
    pokemon_digitado = "pikachu"   # simula entrada do usuário
    peso_esperado = 6
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_digitado.lower()}"
    resposta = requests.get(url)

    # 1. Verifica se a API respondeu OK
    assert resposta.status_code == 200  

    # 2. Verifica o peso do pokemon.
    dados = resposta.json()
    assert dados["weight"] == peso_esperado
    
def test2_pikachu_habilidade_existe():
    pokemon_digitado = "pikachu"   # simula entrada do usuário
    habilidade_esperada = 'Static'
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_digitado.lower()}"
    resposta = requests.get(url)

    # 1. Verifica se a API respondeu OK
    assert resposta.status_code == 200  

    # 2. Verifica as habilidades do pokemon.
    dados = resposta.json()
    for habilidade in dados["abilities"]:
        if not habilidade["is_hidden"]:
            assert habilidade['ability']['name'] == habilidade_esperada

def test2_pikachu_habilidade_escondida_existe():
    pokemon_digitado = "pikachu"   # simula entrada do usuário
    habilidade_escondida_esperada = 'Lightning Rod'
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_digitado.lower()}"
    resposta = requests.get(url)

    # 1. Verifica se a API respondeu OK
    assert resposta.status_code == 200  

    # 2. Verifica as habilidades escondidas do pokemon.
    dados = resposta.json()
    for habilidade in dados["abilities"]:
        if habilidade["is_hidden"]:
            assert habilidade['ability']['name'] == habilidade_escondida_esperada

#########################################################################################
#### CHARMANDER #########################################################################
#########################################################################################    

def test2_charmander_altura_existe():
    pokemon_digitado = "charmander"   # simula entrada do usuário
    altura_esperada = 60
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_digitado.lower()}"
    resposta = requests.get(url)

    # 1. Verifica se a API respondeu OK
    assert resposta.status_code == 200  

    # 2. Verifica o peso do pokemon.
    dados = resposta.json()
    assert dados["height"] == altura_esperada
    
def test2_charmander_peso_existe():
    pokemon_digitado = "charmander"   # simula entrada do usuário
    peso_esperado = 8.5
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_digitado.lower()}"
    resposta = requests.get(url)

    # 1. Verifica se a API respondeu OK
    assert resposta.status_code == 200  

    # 2. Verifica o peso do pokemon.
    dados = resposta.json()
    assert dados["weight"] == peso_esperado
    
def test2_charmander_habilidade_existe():
    pokemon_digitado = "charmander"   # simula entrada do usuário
    habilidade_esperada = 'Blaze'
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_digitado.lower()}"
    resposta = requests.get(url)

    # 1. Verifica se a API respondeu OK
    assert resposta.status_code == 200  

    # 2. Verifica as habilidades do pokemon.
    dados = resposta.json()
    for habilidade in dados["abilities"]:
        if not habilidade["is_hidden"]:
            assert habilidade['ability']['name'] == habilidade_esperada

def test2_charmander_habilidade_escondida_existe():
    pokemon_digitado = "charmander"   # simula entrada do usuário
    habilidade_escondida_esperada = 'Solar Power'
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_digitado.lower()}"
    resposta = requests.get(url)

    # 1. Verifica se a API respondeu OK
    assert resposta.status_code == 200  

    # 2. Verifica as habilidades escondidas do pokemon.
    dados = resposta.json()
    for habilidade in dados["abilities"]:
        if habilidade["is_hidden"]:
            assert habilidade['ability']['name'] == habilidade_escondida_esperada
            
            
