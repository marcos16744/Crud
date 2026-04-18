tarefas={}

tarefas[1]={
    'titulo':'despertador',
    'descriçao':'despertador',
    'status':'concluida',
    'data_de_criacao':'22 fevereiro'
}


tarefas[2]={
    'titulo':'faculdade',
    'descriçao':'despertador',
    'status':'concluida',
    'data_de_criacao':'22 fevereiro'
}


def adicionar(id, titulo,descriçao, status, data_de_criacao): #creat
    if id in tarefas:
        return 'ja existe essa tarefa'
    tarefas[id]={
        'titulo':titulo,
        'descriçao':descriçao,
        'status':status,
        'data_de_criacao':data_de_criacao
    }
    return 'usuario cadastrado com sucesso'




def mostrar_tarefa(id):#funçao read
    if id not in tarefas:
        return'nao existe'
    
    return tarefas[id]


def mostrar_data(id):#funçao read
    if id not in tarefas:
        return ' email nao cadastrado'
    return tarefas[id]['data_de_criacao']




def atualizar_tarefa(id,campo,novo_valor):#update
    if id not in tarefas:
        return ' nao encontrei a tarefa'
    tarefas[id][campo]=novo_valor
    return 'usuario atualizado com sucesso'


def deletar(id):#delet
    if id in tarefas:
        del tarefas[id]
        return 'tarefa apagada com sucesso'
    return ' tarefa nao apagada'





