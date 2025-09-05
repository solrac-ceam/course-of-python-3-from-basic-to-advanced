# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Exception em Python, você só
# precisa herdar de alguma exceção da linguagem.
# A recomendação da doc é herdar de Exception.
# https://docs.python.org/3/library/exceptions.html
# Criando exceções (comum colocar Error ao final)
# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)
class MeuError(Exception):
    ...


class OutroError(Exception):
    ...


def levantar():
    exception_ = MeuError("a", "b", "c")
    exception_.add_note("Olha a noat 1")
    exception_.add_note("Você errou isso")
    raise exception_


try:
    levantar()
except (MeuError, ZeroDivisionError) as erro:
    print(erro.__class__.__name__)
    print(erro.args)
    exception_ = OutroError("Vou lançar de novo")
    exception_.__notes__ = erro.__notes__.copy()
    exception_.add_note("Mais uma nota")
    raise exception_ from erro
