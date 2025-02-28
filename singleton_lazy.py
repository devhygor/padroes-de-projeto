

class Singleton:

    __instance = None

    def __init__(self):
        if not Singleton.__instance:
            print('O metodo __init__ foi chamado...')
        else:
            print(f'A instancia já foi criada: {self.get_instance()}')

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Singleton()
        return cls.__instance

s1 = Singleton() # A classe é inicializada, mas o objeto não é criado...

print(f'Criar o objeto agora: {Singleton.get_instance()}') # Detalhe aqui q eu vi q antes mesmo dele entrar no get instance ele entra no init primeiro novamente

s2 = Singleton() # Instancia já criada...