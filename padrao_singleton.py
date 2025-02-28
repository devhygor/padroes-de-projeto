

class Singleton(object):

    def __new__(cls):
        # Verifica se a classe já tem uma instância
        # Se não tiver, cria uma nova instância
        # Se tiver, retorna a instância já criada
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
        return cls.instance

s1 = Singleton()
print(f'ID Instância 1: {id(s1)}')

s2 = Singleton()
print(f'Instância 2: {id(s2)}')