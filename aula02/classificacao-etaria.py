#Este código classifica a idade de uma pessoa em diferentes categorias etárias.

idade = int(input("Digite sua idade: ")) #Solicita a idade do usuário.

if idade >= 65: #Verifica se a idade é maior ou igual a 65, se for, exibe que a pessoa é idosa.
    print("Você é idoso")
elif idade >= 18: #Verifica se a idade é maior ou igual a 18, se for, exibe que a pessoa é adulta.
    print("Você é adulto")
elif idade >= 12: #Verifica se a idade é maior ou igual a 12, se for, exibe que a pessoa é adolescente.
    print("Você é adolescente")
elif idade >= 3: #Verifica se a idade é maior ou igual a 3, se for, exibe que a pessoa é criança.
    print("Você é criança")
else: #Se não for nenhuma das opções acima, exibe que a pessoa é bebê.
    print("Você é bebê")
# Fim do código.