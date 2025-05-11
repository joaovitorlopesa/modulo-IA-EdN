#Este código calcula a idade de uma pessoa em dias, dado o ano de nascimento.

import datetime #Importa a biblioteca datetime para trabalhar com datas e horas

def calcular_idade_em_dias(ano_nascimento): #Função para calcular a idade em dias

    ano_atual = datetime.datetime.now().year #datetime.datetime.now() retorna a data e hora atual

    idade_anos = ano_atual - ano_nascimento #Calcula a idade em anos

    idade_dias = idade_anos * 365 #Calcula a idade em dias (aproximado)

    return idade_dias 

try: #Entrada de dados
    ano = int(input("Digite o ano de nascimento: "))

    if ano > datetime.datetime.now().year: #Verifica se o ano é maior que o ano atual
        print("Erro: Ainda não inventamos a máquina do tempo! Não pode colocar um ano no futuro")
    else:
        dias = calcular_idade_em_dias(ano) #Calcula a idade em dias
        print(f"Sua idade aproximada em dias é: {dias} dias.")

except ValueError: #Tratamento de erro, caso o usuário digite algo que não seja um número
    print("Erro: Digite um ano válido")