# Exercício - Lista de tarefas com desfazer e refazer
# Música para codar =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> lista de tarefas
# todo = ['fazer café'] -> Adicionar fazer café
# todo = ['fazer café', 'caminhar'] -> Adicionar caminhar
# desfazer = ['fazer café',] -> Refazer ['caminhar']
# desfazer = [] -> Refazer ['caminhar', 'fazer café']
# refazer = todo ['fazer café']
# refazer = todo ['fazer café', 'caminhar']
LISTAR = "listar"
DESFAZER = "desfazer"
REFAZER = "refazer"
SAIR = "sair"

todo = []
undo_redo = []


def list_todo(todo):
    print()
    print("TAREFAS")
    print(*todo, sep="\n")
    print()


while True:
    print("Comandos: listar, desfazer, refazer, sair")
    user_input = input("Digite uma tarefa ou comando: ")

    if user_input == LISTAR:
        list_todo(todo)
    elif user_input == DESFAZER:
        try:
            undo_redo.append(todo.pop())
            list_todo(todo)
        except IndexError:
            print("\nNada a dezfazer\n")
    elif user_input == REFAZER:
        try:
            todo.append(undo_redo.pop())
            list_todo(todo)
        except:
            print("\nNada a rezfazer\n")
    elif user_input == SAIR:
        print("Até mais!")
        break
    else:
        todo.append(user_input)
        list_todo(todo)
