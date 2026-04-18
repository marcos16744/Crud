import json

def salvar(dados):
    with open('dados.json','w') as arquivo:
        json.dump(dados,arquivo)

def carregar():
    try:
        with open('dados.json','r') as arquivo:
            return json.load(arquivo)
    except FileNotFoundError:
        return {}
    


import json

def salvar (dados):
    with open('dados.json','w') as arquivo:
        json.dump(dados,arquivo)


        