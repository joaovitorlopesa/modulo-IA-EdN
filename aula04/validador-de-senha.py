#Este código valida senhas de acordo com critérios específicos. O usuário pode inserir uma senha e, se ela não atender aos critérios, o programa solicitará uma nova senha. O processo continua até que uma senha válida seja inserida ou o usuário decida sair digitando 'sair'.

while True: #Loop infinito para permitir múltiplas tentativas de senha
    senha = input("Digite uma senha (ou 'sair' para encerrar)") #Solicita ao usuário que digite uma senha ou 'sair' para encerrar

    if senha.lower() == 'sair': #Verifica se o usuário digitou 'sair' para encerrar
        print("Programa encerrado")
        break #Encerra o loop se o usuário optar por sair

    tem_numero = False #Inicializa a variável para verificar se há números na senha

    for char in senha: #Loop para verificar cada caractere da senha
        if char.isdigit(): #Verifica se o caractere é um dígito
            tem_numero = True #Define que a senha contém um número
            break #Encerra o loop se um número for encontrado

    if len(senha) < 8:#Verifica se a senha tem menos de 8 caracteres
        print("Senha fraca: Ela deve ter ao menos 8 caracteres!")
    elif not tem_numero: #Verifica se a senha não contém números
        print("Senha fraca: Precisa ter ao menos um número!") 
    else: #Caso a senha atenda a todos os critérios
        print("Senha validada com sucesso!")
        break #Encerra o loop após validar a senha