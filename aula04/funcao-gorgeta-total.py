#Este código calcula a gorjeta baseado no valor da conta e na porcentagem informada pelo usuário. Ele solicita o valor total da conta e a porcentagem da gorjeta, calcula o valor da gorjeta e exibe o resultado formatado.

def calculo_gorjeta(valor_conta, porcentagem_gorjeta): #Função para calcular a gorjeta

    gorjeta = valor_conta * (porcentagem_gorjeta / 100) #Calcula o valor da gorjeta

    return round(gorjeta, 2) #Arredonda o valor da gorjeta para duas casas decimais

def valor_total(valor_conta, valor_gorjeta): #Função para calcular o valor total a ser pago

    total = valor_conta + valor_gorjeta #Calcula o valor total a ser pago
    return total 

total_conta = float(input("Informa o total da conta: ")) #Solicita ao usuário o valor total da conta e converte para float
porcentagem = float(input("Informe a porcentagem da gorjeta: ")) #Chama a função calculo_gorjeta com o valor da conta e a porcentagem informada pelo usuário e armazena o resultado na variável valor_gorjeta

valor_gorjeta = calculo_gorjeta(total_conta, porcentagem) #Chama a função calculo_gorjeta com o valor da conta e a porcentagem informada pelo usuário e armazena o resultado na variável valor_gorjeta
total_a_pagar = valor_total (total_conta, valor_gorjeta) #Chama a função valor_total com o valor da conta e o valor da gorjeta e armazena o resultado na variável total_a_pagar

print(f"Para uma conta de {total_conta:.2f}, a gorjeta de {porcentagem}% tem o valor de R${valor_gorjeta}") #Exibe o valor da gorjeta formatado com duas casas decimais

print(f"O valor total da conta (conta + gorjeta) é: R${total_a_pagar:.2f}") #Exibe o valor total a ser pago formatado com duas casas decimais
