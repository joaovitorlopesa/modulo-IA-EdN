#Este código conta quantos números pares e ímpares foram digitados pelo usuário. O usuário pode inserir números inteiros um por um e, quando terminar, digitar 'fim' para encerrar a entrada de dados. O programa então exibe a contagem de números pares e ímpares.

pares = 0 #Inicializa o contador de números pares
impares = 0 #Inicializa o contador de números ímpares

while True: #Loop infinito para permitir múltiplas entradas
    entrada = input("Digite um número inteiro (ou'fim' para encerrar): ")

    if entrada.lower() == 'fim': #Verifica se o usuário digitou 'fim' para encerrar
        print("Encerrado com sucesso!")
        break

    try: #Tenta converter a entrada em um número inteiro
        numero = int(entrada)

        if numero % 2 == 0: #Verifica se o número é par
            print(f"O número {numero} é par. ") 
            pares += 1 #Incrementa o contador de números pares
        else: #Caso contrário, o número é ímpar
            print(f"O número {numero} é impar.")
            impares += 1 #Incrementa o contador de números ímpares

    except ValueError: #Captura o erro caso a conversão falhe
        print("Erro: Digite apenas números inteiros")

print("\nResultado: ") #Exibe o resultado final
print(f"Números Pares: {pares}") #Exibe a contagem de números pares
print(f"Números Impares: {impares}") #Exibe a contagem de números ímpares