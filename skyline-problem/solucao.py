class Solution(object):
    def getSkyline(self, edificios):
        coordenadas = []
        for inicio, fim, altura in edificios:
            coordenadas.append(inicio)
            coordenadas.append(fim)
        return []

solucao = Solution()
print(solucao.getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]))