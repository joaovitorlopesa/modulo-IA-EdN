#Este código coleta dados de um usuário aleatório usando a API Random User Generator e imprime o nome, email e país do usuário.

import requests #Importa a biblioteca requests para fazer requisições HTTP

url = "https://randomuser.me/api" #URL da API Random User Generator

response = requests.get(url) #Faz uma requisição GET para a API

if response.status_code == 200: #Verifica se a requisição foi bem-sucedida (código 200)

    data = response.json() #Converte a resposta da API para JSON

    user = data['results'][0] #Acessa o primeiro resultado da lista de usuários
    name = f"{user['name']['title']} {user['name']['first']} {user['name']['last']}" #Formata o nome do usuário
    email = user['email'] #Acessa o email do usuário
    country = user ['location']['country'] #Acessa o país do usuário

    print(f"Nome: {name}")
    print(f"Email: {email}")
    print(f"País: {country}")
else: #Caso a requisição não tenha sido bem-sucedida, exibe o código de erro
    print("Erro de chamada à API: {response.status_code}")