# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Henrique Mualem Marti, henriquemm3@al.insper.edu.br
# - aluno B: Thiago Lopes, thiagod@al.insper.edu.br


"""
NKO Enterprises Presents: Escape Insper

Created on Tue Apr 16 16:32:14 2019

@author: Maulem and ThiagoD
"""

###Animação de entrada:








###Introdução ao game:

"""

print("Bem vindo ao Choices Game")
print("Digite o nome do seu jogador:")
player = input("Nome:")
print("\x1b[2J\x1b[1;1H") ###Esse comando limpa a tela do console do usuario
print("") ###Esse comando pula uma linha para ficar organizado apos usar o comando acima.
print("Bem vindo {0} ao Choices Game!".format(player))
print("")
print("Descrição do jogo:")
print("Você é um aluno do Insper que teve uma crise de insonia e dormiu alguns dias seguidos perdendo aulas e chegando no dia da entrega do EP.")
print("")
print("Você então vai tentar pedir para o professor adiar a entrega, mas para isso primeiro vai ter que achar ele. ")
print("")
print("Então boa sorte na sua jornada {0}!".format(player))


"""

###Cenarios gerais:

def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "Rua",
            "descricao": "Voce esta na frente dos dois predios do Insper."
                         "Para qual predio voce quer ir?",
            "opcoes": {
                "predio 1": "Entrar no predio 1",
                "predio 2": "Entrar no predio 2"
            }
        },
        "predio 1": {
                "titulo": "Saguao de entrada do predio antigo(predio 1)",
                "descricao": "Voce esta no saguao de entrada do predio 1",
                "opcoes": {
                        "inicio": "Voltar pra rua",
                        "biblioteca": "Ir para a biblioteca buscar pistas",
                        "elevador": "Ir pro elevador para procurar o professor"
            }
        },     
        "biblioteca": {
            "titulo": "A casa dos livros",
            "descricao": "Voce sente um cheiro misterioso e quente vindo de uma das salas do fundao!",
            "opcoes": {
                "Sala misteriosa": "Ir investigar o cheiro misterioso",
                "predio 1": "Voltar para o saguao de entrada do predio 1"
            }
        },
        "sala misteriosa": {
            "titulo": "O cachorro quente magico",
            "descricao": "Voce ve um cachorro quente cheiroso e quentinho em cima da mesa. "
                         "Voce pode come-lo para ganhar alguma habilidade especial... "
                         "ou talvez deixa-lo la ja que ele nao é seu...",
            "opcoes": {
                "comer": "Encher sua barriga com esse delicioso cachorro quente",
                "biblioteca": "Voltar para a Biblioteca"
              }
        },
        "elevador": {
            "titulo": "Caverna da tranquilidade",
            "descricao": "Voce esta na biblioteca",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada"
            }
        }
    }
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual 
    

cenarios, cenario_atual = carregar_cenarios()


###Jogo central

game_over = False
while not game_over:
    cenario_atual = cenarios[cenario_atual]
    
    print("Voce esta no(a) {0}".format(cenario_atual["titulo"]))
    print(cenario_atual["descricao"])
    print("Suas opcoes são: {0}".format(cenario_atual["opcoes"]))     
    

    opcoes = cenario_atual["opcoes"] 
    if len(opcoes) == 0:
        print("Acabaram-se suas opções! Mwo mwo mwooooo...")
        game_over = True
    else:

    # Aluno B: substitua este comentário e a linha abaixo pelo código
    # para pedir a escolha do usuário.
        escolha = input("-")

    if escolha in opcoes:
        cenario_atual = escolha
    else:
        print("Sua indecisão foi sua ruína!")
        game_over = True

print("Você morreu!")
    



 






































