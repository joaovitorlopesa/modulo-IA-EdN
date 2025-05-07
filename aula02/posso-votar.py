#Este código verifica se a idade digitada pelo usuário, tem permissão ou não de votar.

idade = int(input("Digite sua idade: ")) #Solicita a idade ao usuário e converte para inteiro.
            
if idade >= 16: #Se a idade for maior ou igual a 16, exibe que o usuário pode votar.
    print("Você pode votar!")
else: #Se a idade for menor que 16, exibe que o usuário não pode votar.
    print("Você não pode votar!")
#Fim do código.