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
        return []

solucao = Solution()
print(solucao.getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))