import requests

def main():
    digimon = input("Digite o seu Digimon: ")
    url = f"https://digi-api.com/api/v1/digimon/{digimon.lower()}"

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
        print(f"Erro: Digimon '{digimon}' não encontrado.")

if __name__ == "__main__":
    main()
