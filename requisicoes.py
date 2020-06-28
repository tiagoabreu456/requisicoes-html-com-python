import requests

#consome api de cep's
#cep = input("Digite o cep a ser consultado: ")
def retorna_dados_cep(cep):
    response = requests.get("https://viacep.com.br/ws/{}/json/" .format(cep))

    print(response.status_code)
    dados_cep = response.json()

    print(dados_cep['bairro'])
    return dados_cep
#consome api pokeapi
def retorna_dados_pokemon(pokemon):
    response = requests.get("https://pokeapi.co/api/v2/pokemon/{}/" .format(pokemon))
    dados_pokemon = response.json
    return dados_pokemon
#retorna o html da pagina
def retorna_html(url):
    response = requests.get(url)
    return response.text 


if __name__ == "__main__":
    #retorna_dados_cep(cep)
    response = retorna_html("https://www.google.com")
    print(response)