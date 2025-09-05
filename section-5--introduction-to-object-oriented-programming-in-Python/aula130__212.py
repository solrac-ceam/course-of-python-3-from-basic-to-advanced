# method vs @classmethod vs @staticmethod
# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estático (❌self, ❌cls)
class Connection:
    def __init__(self, host="localhost"):
        self.host = host
        self.user = None
        self.password = None

    def set_user(self, user):
        self.user = user

    def set_password(self, password):
        self.password = password

    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.set_user(user)
        connection.set_password(password)
        return connection

    @staticmethod
    def log(msg):
        print("LOG", msg)


c1 = Connection()
c1.set_user("Luiz")
c1.set_password("123")
print(c1.user)
print(c1.password)

print()

c2 = Connection.create_with_auth("luiz", "1234")
print(c2.user)
print(c2.password)

print()

Connection.log("Essa é uma mensagem de log")
