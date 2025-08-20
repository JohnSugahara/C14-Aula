import requests

def main():
    pokemon = input("Digite o seu Pokémon: ")
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
