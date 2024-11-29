from LongestCommonSubsequence import LCS
import os

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    LongestCommon = LCS()
    print('===============================================')
    print('| LONGEST COMMON SUBSEQUENCE                  |')
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

        s1 = "CADD"
        s2 = "CBBADED"
        print(f'Sequência 1: {s1}')
        print(f'Sequência 2: {s2}')

        matrix = LongestCommon.getLCS(s1, s2)
        print('\nMatriz de programação dinâmica: ')
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                print(matrix[i][j], end = " ")
            print()

        print('\n===============================================')
        print(f'|Tamanho da maior subsequência comum: {matrix[len(s1)][len(s2)]}')
        print(f'|Maior subsequência comum: {LongestCommon.extrairLCS(s1, s2, matrix)}')
        print('===============================================')

    elif opcao == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('===============================================')
        print('|Inserindo valores manualmente!               |')
        print('===============================================')
        s1 = input('Digite a primeira sequência: ')
        s2 = input('Digite a segunda sequência: ')
        print('===============================================')
        print(f'|Sequência 1: {s1}')
        print(f'|Sequência 2: {s2}')
        print('===============================================')

        matrix = LongestCommon.getLCS(s1, s2)
        print('\nMatriz de programação dinâmica: ')
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                print(matrix[i][j], end = " ")
            print()

        print('\n===============================================')
        print(f'|Tamanho da maior subsequência comum: {matrix[len(s1)][len(s2)]}')
        print(f'|Maior subsequência comum: {LongestCommon.extrairLCS(s1, s2, matrix)}')
        print('===============================================')
        print('|Obs: Se inverter a ordem das sequências, o   |')
        print('|resultado pode ser diferente                 |')
        print('===============================================')
        