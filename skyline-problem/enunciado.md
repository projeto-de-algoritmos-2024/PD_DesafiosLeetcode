218. O problema do horizonte

O horizonte de uma cidade é o contorno externo da silhueta formada por todos os prédios daquela cidade quando vistos de longe. Dadas as localizações e alturas de todos os prédios, retorne o horizonte formado por esses prédios coletivamente .

As informações geométricas de cada edifício são fornecidas na matriz buildingsonde :buildings[i] = [lefti, righti, heighti]

leftié a coordenada x da borda esquerda do edifício.ith
rightié a coordenada x da borda direita do edifício.ith
heightié a altura do edifício.ith
Você pode presumir que todos os edifícios são retângulos perfeitos apoiados em uma superfície absolutamente plana em altura 0.

O horizonte deve ser representado como uma lista de "pontos-chave" classificados por sua coordenada x no formato . Cada ponto-chave é o ponto final esquerdo de algum segmento horizontal no horizonte, exceto o último ponto na lista, que sempre tem uma coordenada y e é usado para marcar o término do horizonte onde o edifício mais à direita termina. Qualquer terreno entre os edifícios mais à esquerda e mais à direita deve fazer parte do contorno do horizonte.[[x1,y1],[x2,y2],...]0

Nota: Não deve haver linhas horizontais consecutivas de altura igual no horizonte de saída. Por exemplo, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...]não é aceitável; as três linhas de altura 5 devem ser mescladas em uma na saída final, como tal:[...,[2 3],[4 5],[12 7],...]

Exemplo 1:

Entrada: edifícios = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
Saída: [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]
Explicação:
A Figura A mostra os edifícios da entrada.
A Figura B mostra o horizonte formado por esses edifícios. Os pontos vermelhos na figura B representam os pontos-chave na lista de saída.
Exemplo 2:

Entrada: edifícios = [[0,2,3],[2,5,3]]
Saída: [[0,3],[5,0]]

Restrições:

1 <= buildings.length <= 104
0 <= lefti < righti <= 231 - 1
1 <= heighti <= 231 - 1
buildingsé classificado em ordem não decrescente.lefti
