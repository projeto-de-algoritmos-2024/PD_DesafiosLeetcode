class Solution(object):
    def profitableSchemes(self, n, minProfit, grupo, lucro):
        modulo = 10**9 + 7
        tamanho = len(grupo)
        dp = [[[0]*(minProfit+1) for _ in range(n+1)] for _ in range(tamanho+1)]
        dp[0][0][0] = 1
        for i in range(1, tamanho+1):
            pessoas = grupo[i-1]
            ganho_crime = lucro[i-1]
            for membros_usados in range(n+1):
                for ganho_atual in range(minProfit+1):
                    dp[i][membros_usados][ganho_atual] = (dp[i][membros_usados][ganho_atual] 
                    + dp[i-1][membros_usados][ganho_atual]) % modulo
                    if membros_usados + pessoas <= n:
                        novo_ganho = ganho_atual + ganho_crime
                        if novo_ganho > minProfit:
                            novo_ganho = minProfit
                        dp[i][membros_usados + pessoas][novo_ganho] = (dp[i][membros_usados + pessoas][novo_ganho] 
                        + dp[i-1][membros_usados][ganho_atual]) % modulo
        resposta = 0
        for membros_usados in range(n+1):
            resposta = (resposta + dp[tamanho][membros_usados][minProfit]) % modulo
        return resposta


solucao = Solution()
print(solucao.profitableSchemes(5, 3, [2, 2], [2, 3]))
print(solucao.profitableSchemes(10, 5, [2, 3, 5], [6, 7, 8]))