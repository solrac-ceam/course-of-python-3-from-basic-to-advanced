# Introdução às Generator functions em Python
# generator = (n for n i range(1000000))


def generator(n=0):
    yield 1  # Pausar
    print("Continuando...")
    yield 2  # Pausar
    print("Mais uma...")
    yield 3
    print("Vou terminar")
    return "ACABOU"


gen = generator()
for n in gen:
    print(n)


print()


def generator2(n=0, maximun=10):
    while True:
        yield n
        n += 1

        if n >= maximun:
            return


gen2 = generator2()
for n in gen2:
    print(n)
