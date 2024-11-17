class Item:
    def __init__(self, peso, valor):
        self.peso = peso
        self.valor = valor

    def adicionarPeso(self, peso):
        self.peso = peso

    def adicionarValor(self, valor):
        self.valor = valor

class FractionalKnapsackProblem:
    def _ordenarItensProporcaoValorPeso(self, itens):
        for i in range(len(itens)):
            for j in range(i, len(itens)):
                if itens[i].valor / itens[i].peso < itens[j].valor / itens[j].peso:
                    itens[i], itens[j] = itens[j], itens[i] 

    def fractionalKnapsackProblem(self, itens, capacidade):
        self._ordenarItensProporcaoValorPeso(itens)
        valorTotal = 0
        pesoAtual = 0
        for i in range(len(itens)):
            if itens[i].peso + pesoAtual <= capacidade:
                valorTotal += itens[i].valor
                pesoAtual += itens[i].peso
            else:
                valorTotal += (capacidade - pesoAtual) * (itens[i].valor / itens[i].peso)
                break

        return valorTotal
