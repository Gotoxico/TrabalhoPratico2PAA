from FractionalKnapsackProblem import Item
from FractionalKnapsackProblem import FractionalKnapsackProblem
import os

itens = [Item(10, 60), Item(20, 100), Item(30, 120)]
capacidade = 50
problema = FractionalKnapsackProblem()
valorTotal = problema.fractionalKnapsackProblem(itens, capacidade)
print(f"Valor total obtido: {valorTotal}")


def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('===============================================')
    print('| FRACTIONAL KNAPSACK PROBLEM                 |')
    print('===============================================')
    print('|1 - Executar teste pronto                    |')
    print('|2 - Inserir dados manualmente                |')
    print('|0 - Sair                                     |')
    print('===============================================')
    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('===============================================')
        print('|Executando teste pronto!                     |')
        print('===============================================')
        itens = [Item(10, 60), Item(20, 100), Item(30, 120), Item(40, 150), Item(50, 200)]
        capacidade = 50
        print(f"Capacidade da mochila: {capacidade}")
        print("Itens disponíveis: \n")
        for item in itens:
            print(f"|Peso: {item.peso} - Valor: {item.valor}")

        problema = FractionalKnapsackProblem()
        valorTotal = problema.fractionalKnapsackProblem(itens, capacidade)
        print('\n===============================================')
        print(f"|Valor total obtido: {valorTotal}")
        print('=================================================')
    elif opcao == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('===============================================')
        print('|Inserindo dados manualmente!                 |')
        print('===============================================')
        capacidade = int(input('Digite a capacidade da mochila: '))
        n = int(input('Digite a quantidade de itens: '))
        itens = []
        for i in range(n):
            print('===============================================')
            peso = int(input(f'Digite o peso do item {i + 1}: '))
            valor = int(input(f'Digite o valor do item {i + 1}: '))
            itens.append(Item(peso, valor))
            print('===============================================')
        
        print('\n===============================================')
        print(f"|Capacidade da mochila: {capacidade}          ")
        print(f"|Itens disponíveis: ")
        for item in itens:
            print(f"|Peso: {item.peso} - Valor: {item.valor}")
        print('===============================================')
        problema = FractionalKnapsackProblem()
        valorTotal = problema.fractionalKnapsackProblem(itens, capacidade)
        print('\n===============================================')
        print(f"|Valor total obtido: {valorTotal}")
        print('===============================================') 

