from queue import Queue as fila

class Fila(self):
    
    def __init__(self):
        self.fila = fila()

    def inserir(self, item):
        pergunta = input("Digite quantos valores que deseja adicionar na fila:")
        for i in pergunta:
            adicionar = input("Deseja adicionar o que:")
            self.fila.put(adicionar) 
        
    def remover(self):
        pergunta_remover = input("Digite quantos valores que deseja remover:")
        self.fila.get(pergunta_remover)
        
    def cheia(self):
        if self.fila.full() == True:
            print("A fila esta cheia!")
        else:
            print("A fila não esta cheia!")
        
    def vazia(self):
        if self.fila.empty() =
        
        self.fila.empty()
    
    def tamanho(self):
        self.fila.qsize()
    
    def tamanho_maximo(self):
        self.fila.maxsize()
        
