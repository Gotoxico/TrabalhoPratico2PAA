#Transcrição do pseudocódigo presente em https://en.wikipedia.org/wiki/Knapsack_problem e da impressao dos slides
class Item:
    def __init__(self, peso, valor):
        self.peso = peso
        self.valor = valor

    def adicionarPeso(self, peso):
        self.peso = peso

    def adicionarValor(self, valor):
        self.valor = valor

class BooleanKnapsackProblem:
    def _criarArrayValores(self, itens):
        array = []
        for i in range(len(itens)):
            array.append(itens[i].valor)
        return array
    
    def _criarArrayPesos(self, itens):
        array = []
        for i in range(len(itens)):
            array.append(itens[i].peso)
        return array

    def _booleanKnapsackProblem(self, itens, capacidade):
        n = len(itens)
        v = self._criarArrayValores(itens)
        w = self._criarArrayPesos(itens)

        matriz = [[0 for _ in range(capacidade + 1)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, capacidade + 1):
                if w[i - 1] > j:
                    matriz[i][j] = matriz[i - 1][j]
                else:
                    matriz[i][j] = max(matriz[i - 1][j], matriz[i - 1][j - w[i - 1]] + v[i - 1])
        return matriz
    
    def imprimirResultado(self, itens, capacidade):
        matriz = self._booleanKnapsackProblem(itens, capacidade)
        n = len(itens)
        
        solucao = []
        capacidadeAtual = capacidade
        for i in range(n, 0, -1):
            if matriz[i][capacidadeAtual] != matriz[i - 1][capacidadeAtual]:
                solucao.append(itens[i - 1])  
                capacidadeAtual -= itens[i - 1].peso  

        valorTotal = 0
        pesoTotal = 0
        
        print("Itens escolhidos:")
        for item in solucao:
            print(f"Peso: {item.peso}, Valor: {item.valor}")
            valorTotal += item.valor
            pesoTotal += item.peso
        print(f"Valor total: {valorTotal}")
        print(f"Peso total: {pesoTotal}")

        



        