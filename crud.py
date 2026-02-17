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




print(usuarios)
print(adicionar_usuario(4,'jose','jose@gmail.com','1144','4354343','ativo'))
print(usuarios)




def buscar_usuario(id): #funçao read
    if id not in usuarios:
        return "Usuário não encontrado"
    
    return usuarios[id]



print(usuarios)
print(buscar_usuario(2))




def atualizar_senha(id, nova_senha): #funçao update
    if id not in  usuarios:
        return 'Erro'
    usuarios[id]['senha']= nova_senha
    return 'senha atualizada com sucesso'

print(usuarios)
print(atualizar_senha(4,'mangaratiba'))
print(usuarios)


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


print(usuarios)
print(deletar_usuario(2))
print(usuarios)

