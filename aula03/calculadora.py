#Este código é uma calculadora simples que permite ao usuário realizar operações matemáticas básicas (adição, subtração, multiplicação e divisão) com dois números.

while True: #Loop para solicitar os números e a operação ao usuário.
    print("Bem-vindo à calculadora!") #Exibe mensagem de boas-vindas.
    try:
        num1 = float(input("Digite o primeiro número: ")) #Solicita o primeiro número ao usuário.
        num2 = float(input("Digite o segundo número : ")) #Solicita o segundo número ao usuário.
    
        operacao = input("Digite a operação (+ , - , * , / ): ") #Solicita a operação ao usuário.

        if operacao == "+": #Soma.
            resultado = num1 + num2
        elif operacao == "-": #Subtração.
            resultado = num1 - num2
        elif operacao == "*": #Multiplicação.
            resultado = num1 * num2
        elif operacao == "/": #Divisão.
            if num2 == 0: #Verifica se o divisor é zero, se for, exibe um erro.
                raise ZeroDivisionError("Pessoinha, você não pode dividir por zero.")
            resultado = num1 / num2 
        else: #Se a operação não for válida, exibe um erro.
            raise ValueError("Operação Inválida")
        
        print(f"Resultado: {resultado}") #Exibe o resultado da operação.
        break

    except ValueError as e: #Exibe erro para entradas inválidas.

        if str(e) == "Operação Inválida.": 
            print(e)
        else:
            print("Entrada Inválida, isso não é num número, por favor, digite novamente: ")
    
    except ZeroDivisionError as e: #Exibe erro para divisão por zero.
        print(e)
#Fim do código.