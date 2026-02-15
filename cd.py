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
                              

def adicionar_usuario(email,nome,cpf,senha): #funçao creat
    if email in Cadastro_usarios:
        return 'Email já cadastrado'
    
    Cadastro_usarios[email]={
        'nome':nome,
        'cpf':cpf,
        'senha':senha
    }
    return 'usuarios cadastrado com sucesso'


def autenticar_usuario(email, senha): #funçao read
    usuario =Cadastro_usarios.get(email)

    if usuario and usuario["senha"] == senha:
        return f"Login realizado! Bem vindo {usuario['nome']}"

    return "Email ou senha incorreta"


def atualizar_usuario(email, **dados_para_atualizar):#funçao update

    usuario = Cadastro_usarios.get(email)

    if not usuario:
        return "Usuário não encontrado"

    usuario.update(dados_para_atualizar)

    return "Usuário atualizado com sucesso"








def deletar_usuario(email): #funçao delet
    if email in Cadastro_usarios:
        del Cadastro_usarios[email]
        return "Usuário deletado com sucesso"
    return "Usuário não encontrado"










while True:

    escolha = input('1-adicionar|2-login|3-atualizar |4-deletar | sair\n')

    if escolha == '1':
        email = input('Email: ')
        nome = input('Nome: ')
        cpf = input('CPF: ')
        senha = input('Senha: ')

        print(adicionar_usuario(email, nome, cpf, senha))

    elif escolha == '2':
        email = input('digite seu email: ')
        senha = input('digite sua senha: ')
        print(autenticar_usuario(email, senha))

    elif escolha == "3":
        email = input("Digite o email do usuário: ")

        novo_nome = input("Novo nome (Enter para manter): ")
        novo_cpf = input("Novo CPF (Enter para manter): ")
        nova_senha = input("Nova senha (Enter para manter): ")

        dados = {}

        if novo_nome:
            dados["nome"] = novo_nome
        if novo_cpf:
            dados["cpf"] = novo_cpf
        if nova_senha:
            dados["senha"] = nova_senha

        print(atualizar_usuario(email, **dados))
        print(Cadastro_usarios)

    elif escolha == '4':
        email = input('digite o email que deseja deletar: ')
        print(deletar_usuario(email))

    elif escolha == 'sair':
        print('fim do programa')
        break

    else:
        print('opção inválida')


                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              