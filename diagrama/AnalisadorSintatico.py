import pandas as pd
import numpy as np


#************************** TABELA DE ANALISE PREDITIVA E VETOR DE PRODUÇÕES ************************************

#Tabela de Análise Preditiva
df1 = pd.read_excel('tabelaPreditivaExcel.xlsx')
tabela_preditiva = np.asarray(df1)

#Vetor de Producoes
df2 = pd.read_excel('vetorProducoes.xlsx')
vetor_producoes = np.asarray(df2)

#Numero de Linhas e Colunas da Tabela de Análise Preditiva
numero_linhasTab = df1.shape[0]
numero_colunasTab = df1.shape[1]

#Numero de Linhas e Colunas do Vetor de Producoes
numero_linhasVet = df2.shape[0]
numero_colunasVet = df2.shape[1]




#Função para pegar a tupla(linhas,coluna) de determinado Não Terminal. Ex: pegaLinhaColunaNaoTerminal("S")
def pega_linha_coluna(simbolo):
    for i in range(0,numero_linhasTab):
        for j in range(0,numero_colunasTab):
            if tabela_preditiva[i][j] == simbolo:
                return i,j
    return None

#Função que retorna valores da tabela, dado um Não Terminal e um Terminal. Ex: pegaValorTabela("declaracao_das_variaveis","identificador")
def pegaValorTabela(NTerminal, Terminal):
    linhaNTerminal, colunaNTerminal = pega_linha_coluna(NTerminal)
    linhaTerminal, colunaTerminal = pega_linha_coluna(Terminal)

    return tabela_preditiva[linhaNTerminal][colunaTerminal]

#Função que retorna a producao correta, dado um Não Terminal e um Terminal. Ex: pega_vetor_producoes("S","programa")
def pega_vetor_producoes(NTerminal, Terminal):
    linhaNTerminal, colunaNTerminal = pega_linha_coluna(NTerminal)
    linhaTerminal, colunaTerminal = pega_linha_coluna(Terminal)
    valor = tabela_preditiva[linhaNTerminal][colunaTerminal]
    producao = vetor_producoes[valor-1][1]

    print("O valor da produção é: " ,valor, " com resultado: ",producao)
    return producao.split()





#******************************************* PILHA ****************************************************

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

    pilha.push("sadas")
    pilha.push(20)
    pilha.push(30)
    pilha.push(40)

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






