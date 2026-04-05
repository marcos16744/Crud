usuarios={
        1:{'nome':'vivian',
       'email':'vivian@gmail.com',
       'senha':'1152',
       'celular':'11937405541',
       },
       2:{'nome':'marcos',
       'email':'marcos@gmail.com',
        'senha':'1153',
        'celular':'55983754'
       },
       3:{'nome':'bernardo',
          'email':'bernardo@gmail.com',
            'senha':'1154',
            'celular':'55889748'
          },
        4:{'nome':'jonatan',
           'email':'jonatan@gmail.com',
           'senha':'1155',
            'celular':'9934897'
           },}


def cadastra_usuario(nome, email,senha ,celular):
    novo_id=max(usuarios.keys())+1


    usuarios[novo_id]={
        'nome':nome,
        'email':email,
        'senha':senha,
        'celular':celular
    }

    return'usuario cadastrado com sucesso'


def verificar_login(email_digitado,senha_digitada):
    for id_usuarios,dados in usuarios.items():
        if dados['email']==email_digitado and dados['senha']== senha_digitada:
            return f'login realizado!Bem vindo {dados["nome"]}'

    return 'Email, ou senha incorreta'


def buscar_email(email):
    for dados in usuarios.values():
        if dados['email']==email:
            return dados
    return None



def deletar_usuario(email):
    for id_usuario, dados in usuarios.items():
        if dados['email']==email:
            del usuarios[id_usuario]
            return 'Usuario  deletado com sucesso'
    return 'Usuario nao encontrado'



while True:
    print('1-Login')
    print('2-Cadastro')
    print('3-sair')

    opçao=input('Escolha')

    if opçao=='1':
        email=input('Email:')
        senha=input('Senha:')
        print(verificar_login(email,senha))

    elif opçao=='2':
        nome=input('Nome:')
        email=input('Email:')
        senha=input('Senha')
        celular=input('Celular:')
        print(cadastra_usuario(nome,email,senha,celular))

    elif opçao=='3':
        break
    