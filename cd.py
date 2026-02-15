Cadastro_usarios={
    'carlos@gmail.com':{
        'Nome':'Carlos',
        'CPF':'1339394',
        'senha':'1234'
        },
        'jose@gmail.com':{
        'Nome':'jose',
        'CPF':'1338898',
        'senha':'1235'
        },
        'anaclara@gmail.com':
        {'Nome':'ana clara',
        'CPF':'34332432',
       'senha':'434243242'
       },}
                              
def autenticar_usario(email,senha):
    if email in Cadastro_usarios:
        usuario=Cadastro_usarios[email]
        
        if usuario['senha']==senha:
            return f'Login realizado com sucesso Bem vindo {usuario['Nome']}'
    
    return 'Nao foi possivel realizar o login'



while True:
    
    escolha=input('deseja verificar seu login?')
    if escolha =='sim':
        email=input('digite seu email')
        
        senha=input('digite sua senha:')
        print(autenticar_usario(email,senha))
   



                              
                              
                              
                              
                              
                              
                              
                              
                              
                              
                              