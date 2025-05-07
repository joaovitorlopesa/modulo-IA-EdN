#Este código verifica se o dia da semana informado pelo usuário é um dia útil ou não.

dia = input("Digite o dia da semana: ").lower() #Solicita o dia da semana ao usuário e converte para minúsculas.

if dia == "sábado": #Se o dia for sábado, exibe que é dia de trabalho para alguns, mas não para o usuário.
    print("Hoje é dia de trabalho para alguns, mas para você, não!")
elif dia == "domingo": #Se o dia for domingo, exibe que é dia de descanso.
    print("Hoje é dia de descanso!")
else: #Se o dia não for sábado ou domingo, exibe que é dia útil.
    print("Você precisa trabalhar!")
#Fim do código.