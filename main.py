def sistema_gerenciamento_tarefas():
    tarefas = {}
    proximo_id = 1

    def adicionar_tarefa():
        nonlocal proximo_id
        descricao = input("Digite a descrição da nova tarefa: ")
        tarefas[proximo_id] = {"descricao": descricao, "status": "Pendente"}
        print(f"Tarefa '{descricao}' adicionada com ID {proximo_id}.")
        proximo_id += 1

    def listar_tarefas():
        if not tarefas:
            print("Nenhuma tarefa cadastrada.")
            return

        print("\n--- Lista de Tarefas ---")
        for id, tarefa in tarefas.items():
            print(f"ID: {id} | Descrição: {tarefa['descricao']} | Status: {tarefa['status']}")
        print("------------------------")

    def marcar_como_concluida():
        if not tarefas:
            print("Nenhuma tarefa para marcar como concluída.")
            return

        try:
            id_tarefa = int(input("Digite o ID da tarefa que deseja marcar como concluída: "))
        except ValueError:
            print("ID inválido. Por favor, digite um número.")
            return

        if id_tarefa not in tarefas:
            print(f"Tarefa com ID {id_tarefa} não encontrada.")
        elif tarefas[id_tarefa]["status"] == "Concluída":
            print(f"A tarefa com ID {id_tarefa} já está concluída.")
        else:
            tarefas[id_tarefa]["status"] = "Concluída"
            print(f"Tarefa com ID {id_tarefa} marcada como 'Concluída'.")

    while True:
        print("\n--- Menu Principal ---")
        print("1. Adicionar Nova Tarefa")
        print("2. Listar Todas as Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Sair")
        print("----------------------")

        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            adicionar_tarefa()
        elif opcao == '2':
            listar_tarefas()
        elif opcao == '3':
            marcar_como_concluida()
        elif opcao == '4':
            print("Saindo do sistema de gerenciamento de tarefas. Até mais!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

# Executa o sistema
if __name__ == "__main__":
    sistema_gerenciamento_tarefas()