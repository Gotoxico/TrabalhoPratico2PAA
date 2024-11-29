from HuffmanEncoder import Arvore
import os

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('===============================================')
    print('| HUFFMAN ENCODER                             |')
    print('===============================================')
    print('|1 - Executar teste pronto                    |')
    print('|2 - Executar manualmente                     |')
    print('|0 - Voltar                                   |')
    print('===============================================')
    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('===============================================')
        print('|Executando teste pronto!                     |')
        print('===============================================')
        print('|Texto: abracadabra                           |')
        print('|Árvore de Huffman:                           |')
        print('===============================================')

        arvore = Arvore()
        texto = "abracadabra"
        print('\n===============================================')
        print('Texto codificado:')
        arvore.huffmanEncoder(arvore.raiz, list(texto))
        print('=================================================')
    elif opcao == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('===============================================')
        print('|Executando manualmente!                      |')
        print('===============================================')
        texto = input('Digite o texto a ser codificado: ')
       
        print('===============================================')
        print('|Árvore de Huffman:                           |')
        print('===============================================')
        
        arvore = Arvore()
        print('\n===============================================')
        print('Texto codificado:')
        arvore.huffmanEncoder(arvore.raiz, list(texto))
        print('=================================================')
        

