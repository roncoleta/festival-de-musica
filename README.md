Sistema de Organização de Festival de Música

Este projeto simula um sistema simples para organizar um festival de música utilizando Python.

O sistema é dividido em três partes:

Na primeira parte, é criado um dicionário chamado `programacao`, onde cada banda possui um horário e um estilo musical. O sistema permite adicionar novas bandas, listar as bandas com seus estilos e mostrar apenas os horários das apresentações.

Na segunda parte, é utilizada uma fila com `collections.deque` para controlar o acesso do público. O público VIP tem prioridade e entra primeiro na fila. O sistema mostra a ordem atual da fila, simula a entrada de pessoas e permite adicionar mais participantes.

Na terceira parte, um menu interativo é implementado com `input()` para permitir o cadastro de novas bandas, exibir a programação completa e gerenciar a fila do público (adicionando ou removendo pessoas).
