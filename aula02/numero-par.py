#Este código verifica se o número digitado pelo usuário é par ou ímpar.

numero = int(input("Digite um número: ")) #Solicita ao usuário que digite um número e converte para inteiro.

if not (numero % 2 == 0): #Se o resto da divisão do número por 2 não for igual a 0, exibe que o número digitado é ímpar.
    print("O número digitado é ímpar") 
else: #Se o resto da divisão do número por 2 for igual a 0, exibe que o número digitado é par.
    print("O número digitado é par") 
#Fim do código.