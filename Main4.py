from BooleanKnapsackProblem import Item
from BooleanKnapsackProblem import BooleanKnapsackProblem

itens = [Item(10, 60), Item(20, 100), Item(30, 120)]
capacidade = 50
problema = BooleanKnapsackProblem()
problema.imprimirResultado(itens, capacidade)

itens = [Item(2, 10), Item(3, 5), Item(5, 15), Item(7, 7), Item(1, 6), Item(4, 18), Item(1, 3)]
capacidade = 15
problema = BooleanKnapsackProblem()
problema.imprimirResultado(itens, capacidade)