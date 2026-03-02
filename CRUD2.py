usuarios={}

usuarios[1]={
    'id':'1',
    'nome':'marcos',
    'email':'marcos@gmail.com',
    'idade':'19'
}


usuarios[2]={
    'id':'2',
    'nome':'rodrigo',
    'email':'rodrigo@gmail.com',
    'idade':'24',
}

def adicionar_usuario(id,nome, email, idade): #creat
    if id in usuarios:
        return 'Erro usuario ja cadastrado'
    usuarios[id]={
        'id':id,
        'nome':nome,
        'email':email,
        'idade':idade,
    }
    return 'usuarios cadastrado com sucesso'




def ler_email(id,email_digitado):#funçao read 
    if id not in usuarios:
        return 'ERRO email nao existe'
    if usuarios[id]['email']==email_digitado:
        return 'email correto'
    else:
        return 'email errado'
        
    





def atualizar_email(id,novo_email):#update
    if id not in usuarios:
        return ' usuario nao encontrado'
    usuarios[id]['email']=novo_email
    return 'atualizado com sucesso'
 
    




def atualizar_geral(id,campo,novo_valor):#update generica
    if id not in usuarios:
        return 'usuario nao existente'
    if campo not in usuarios[id]:
        return 'campo nao encontrado'
    usuarios[id][campo]=novo_valor
    return 'atualizaçao feita com sucesso'




def deletar_usuario(id):# delet
    if id not in usuarios:
        return 'usuario nao cadastrado'
    del usuarios[id]
    return ' usuario apagado com suceso'

