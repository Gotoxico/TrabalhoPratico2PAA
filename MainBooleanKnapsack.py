from BooleanKnapsackProblem import Item
from BooleanKnapsackProblem import BooleanKnapsackProblem
import os

itens = [Item(10, 60), Item(20, 100), Item(30, 120)]
capacidade = 50
problema = BooleanKnapsackProblem()
problema.imprimirResultado(itens, capacidade)

itens = [Item(2, 10), Item(3, 5), Item(5, 15), Item(7, 7), Item(1, 6), Item(4, 18), Item(1, 3)]
capacidade = 15
problema = BooleanKnapsackProblem()
problema.imprimirResultado(itens, capacidade)

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('===============================================')
    print('| PROBLEMA DA MOCHILA BOOLEANA                |')
    print('===============================================')
    print('|1 - Executar teste pronto                    |')
    print('|2 - Inserir valores manualmente              |')
    print('|0 - Voltar                                   |')
    print('===============================================')
    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('===============================================')
        print('| Executando teste pronto                     |')
        print('===============================================')

        itens = [Item(2, 10), Item(3, 5), Item(5, 15), Item(7, 7), Item(1, 6), Item(4, 18), Item(1, 3)]
        capacidade = 15

        print(f'Capacidade da mochila: {capacidade}')
        print('Itens disponíveis:')
        
        for item in itens:
            print(f'|Peso: {item.peso} - Valor: {item.valor}')

        problema = BooleanKnapsackProblem()
        print('===============================================')
        print('Resultado:')
        problema.imprimirResultado(itens, capacidade)
        print('===============================================')

    elif opcao == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('===============================================')
        print('|Inserindo valores manualmente!               |')
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
        print(f'|Capacidade da mochila: {capacidade}')
        print(f'|Itens disponíveis: ')
        for item in itens:
            print(f'|Peso: {item.peso} - Valor: {item.valor}')
        print('===============================================')
        problema = BooleanKnapsackProblem()
        print('===============================================')
        print('Resultado:')
        problema.imprimirResultado(itens, capacidade)
        print('===============================================')