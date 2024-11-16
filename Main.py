from AssignmentProblem import Grafo, Arvore

numeroVertices = 4  # Change this number as needed
grafo = Grafo(numeroVertices)

# Add edges to the graph with weights
grafo.adicionarAresta(0, 1, 10)
grafo.adicionarAresta(0, 2, 15)
grafo.adicionarAresta(0, 3, 20)
grafo.adicionarAresta(1, 0, 5)
grafo.adicionarAresta(1, 2, 9)
grafo.adicionarAresta(1, 3, 10)
grafo.adicionarAresta(2, 0, 6)
grafo.adicionarAresta(2, 1, 13)
grafo.adicionarAresta(2, 3, 12)
grafo.adicionarAresta(3, 0, 8)
grafo.adicionarAresta(3, 1, 8)
grafo.adicionarAresta(3, 2, 9)

# Create an instance of Arvore and solve the problem
arvore = Arvore()
arvore.buscarMelhorCaminho(grafo)

# Print the best solution found
if arvore.melhorSolucao:
    print("Melhor caminho encontrado:", arvore.melhorSolucao.combinacao)
    print("Custo do melhor caminho:", arvore.melhorCusto)
else:
    print("Nenhuma solução encontrada.")