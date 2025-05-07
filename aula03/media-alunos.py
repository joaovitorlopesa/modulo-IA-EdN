# Este código calcula a média das notas de uma turma de alunos. O professor pode inserir as notas um por um e, quando terminar, digitar 'fim' para encerrar a entrada de dados. O programa então calcula e exibe a média das notas inseridas.

notas = [] #Lista para armazenar as notas.
numero_de_alunos = 0 #Contador de alunos.

while True: #Loop para solicitar as notas dos alunos.
    entrada = input("Digite a nota do aluno (ou escreva 'fim' para encerrar): ") #Solicita a nota do aluno ou 'fim' para encerrar.

    if entrada.lower() == 'fim': #Verifica se o professor quer encerrar.
        break #Encerra o loop se o professor digitar 'fim'.

    try:
        nota = float(entrada) #Converte a entrada para float.

        if 0 <= nota <=10: #Verifica se a nota está dentro do intervalo válido.
            notas.append(nota)
            numero_de_alunos += 1
        else: #Exibe erro se a nota não estiver no intervalo válido.
            print("Nota inválida, Digite um valor de 0 a 10!")
    
    except ValueError: #Exibe erro para entradas inválidas.
        print("Entrada inválida. Por favor, escreva um número de 0 a 10 ou 'fim'.")

#Calcula e exibe a média

if numero_de_alunos > 0: #Verifica se há notas registradas.
    media = sum(notas) / numero_de_alunos #Calcula a média.
    print(f"A média da turma é: {media:.2f}") #Exibe a média com duas casas decimais.
    print(f"Total de alunos computados: {numero_de_alunos}") #Exibe o total de alunos.
else: #Se não houver notas registradas, exibe mensagem.
    print("Nenhuma nota foi registrada.")
#Fim do código.
