class Solution(object):
    def maxProduct(self, numeros):
        tamanho = len(numeros)
        dp = [0] * tamanho
        dp[0] = numeros[0]
        resposta = dp[0]
        for i in range(1, tamanho):
            dp[i] = max(numeros[i], dp[i - 1] * numeros[i])
            if dp[i] > resposta:
                resposta = dp[i]
        return resposta


# Testes
solucao = Solution()
print(solucao.maxProduct([2,3,-2,4]))

