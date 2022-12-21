class Nodo:

    def __init__(self, dado=None, nodo_anterior=None):
        self.dado = dado
        self.anterior = nodo_anterior

    def __repr__(self):
        return '%s -> %s' % (self.dado, self.anterior)


class Pilha:

    def __init__(self):
        self.topo = None
        self.tamanho = 0

    def __repr__(self):
        return "[" + str(self.topo) + "]"

    def push(self, novo_dado):

        # Cria um novo nodo com o dado a ser armazenado.
        novo_nodo = Nodo(novo_dado)

        # Faz com que o novo nodo seja o topo da pilha.
        novo_nodo.anterior = self.topo

        # Faz com que a cabeça da lista referencie o novo nodo.
        self.topo = novo_nodo

        # Adiciona 1 no tamanho da pilha
        self.tamanho = self.tamanho + 1

    def pop(self):

        assert self.topo, "Impossível remover valor de pilha vazia."

        self.topo = self.topo.anterior

        self.tamanho = self.tamanho - 1

    def pilha_vazia(self):
        if self.topo == None:
            return True
        else:
            return False


def main():
    pilha = Pilha()
    print("Pilha vazia: ", pilha)

    # Insere elementos na pilha.

    pilha.push(10)
    pilha.push(20)
    pilha.push(30)

    pilha.pop()
    pilha.pop()

    print(pilha)

    if pilha.pilha_vazia():
        print("A pilha está vazia")
    else:
        print("A pilha não esta vazia")

    print("O tamanho da pilha é: ", pilha.tamanho)


if __name__ == '__main__':
    main()