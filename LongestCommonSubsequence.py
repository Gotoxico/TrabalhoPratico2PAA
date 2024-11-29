class LCS:
    def getLCS(self, s1, s2):
        m = len(s1)
        n = len(s2)

        matrix = [[0] * (n + 1) for i in range(m + 1)]
    
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    matrix[i][j] = matrix[i - 1][j - 1] + 1
                else:
                    matrix[i][j] = max(matrix[i - 1][j], matrix[i][j - 1])
                
        return matrix

    def extrairLCS(self, s1, s2, matrix):
        m = len(s1)
        n = len(s2)
        index = matrix[m][n]
        lcs_algo = [""] * (index + 1)
        i = m
        j = n
        while i > 0 and j > 0:

            if s1[i-1] == s2[j-1]:
                lcs_algo[index-1] = s1[i-1]
                i -= 1
                j -= 1
                index -= 1

            elif matrix[i-1][j] > matrix[i][j-1]:
                i -= 1
            else:
                j -= 1
        
        return "".join(lcs_algo)
            

