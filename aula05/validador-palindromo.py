#Este código verifica se uma palavra ou frase é um palíndromo, ou seja, se pode ser lida da mesma forma de trás para frente.

def validar_palindromo(texto): #Função para validar se o texto é um palíndromo

    texto_processado = '' #Variável para armazenar o texto processado

    for caractere in texto.lower(): #Converte o texto para minúsculas para facilitar a comparação
        if caractere.isalnum(): #Verifica se o caractere é alfanumérico
            texto_processado += caractere #Adiciona o caractere processado à variável texto_processado

    return texto_processado == texto_processado[::-1] #Compara o texto processado com sua versão invertida

texto = input("Digite uma palavra ou frase: ") #Entrada de dados
resultado = validar_palindromo(texto) #Chama a função validar_palindromo com o texto digitado pelo usuário

if resultado: #Verifica se o resultado é verdadeiro
    resposta = "Sim"
else: #Caso contrário, a resposta é "Não"
    resposta = "Não"

print(f"'{texto} é um palíndromo? {resposta}") #Exibe o resultado final