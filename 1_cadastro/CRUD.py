usuarios = {}

usuarios[1] = {
    "id": '1',
    "nome": "Carlos",
    "email": "carlos@gmail.com",
    "senha": "1234",
    "cpf": "23434242",
    "ativo": True
}

usuarios[2]={
    'id':'2',
    'nome':'Augusto',
    'email':'Augusto',
    'senha':'323232',
    'cpf':'3232342',
    'ativo': True
}



def adicionar_usuario(id, nome, email, senha, cpf,ativo): #funçao creat
    if id  in usuarios:
        return 'ja esta cadastrado'
    
    usuarios[id]={
        'id':id,
        'nome':nome,
        'email':email,
        'senha':senha,
        'cpf':cpf,
        'ativo':ativo,
        } 
    return('usuario cadastrado com sucesso')







def buscar_usuario(id): #funçao read
    if id not in usuarios:
        return "Usuário não encontrado"
    
    return usuarios[id]






def atualizar_senha(id,nova_senha): #funçao update
    if id not in  usuarios:
        return 'Erro'
    usuarios[id]['senha']=nova_senha
    return 'senha atualizada com sucesso'



def atualizar_usuario(id, campo, novo_valor): #funçao update mais geral
    if id not in usuarios:
        return 'Usuário não encontrado'
    
    usuarios[id][campo] = novo_valor
    return 'Usuário atualizado com sucesso'





def deletar_usuario(id): #funçao delet
    if id in usuarios:
        del usuarios[id]
        return ' usuarios deletado'
    return 'usuario nao encontrado'


while True:
    print('1-adicionar|2-buscar|3-atualizar|4-deletar|5-sair')
    escolha=input('escolha:')
    if escolha=='1':
        id=int(input('digite o id'))
        nome=input('digite seu nome')
        email=input('digite seu email')
        senha=input('digite sua senha')
        cpf=input('digite seu cpf')
        ativo=input('digite seu status')
        print(adicionar_usuario(id, nome, email, senha, cpf,ativo))
    
    if escolha=='2':
        id=int(input('qual o seu id'))
        print(buscar_usuario(id))

    if escolha=='3':
        id =int(input('Digite o id: '))
        nova_senha=input('Digite a nova senha: ')
        print(atualizar_senha(id, nova_senha))

    if escolha=='4':
        id=int(input('Digite o id: '))
        print(deletar_usuario(id))

    if escolha=='5':
        break


