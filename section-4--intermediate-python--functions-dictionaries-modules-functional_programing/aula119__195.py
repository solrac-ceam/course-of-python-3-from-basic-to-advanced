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
import os

todo = []
undo_redo = []


def list_todo(todo):
    print()
    print("TAREFAS")
    print(*todo, sep="\n")
    print()


def undo(todo, undo_redo):
    try:
        undo_redo.append(todo.pop())
        list_todo(todo)
    except IndexError:
        print("\nNada a dezfazer\n")


def redo(todo, undo_redo):
    try:
        todo.append(undo_redo.pop())
        list_todo(todo)
    except:
        print("\nNada a rezfazer\n")


def add_task(todo, user_input):
    todo.append(user_input)
    list_todo(todo)


while True:
    print("Comandos: listar, desfazer, refazer, sair")
    user_input = input("Digite uma tarefa ou comando: ")

    comandos = {
        "listar": lambda: list_todo(todo),
        "desfazer": lambda: undo(todo, undo_redo),
        "refazer": lambda: redo(todo, undo_redo),
        "sair": lambda: os._exit(0),
        "adicionar": lambda: add_task(todo, user_input),
    }
    
    comando = (
        comandos.get(user_input)
        if comandos.get(user_input) is not None
        else comandos["adicionar"]
    )
    comando()
