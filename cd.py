Cadastro_usarios={
    'carlos@gmail.com':{
        'nome':'Carlos',
        'cpf':'1339394',
        'senha':'1234'
        },
        'jose@gmail.com':{
        'nome':'jose',
        'cpf':'1338898',
        'senha':'1235'
        },
        'anaclara@gmail.com':
        {'nome':'ana clara',
        'cpf':'34332432',
       'senha':'434243242'
       },}
                              

def adicionar_usuario(email,nome,cpf,senha):
    if email in Cadastro_usarios:
        return 'Email já cadastrado'
    
    Cadastro_usarios[email]={
        'nome':nome,
        'cpf':cpf,
        'senha':senha
    }
    return 'usuarios cadastrado com sucesso'


def autenticar_usuario(email, senha):
    usuario =Cadastro_usarios.get(email)

    if usuario and usuario["senha"] == senha:
        return f"Login realizado! Bem vindo {usuario['nome']}"

    return "Email ou senha incorreta"














def deletar_usuario(email):
    if email in Cadastro_usarios:
        del Cadastro_usarios[email]
        return "Usuário deletado com sucesso"
    return "Usuário não encontrado"














while True:

    
    escolha=input('deseja verificar seu login ou o solicitar o cadastro ou deletar?')
    if escolha =='Login':
        email=input('digite seu email')
        
        senha=input('digite sua senha:')
        print(autenticar_usuario(email,senha))
   


    if escolha == 'cadastro':
        email = input('Email: ')
        nome = input('Nome: ')
        cpf = input('CPF: ')
        senha = input('Senha: ')

        print(adicionar_usuario(email, nome, cpf, senha))
       
        
    if escolha=='deletar':
        email=input('digite o email que deseja deletar:')
        print(deletar_usuario(email))


                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              