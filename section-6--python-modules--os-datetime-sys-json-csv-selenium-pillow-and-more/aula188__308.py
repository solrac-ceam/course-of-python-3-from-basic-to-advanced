# argparse.ArgumentParser para argumentos mais complexos
# Tutorial Oficial:
# https://docs.python.org/pt-br/3/howto/argparse.html
from argparse import ArgumentParser


parser = ArgumentParser()

parser.add_argument(
    "-b",
    "--basic",
    help='Mostra "Ola mundo" na tela',
    # type=str,
    metavar="STRING",
    action="append",  # Recebe o argumento mais dce uma vez
    # nargs="+",  # Recebe mais de um valor
)

parser.add_argument(
    "-v",
    "--verbose",
    help="mostra logs",
    action="store_true",  # Recebe o argumento como booleano
)


args = parser.parse_args()

if args.basic is None:
    print("Você não passou o argumento -b")
else:
    print("O valor de basic:", args.basic)

print(args.verbose)
