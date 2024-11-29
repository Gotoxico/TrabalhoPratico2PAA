import MainAssignmentProblem  
import MainHuffmanEncoder
import MainBooleanKnapsack
import MainLongestCommon
import MainFractionalKnapsack
import os

def menuInicial():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('===============================================')
    print('| TRABALHO PRÁTICO 2 - PROJETO DE ALGORITMOS  |')
    print('===============================================')
    print('|1 - Assignment Problem                       |')
    print('|2 - Huffman Encoder                          |')
    print('|3 - Fractional Knapsack Problem              |')
    print('|4 - Boolean Knapsack Problem                 |')
    print('|5 - Longest Common Subsequence               |')
    print('|0 - Sair                                     |')
    print('===============================================')
    return int(input('Escolha qual algorítmo será executado: '))


if __name__ == '__main__':
    while True:
        opcao = menuInicial()
        if opcao == 0:
            break
        elif opcao == 1:
            MainAssignmentProblem.main()
        elif opcao == 2:
            MainHuffmanEncoder.main()
        elif opcao == 3:
            MainFractionalKnapsack.main()
        elif opcao == 4:
            MainBooleanKnapsack.main()
        elif opcao == 5:
            MainLongestCommon.main()
        else:
            print('Opção inválida! Tente novamente.')
        input('\nPressione qualquer tecla para continuar...')
    