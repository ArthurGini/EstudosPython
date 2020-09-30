"""
No Liers’ dice, cada jogador recebe 5 dados. Em cada rodada os jogadores lançam os seus dados, mantendo suas faces escondidas dos demais jogadores.
Cada jogador então escolhe uma face (1 a 6) e da um palpite de quantas faces iguais a esta há na mesa.
O próximo a jogar tem três alternativas

    escolhe uma face e da um palpite, que deve ser necessariamente maior que o palpite anterior e passa para o próximo jogador.

    chama o jogador anterior de mentiroso, neste caso abrem-se os dados e verifica-se o palpite corrente é verdadeiro. Se for o jogador atual perde um dado, senão o jogador anterior perde um dado.

    concorda com o palpite do jogador anterior. Neste caso, abrem-se os dados e se o palpite estiver correto, o jogador anterior perde dois dados.

Ganha o último jogador com dados na mesa.
Implemente o Liers’ dice.

    O jogo deve ser para um usuário contra até 4 jogadores controlados pelo computador

    Use funções;

    Considere usar probabilidades para que um jogador do PC, de um palpite, chame de mentiroso ou concorde com o jogador anterior.

    Use diferentes probabilidade para diferentes jogadores para simular diferentes comportamentos.

    É possível utilizar-se de alguma heurística para melhorar os jogadores do PC?

    Quem fica mais tempo na mesa, um jogador com heurística ou um jogador aleatório?

"""

1 jogador = 5 dados 
1 jogador escolhe a face do dado (1 a 6)
Palpita quantas faces iguais tem na mesa 

O prox jogador tem 2 alternativas:
    escolhe uma face e da um palpite, que deve ser necessariamente maior que o palpite anterior e passa para o próximo jogador.

    chama o jogador anterior de mentiroso, neste caso abrem-se os dados e verifica-se o palpite corrente é verdadeiro. 
    Se for o jogador atual perde um dado, senão o jogador anterior perde um dado.

    concorda com o palpite do jogador anterior. Neste caso, abrem-se os dados e se o palpite estiver correto, o jogador anterior perde dois dados.