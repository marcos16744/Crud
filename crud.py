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


def adicionar_usuario(id, nome, email, senha, cpf,ativo):
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






#para confirmar se esta funcionado a funçao usa um while True perguntando cada variavel e depois da o print da funçao e os parametros
# ou para confirmar da o print da funçao e ao inves de colocar os parametros , coloca o resultado que voce ja quiser usa string para nome , se ano usar ele interpreta como variavel
#mas voce precisa colocar  um return  na funçao para ver se deu certo se colocar um return que 'vai dar errado' ( fazendo parte da estrutura da funçao) , se 'estiver certo ' ele nao vai aparecer ou entao dar o print do dicinario para ver se ele foi adicionado


    
print(adicionar_usuario(
    3,
    "Bruna marquezine",
    "bruna@gmail.com",
    "1234",
    "999999999",
    True
))

print(usuarios)

# while True:
#     id=input('qual o id:')
#     nome=input('qual o nome:')
#     email=input('qual o email:')
#     senha=input('qual a senha:')
#     cpf=input('qual o cpf:')
#     ativo=input('qual o estado:')

#     print(adicionar_usuario(id, nome, email, senha, cpf,ativo))
#     print(usuarios)


