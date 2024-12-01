from AssignmentProblem import Grafo, Arvore
import os

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('===============================================')
    print('|ASSIGNMENT PROBLEM (Utilizando grafo com     |')
    print('|matriz de adjacência para representação)     |')
    print('===============================================')
    print('|1 - Executar teste pronto                    |')
    print('|2 - Inserir dados manualmente                |')
    print('|0 - Voltar                                   |')
    print('===============================================')
    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        numeroVertices = 4
        os.system('cls' if os.name == 'nt' else 'clear')
        print('===============================================')
        print('|Executando teste pronto!                     |')
        print('|Grafo com 4 vértices...                      |')
        print('===============================================')
        grafo = Grafo(numeroVertices)
        print('\n===============================================')
        print('|Adicionando arestas ao grafo                 |')
        print('===============================================')
        grafo.adicionarAresta(0, 1, 10)
        print('|Aresta 0 -> 1 adicionada com peso 10         |')
        
        grafo.adicionarAresta(0, 2, 15)
        print('|Aresta 0 -> 2 adicionada com peso 15         |')
        
        grafo.adicionarAresta(0, 3, 20)
        print('|Aresta 0 -> 3 adicionada com peso 20         |')

        grafo.adicionarAresta(1, 0, 5)
        print('|Aresta 1 -> 0 adicionada com peso 5          |')
        grafo.adicionarAresta(1, 2, 9)
        print('|Aresta 1 -> 2 adicionada com peso 9          |')
        grafo.adicionarAresta(1, 3, 10)
        print('|Aresta 1 -> 3 adicionada com peso 10         |')
        grafo.adicionarAresta(2, 0, 6)
        print('|Aresta 2 -> 0 adicionada com peso 6          |')
        grafo.adicionarAresta(2, 1, 13)
        print('|Aresta 2 -> 1 adicionada com peso 13         |')
        grafo.adicionarAresta(2, 3, 12)
        print('|Aresta 2 -> 3 adicionada com peso 12         |')
        grafo.adicionarAresta(3, 0, 8)
        print('|Aresta 3 -> 0 adicionada com peso 8          |')
        grafo.adicionarAresta(3, 1, 8)
        print('|Aresta 3 -> 1 adicionada com peso 8          |')
        grafo.adicionarAresta(3, 2, 9)
        print('|Aresta 3 -> 2 adicionada com peso 9          |')
        print('===============================================')

        print('\n===============================================')
        print('|Criando árvore e buscando melhor caminho...  |')
        print('===============================================')

        arvore = Arvore()
        arvore.buscarMelhorCaminho(grafo)

        print('\n===============================================')
        print('|Resultado:                                   |')
        print('===============================================')
        if arvore.melhorSolucao:
            print("Melhor caminho encontrado:", arvore.melhorSolucao.combinacao)
            print("Custo do melhor caminho:", arvore.melhorCusto)
        else:
            print("Nenhuma solução encontrada.")
        print('===============================================')

    elif opcao == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\n==============================================')
        print('|Inserindo dados manualmente                 |')
        print('==============================================')
        
        numeroVertices = int(input('Digite o número de vértices do grafo: '))
        grafo = Grafo(numeroVertices)

        print('\n===============================================')
        print('|Adicionando arestas ao grafo                 |')
        print('===============================================')

        for i in range(numeroVertices):
            for j in range(numeroVertices):
                print('\n===============================================')
                print('|1 - Definir aresta de %d -> %d?' % (i, j))
                print('|0 - Não adicionar aresta')
                print('================================================')
                print('Escolha uma opção:')
                opcaoAresta = int(input())
                if opcaoAresta == 1:
                    peso = int(input(f'Digite o peso da aresta {i} -> {j}: '))
                    grafo.adicionarAresta(i, j, peso)
                    print(f'Aresta {i} -> {j} adicionada com peso {peso}')

        grafo.imprimirGrafo()

        print('\n===============================================')
        print('|Criando árvore e buscando melhor caminho      |')
        print('================================================')
        arvore = Arvore()

        arvore.buscarMelhorCaminho(grafo)

        print('\n===============================================')
        print('|Resultado: ')
        print('===============================================')

        if arvore.melhorSolucao:
            print("Melhor caminho encontrado:", arvore.melhorSolucao.combinacao)
            print("Custo do melhor caminho:", arvore.melhorCusto)
        else:
            print("|Nenhuma solução encontrada. ")
        print('================================================')
    else:
        return
    


