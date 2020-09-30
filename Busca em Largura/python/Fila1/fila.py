class No:
    def __init__(self, dado=0, proximo_no=None):
        self.dado = dado
        self.proximo = proximo_no

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.proximo)

class Fila:
    
    def __init__(self):
        self.primeiro = None
        self.ultimo   = None


    def __repr__(self):
        return "[" + str(self.primeiro) + "]"

    def insere(self, novo_dado):
        novo_no = No(novo_dado)

        # Insere em uma fila vazia.
        if self.primeiro == None:
            self.primeiro = novo_no
            self.ultimo = novo_no
        else:
            # Faz com que o novo nodo seja o último da fila.
            self.ultimo.proximo = novo_no
            # Faz com que o último da fila referencie o novo nodo.
            self.ultimo = novo_no
    
    def remove(self):
        assert self.primeiro != None, "Impossível remover elemento de fila vazia."
        aux = self.primeiro
        self.primeiro = self.primeiro.proximo

        if self.primeiro == None:
            self.ultimo = None
        
        return aux