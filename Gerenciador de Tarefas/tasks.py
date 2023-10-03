"""
criar lista
dar a permissão de olhar a lista
adicionar ou remover
"""
tasktodo = []
taskdone = []

def addtask():
    tarefa = input('Digite a tarefa a ser adicionada: ')
    tasktodo.append(tarefa)
    print('Tarefa adicionada!')
    
def concluirtask():
    if not tasktodo:
        print('Não existem tarefas pendentes.')
    else: 
        for i,tarefa in enumerate(tasktodo):
            print(f'{i+1}. {tarefa}')
        indice = int(input('Selecione qual das tarefas concluir.'))
        if 0 <= indice < len(tasktodo):
            taskdone = tasktodo.pop(indice)
            taskdone.append(taskdone)
            print(f"Tarefa '{taskdone}'concluida e movida para a lista de tarefas concluídas.")
        else:
            print('Indice inválido.')
            
def removetask():
    if not tasktodo:
        print('Não existem tarefas pendentes para remover.')
    else: 
        for i,tarefa in enumerate(tasktodo):
            print(f'{i+1}. {tarefa}')
        indice = int(input('Selecione qual das tarefas remover.'))
        if 0 <= indice < len(tasktodo):
            taskdone = tasktodo.pop(indice)
            print(f"Tarefa '{taskdone}'removida.")
        else:
            print('Indice inválido.')
            

while True:
    opcao = input('[1] - Adicionar\n[2] - Remover\n[3] - Concluir tarefa\n[4] - Tarefas Pendentes\n[5] - Tarefas concluídas\n[6] - Sair\n\nEscolha sua opção: ')
    
    if opcao == '1':
        addtask()
    elif opcao == '2':
        if not tasktodo:
            print('Não existem tarefas para remover.')
        else:
            removetask()
    elif opcao == '3':
        concluirtask()
    elif opcao == '4':
        if not tasktodo:
            print('Não existem tarefas pendentes.')
        else:
            for i, task in enumerate(tasktodo):
                print(f'{i + 1}. {task}')
    elif opcao == '5':
        if not taskdone:
            print('Não existem tarefas concluidas.')
        else:
            for i, task in enumerate(taskdone):
                print(f'{i + 1}. {task}')
    elif opcao == '6':
        print('Saindo...')
        break
    else:
        print('Opção inválida.')