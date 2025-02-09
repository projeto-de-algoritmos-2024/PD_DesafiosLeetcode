class Solution(object):
    def maxProduct(self, numeros):
        tamanho = len(numeros)
        dp_maior = [0] * tamanho
        dp_menor = [0] * tamanho
        dp_maior[0] = numeros[0]
        dp_menor[0] = numeros[0]
        resposta = numeros[0]
        for i in range(1, tamanho):
            dp_maior[i] = max(numeros[i], 
            dp_maior[i - 1] * numeros[i], 
            dp_menor[i - 1] * numeros[i])
            dp_menor[i] = min(numeros[i], 
            dp_maior[i - 1] * numeros[i], 
            dp_menor[i - 1] * numeros[i])
            if dp_maior[i] > resposta:
                resposta = dp_maior[i]
        return resposta



solucao = Solution()
print(solucao.maxProduct([2,3,-2,4]))
print(solucao.maxProduct([-2,0,-1]))
print(solucao.maxProduct([-2,3,-4]))

