def validarSenha(s):
    if len(s) < 8:
        return 'Senha inválida, muito curta'
    
    temNumero = False
    temMaiuscula = False
    simbolos = '!@#$%&'
    temSimbolo = False
    
    for c in s:
        if c == ' ':
            return ' Senha inválida, não pode conter espaços'
        if c >= '0' and c <= '9':
            temNumero = True
        if c >= 'A' and c <= 'Z':
            temMaiuscula = True
        if c in simbolos: 
            temSimbolo = True
            
    if not temNumero:
        return 'Senha inválida, deve conter pelo menos um número'
    if not temMaiuscula:
        return 'Senha inválida, deve conter pelo menos uma letra maiúscula'
    return 'Senha válida'
        
    #main
senha = input('Digite a senha: ')
r = validarSenha(senha)
print(r)