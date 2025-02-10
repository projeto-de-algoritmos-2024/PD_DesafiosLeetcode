class Solution(object):
    def getSkyline(self, edificios):
        coordenadas = []
        for inicio, fim, altura in edificios:
            coordenadas.append(inicio)
            coordenadas.append(fim)
        conjunto_ordenado = sorted(set(coordenadas))
        mapeamento = {}
        for i, c in enumerate(conjunto_ordenado):
            mapeamento[c] = i
        dp = [0] * len(mapeamento)
        for inicio, fim, altura in edificios:
            for j in range(mapeamento[inicio], mapeamento[fim]):
                if altura > dp[j]:
                    dp[j] = altura
        resposta = []
        altura_atual = 0
        for i in range(len(dp)):
            if dp[i] != altura_atual:
                resposta.append([conjunto_ordenado[i], dp[i]])
                altura_atual = dp[i]
        if altura_atual != 0:
            resposta.append([conjunto_ordenado[-1], 0])
        return resposta

solucao = Solution()
print(solucao.getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))
print(solucao.getSkyline([[0,2,3],[2,5,3]]))