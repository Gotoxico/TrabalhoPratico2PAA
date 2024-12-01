class NoArvore:
    def __init__(self, pai=None, simbolo=None, quantidade=None, probabilidade=None, filhos=None):
        self.pai = pai
        self.simbolo = simbolo
        self.quantidade = quantidade
        self.probabilidade = probabilidade
        self.filhos = filhos if filhos else []

class Arvore:
    def __init__(self):
        self.raiz = NoArvore()  

    def _adicionarNo(self, pai, simbolo, quantidade, probabilidade):
        no = NoArvore(pai, simbolo, quantidade, probabilidade)
        pai.filhos.append(no)
        return no

    def _transformarSimbolosArvore(self, no, texto):
        total = len(texto)
        simbolos_contagem = {}
        
        for simbolo in texto:
            if simbolo in simbolos_contagem:
                simbolos_contagem[simbolo] += 1
            else:
                simbolos_contagem[simbolo] = 1
        
        for simbolo, quantidade in simbolos_contagem.items():
            probabilidade = quantidade / total
            self._adicionarNo(no, simbolo, quantidade, probabilidade)

    def _tamanho(self, no):
        if not no.filhos:
            return 1
        else:
            tamanho = 0
            for filho in no.filhos:
                tamanho += self._tamanho(filho)
            return tamanho

    def _retiraMenorProbabilidade(self, no):
        menor = None
        for filho in no.filhos:
            if not menor or filho.probabilidade < menor.probabilidade:
                menor = filho
        if menor:
            no.filhos.remove(menor)
        return menor

    def _percorreDaRaizAteAFolha(self, folha, caminho=""):
        if not folha.filhos: 
            return {folha.simbolo: caminho}
        else:
            codificacoes = {}
            for filho in folha.filhos:
                novo_caminho = caminho + ("0" if filho == folha.filhos[0] else "1")
                codificacoes.update(self._percorreDaRaizAteAFolha(filho, novo_caminho))
            return codificacoes

    def huffmanEncoder(self, no, texto):
        self._transformarSimbolosArvore(no, texto)

        self.imprimirArvore(no)

        while len(no.filhos) > 1:
            S0 = self._retiraMenorProbabilidade(no)
            S1 = self._retiraMenorProbabilidade(no)
            X = self._adicionarNo(no, S0.simbolo + S1.simbolo, S0.quantidade + S1.quantidade, S0.probabilidade + S1.probabilidade)
            X.filhos.append(S0)
            X.filhos.append(S1)
        
        self.imprimirArvore(no)

        X = no.filhos[0]  

        codigos = self._percorreDaRaizAteAFolha(X)  
        for simbolo, codigo in codigos.items():
            print(f"Código para {simbolo}: {codigo}")
        
        i = 0
        palavra = ""
        while i < len(texto):
            simbolo = texto[i]
            if simbolo in codigos:
                palavra = palavra + codigos[simbolo] + " "
            i += 1
        print(f"Palavra codificada: {palavra}")
        
            

    def imprimirArvore(self, no, nivel=0):
        if no is not None:
            print(f"{' ' * nivel}Simbolo: {no.simbolo}, Quantidade: {no.quantidade}, Probabilidade: {no.probabilidade}")
            for filho in no.filhos:
                self.imprimirArvore(filho, nivel + 2)  


