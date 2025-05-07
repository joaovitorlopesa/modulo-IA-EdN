#Este código calcula o IMC (Índice de Massa Corporal) de uma pessoa com base na sua altura e peso.

altura_m = float(input("Digite a sua altura em centímetros: ")) #Lê a altura em centímetros.
peso = float(input("Digite o seu peso em quilogramas: ")) #Lê o peso em quilogramas.

altura_cm = (altura_m / 100) #Converte a altura de centímetros para metros.

imc = peso / (altura_cm ** 2) #Calcula o IMC usando a fórmula peso / altura².

print(f"Seu IMC é {imc:.2f}") #Exibe o IMC com duas casas decimais.

if imc < 18.5: #Verifica se o IMC é menor que 18.5, se o IMC for menor que 18.5, exibe que a pessoa está abaixo do peso.
    print("Você está abaixo do peso.")
elif imc < 25: #Verifica se o IMC é menor que 25, se o IMC for menor que 25, exibe que a pessoa está com o peso normal.
    print("Você está com o peso normal.")
elif imc < 30: #Verifica se o IMC é menor que 30, se o IMC for menor que 30, exibe que a pessoa está com sobrepeso.
    print("Você está com sobrepeso.")
else: #Se o IMC for maior ou igual a 30, exibe que a pessoa está acima do peso.
    print("Você está acima do peso.")
#Fim do código.