from contextlib import contextmanager


@contextmanager
def my_open(caminho_arquivo, modo):
    try:
        print("Abrindo arquivo")
        arquivo = open(caminho_arquivo, modo, encoding="utf8")
        yield arquivo
    except Exception as e:
        print("Ocurreo um erro", e)
    finally:
        print("Fechando arquivo")
        arquivo.close()


DIR_PATH = "section 5 - introduction to object oriented programming in Python"
with my_open(f"{DIR_PATH}/aula150.txt", "w") as arquivo:
    arquivo.write("Licha 1\n")
    arquivo.write("Licha 2\n", 123)
    arquivo.write("Licha 3\n")
    print("With", arquivo)
