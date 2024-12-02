# Jogo do NIM
def computador_escolhe_jogada(n,m):
    jogada = n % (m + 1)
    if jogada > 0:
        return jogada
    else:
        return m

def usuario_escolhe_jogada(n,m):
    while True: 
        jogada = int(input("Quantas peças você vai tirar? "))
        if 1 <= jogada <= m and jogada <= n: 
            return jogada 
        else:
            print("Oops! Jogada inválida! Tente de novo.")


def comeca(n,m):
    if n % (m + 1) == 0:
        print("Voce começa!")
        return "usuario"
    else:
        return "computador"
def partida():
    n = int(input("Quantas peças? "))
    m = int(input("Limite de peças por jogada? "))
    primeiro_jogador = comeca(n, m)

    if primeiro_jogador == "computador":
        print("Computador começa!")
        while n > 0:
            jogada_computador=computador_escolhe_jogada(n,m)
            n = n - jogada_computador
            print("O computador tirou" ,jogada_computador, "peças.")
            print("Sobraram",n,"peças")

            if n == 0:
                print("Fim do jogo! O computador ganhou!")
                break

            jogada_usuario = usuario_escolhe_jogada(n,m)
            n = n- jogada_usuario
            print("Você tirou",jogada_usuario,"peças")
            print("Sobraram",n,"peças")
            if n == 0:
                break
    else:
        while n > 0:
            jogada_usuario = usuario_escolhe_jogada(n,m)
            n = n- jogada_usuario
            print("Você tirou ",jogada_usuario,"peças")
            print("Sobraram",n,"peças")
            if n == 0:
                break
            jogada_computador=computador_escolhe_jogada(n,m)
            n = n - jogada_computador
            print("O computador tirou" ,jogada_computador, "peças.")
            print("Sobraram",n,"peças")
            if n == 0:
                print("Fim do jogo! O computador ganhou!")
                break
def campeonato():
    vitorias_usuario = 0
    vitorias_computador = 0

    print("**** Rodada 1 ****")
    vencedor = partida()
    if vencedor == "Fim do jogo! O usuario ganhou!":
        vitorias_usuario += 1
    else:
        vitorias_computador += 1

    print("**** Rodada 2 ****")
    vencedor = partida()
    if vencedor == "usuario":
        vitorias_usuario += 1
    else:
        vitorias_computador += 1

    print("**** Rodada 3 ****")
    vencedor = partida()
    if vencedor == "usuario":
        vitorias_usuario += 1
    else:
        vitorias_computador += 1

    print("**** Final do campeonato! ****")
    print("Placar: Você ",vitorias_usuario, "X",vitorias_computador," Computador")

print("Bem-vindo ao jogo do NIM!")
print("Escolha:")
print("1 - para jogar uma partida isolada")
print("2 - para jogar um campeonato")
escolha =int(input("Qual sua escolha?: "))
while escolha != 1 and escolha != 2:
    print("Ops... não temos essa opção, vamos tentar novamente!")
    escolha =int(input("Qual sua escolha?: "))
if escolha == 2:
    print("Voce escolheu um campeonato!")
    print("Vamos começar! ")
    campeonato()
else:
    print("Voce escolheu uma partida isolada!")
    print("Vamos começar! ")
    partida()
