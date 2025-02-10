class Solution(object):
    def profitableSchemes(self, n, minProfit, grupo, lucro):
        tamanho = len(grupo)
        dp = [[[0]*(minProfit+1) for _ in range(n+1)] for _ in range(tamanho+1)]
        dp[0][0][0] = 1
        for i in range(1, tamanho+1):
            pessoas = grupo[i-1]
            ganho_crime = lucro[i-1]
            for membros_usados in range(n+1):
                for ganho_atual in range(minProfit+1):
                    dp[i][membros_usados][ganho_atual] += dp[i-1][membros_usados][ganho_atual]
                    if membros_usados + pessoas <= n:
                        novo_ganho = ganho_atual + ganho_crime
                        if novo_ganho > minProfit:
                            novo_ganho = minProfit
                        dp[i][membros_usados + pessoas][novo_ganho] += dp[i-1][membros_usados][ganho_atual]
        resposta = 0
        for membros_usados in range(n+1):
            resposta += dp[tamanho][membros_usados][minProfit]
        return resposta


print(solucao.profitableSchemes(5, 3, [2, 2], [2, 3]))