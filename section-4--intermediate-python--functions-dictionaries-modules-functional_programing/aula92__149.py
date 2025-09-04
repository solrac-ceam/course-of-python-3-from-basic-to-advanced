# Yield from

def gen1():
    yield 1
    yield 2
    yield 3

def gen2():
    yield from gen1()
    yield 4
    yield 5
    yield 6

g = gen2()
for numero in g:
    print(numero)


print()


def gen3(gen=None):
    if gen is not None:
         yield from gen()
    yield 4
    yield 5
    yield 6

def gen4():
    yield 10
    yield 20
    yield 30

g1 = gen3(gen1)
g2 = gen3(gen4)
g3 = gen3()

print("g1:")
for numero in g1:
    print(numero)

print()
print("g2:")
for numero in g2:
    print(numero)

print()
print("g3:")
for numero in g3:
    print(numero)
