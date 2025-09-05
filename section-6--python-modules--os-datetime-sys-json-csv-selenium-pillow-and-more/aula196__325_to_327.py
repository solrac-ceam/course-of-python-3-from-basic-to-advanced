from time import sleep
from threading import Thread, Lock

# print("hello")
# for i in range(10):
#     print(i)
#     sleep(.5)
# print("World!")


# # Threads usando classes.
# # -----------------------
# class MeuThread(Thread):
#     def __init__(self, texto, tempo):
#         self.texto = texto
#         self.tempo = tempo

#         super().__init__()

#     def run(self) -> None:
#         sleep(self.tempo)
#         print(self.texto)


# t1 = MeuThread("Thread 1", 5)
# t1.start()

# t2 = MeuThread("Thread 2", 3)
# t2.start()

# t3 = MeuThread("Thread 3", 2)
# t3.start()

# for i in range(20):
#     print(i)
#     sleep(1)


# # Threads usando funções.
# # -----------------------
# def vai_demorar(texto, tempo):
#     sleep(tempo)
#     print(texto)


# t1 = Thread(target=vai_demorar, args=("Olá Mundo! 1", 5))
# t1.start()

# t2 = Thread(target=vai_demorar, args=("Olá Mundo! 2", 1))
# t2.start()

# t3 = Thread(target=vai_demorar, args=("Olá Mundo! 3", 2))
# t3.start()

# for i in range(20):
#     print(i)
#     sleep(.5)


# # Esperando a thread terminar.
# # ----------------------------
# def vai_demorar(texto, tempo):
#     sleep(tempo)
#     print(texto)


# t1 = Thread(target=vai_demorar, args=("Olá Mundo! 1", 10))
# t1.start()

# # while t1.is_alive():
# #     print("Esperando a thread.")
# #     sleep(2)
# t1.join()

# print("Thread acabou!")


# Trabalhando com dados nas threads.
# ----------------------------------
class Ingressos:
    def __init__(self, estoque) -> None:
        self.estoque = estoque
        self.lock = Lock()

    def comprar(self, quantidade):
        self.lock.acquire()

        if self.estoque < quantidade:
            print("Não temos ingressos suficeintes")
            self.lock.release()
            return
        
        sleep(1)

        self.estoque -= quantidade
        print(f"Vocẽ comprou {quantidade} ingresso(s). Ainda temos {self.estoque} em estoque.")

        self.lock.release()


ingressos = Ingressos(10)

for i in range(1, 20):
   t = Thread(target=ingressos.comprar, args=(i,))
   t.start()

print(ingressos.estoque)