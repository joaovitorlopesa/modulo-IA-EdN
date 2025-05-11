#Este código calcula gorteja baseado no valor da conta e na porcentagem informada pelo usuário. Ele solicita o valor total da conta e a porcentagem da gorjeta, calcula o valor da gorjeta e exibe o resultado formatado.

def calculo_gorjeta(valor_conta, porcentagem_gorjeta): #Função para calcular a gorjeta

    gorjeta = valor_conta * (porcentagem_gorjeta / 100) #Calcula o valor da gorjeta

    return round(gorjeta, 2) #Arredonda o valor da gorjeta para duas casas decimais

total_conta = float(input("Informa o total da conta: ")) #Solicita ao usuário o valor total da conta e converte para float

porcentagem = float(input("Informe a porcentagem da gorjeta: ")) #Chama a função calculo_gorjeta com o valor da conta e a porcentagem informada pelo usuário e armazena o resultado na variável valor_gorjeta

valor_gorjeta = calculo_gorjeta(total_conta, porcentagem) #Chama a função calculo_gorjeta com o valor da conta e a porcentagem informada pelo usuário e armazena o resultado na variável valor_gorjeta

print(f"Para uma conta de {total_conta:.2f}, a gorjeta de {porcentagem}% tem o valor de R${valor_gorjeta}") #Exibe o valor da gorjeta formatado com duas casas decimais