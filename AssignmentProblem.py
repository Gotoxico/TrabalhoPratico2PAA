class noGrafo:
    def __init__(self):
        self.valor = 0
        self.peso = -1
        self.vertice = -1

class Grafo:
    def __init__(self, numeroVertices):
        self.matrizAdjacencia = [[noGrafo() for _ in range(numeroVertices)] for _ in range(numeroVertices)]

    def adicionarAresta(self, vertice1, vertice2, peso):
        self.matrizAdjacencia[vertice1][vertice2].valor = 1
        self.matrizAdjacencia[vertice1][vertice2].peso = peso
        self.vertice = vertice1

    def removerAresta(self, vertice1, vertice2):
        self.matrizAdjacencia[vertice1][vertice2].valor = 0
        self.matrizAdjacencia[vertice1][vertice2].peso = -1
        self.vertice = -1
    
    def verificarAresta(self, vertice1, vertice2):
        return self.matrizAdjacencia[vertice1][vertice2].valor != 0
    
    def verificarPeso(self, vertice1, vertice2):
        return self.matrizAdjacencia[vertice1][vertice2].peso != -1
    
    def obterPeso(self, vertice1, vertice2):
        return self.matrizAdjacencia[vertice1][vertice2].peso
    
    def obterVizinhos(self, vertice):
        vizinhos = []
        for i in range(len(self.matrizAdjacencia[vertice])):
            if self.matrizAdjacencia[vertice][i].valor != 0:
                vizinhos.append(i)
        return vizinhos
    
    def imprimirGrafo(self):
        for i in range(len(self.matrizAdjacencia)):
            for j in range(len(self.matrizAdjacencia[i])):
                if self.matrizAdjacencia[i][j].valor != 0:
                    print(f'Vertice {i} -> {j} com peso {self.matrizAdjacencia[i][j].peso}')
    
class NoArvore:
    def __init__(self, pai = None, combinacao = None, custo = 0):
        self.pai = pai
        self.combinacao = combinacao if combinacao else []
        self.custo = custo

class Arvore:
    def __init__(self):
        self.raiz = NoArvore()
        self.melhorSolucao = None
        self.melhorCusto = float('inf')

    def adicionarNo(self, pai, combinacao, custo):
        no = NoArvore(pai, combinacao, custo)
        return no
    
    def _assignmentProblem(self, no, grafo):
        if len(no.combinacao) == len(grafo.matrizAdjacencia):
            if no.custo < self.melhorCusto:
                self.melhorCusto = no.custo
                self.melhorSolucao = no
            return
        
        for i in range(len(grafo.matrizAdjacencia)):
            if i not in no.combinacao:
                custoAdicional = grafo.obterPeso(len(no.combinacao), i)
                if custoAdicional != -1:
                    novoCusto = no.custo + custoAdicional
                    if novoCusto < self.melhorCusto:
                        novoNo = self.adicionarNo(no, no.combinacao + [i], novoCusto)
                        self._assignmentProblem(novoNo, grafo)

    def buscarMelhorCaminho(self, grafo):
        self._assignmentProblem(self.raiz, grafo)

    


    




        

        
    
