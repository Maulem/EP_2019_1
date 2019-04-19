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
###Imports:


import time
import random



###Variaveis iniciais:


player = "*****"
game_over = False
comeu = False
aspas = '"'


###Animação de entrada:







###Animacão da morte:


def death(game_over):###Raul perdao por botar print dentro de funcao mas nao sei como fazer para a animacao
    if game_over == True:###funcionar só usando return.
        time.sleep(1)
        print()
        print('                  uuuuuuu')
        time.sleep(0.1)
        print('             uu$$$$$$$$$$$uu')
        time.sleep(0.1)
        print('           uu$$$$$$$$$$$$$$$$$uu')
        time.sleep(0.1)
        print('          u$$$$$$$$$$$$$$$$$$$$$u      ')
        time.sleep(0.1)
        print('         u$$$$$$$$$$$$$$$$$$$$$$$u      ')
        time.sleep(0.1)
        print('        u$$$$$$$$$$$$$$$$$$$$$$$$$u     ')
        time.sleep(0.1)
        print('        u$$$$$$$$$$$$$$$$$$$$$$$$$u     ')
        time.sleep(0.1)
        print('        u$$$$$$"   "$$$"   "$$$$$$u     ')
        time.sleep(0.1)
        print('        "$$$$"      u$u       $$$$"      ')
        time.sleep(0.1)
        print('         $$$u       u$u       u$$$      ')
        time.sleep(0.1)
        print('         $$$u      u$$$u      u$$$      ')
        time.sleep(0.1)
        print('          "$$$$uu$$$   $$$uu$$$$"      ')
        time.sleep(0.1)
        print('           "$$$$$$$"   "$$$$$$$"     ')
        time.sleep(0.1)
        print('             u$$$$$$$u$$$$$$$u')
        time.sleep(0.1)
        print('              u$"$"$"$"$"$"$u')
        time.sleep(0.1)
        print('   uuu        $$u$ $ $ $ $u$$       uuu')
        time.sleep(0.1)
        print('  u$$$$        $$$$$u$u$u$$$       u$$$$')
        time.sleep(0.1)
        print('   $$$$$uu      "$$$$$$$$$"     uu$$$$$$')
        time.sleep(0.1)
        print(' u$$$$$$$$$$$uu    """""    uuuu$$$$$$$$$$')
        time.sleep(0.1)
        print(' $$$$"""$$$$$$$$$$uuu   uu$$$$$$$$$"""$$$"')
        time.sleep(0.1)
        print('  """      ""$$$$$$$$$$$uu ""$"""')
        time.sleep(0.1)
        print('            uuuu ""$$$$$$$$$$uuu')
        time.sleep(0.1)
        print('   u$$$uuu$$$$$$$$$uu ""$$$$$$$$$$$uuu$$$')
        time.sleep(0.1)
        print('   $$$$$$$$$$""""           ""$$$$$$$$$$$"')
        time.sleep(0.1)
        print('    "$$$$$"                      ""$$$$""')
        time.sleep(0.1)
        print('      $$$"                         $$$$"')
        print()
        time.sleep(1)
        
        return "                  Game over!"


###Introdução ao game:

"""

print("Bem vindo ao Escape Insper")
print("Digite o nome do seu jogador:")
player = input("Nome:")
#print("\x1b[2J\x1b[1;1H") ###Esse comando limpa a tela do console do usuario
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
            "titulo": "Rua da perdição",
            "descricao": "Voce esta na frente dos dois predios do Insper.                                       "
                         "Para qual predio voce quer ir?",
            "opcoes": {
                "predio 1": "entrar no predio 1",
                "predio 2": "entrar no predio 2"
            }
        },
        "predio 1": {
                "titulo": "Predio velhão",
                "descricao": "Voce esta no saguao de entrada do predio 1",
                "opcoes": {
                        "inicio": "voltar pra rua",
                        "biblioteca": "ir para a biblioteca buscar pistas",
                        "elevador": "ir pro elevador para procurar o professor"
            }
        },     
        "biblioteca": {
            "titulo": "A casa dos livros",
            "descricao": "Voce sente um cheiro misterioso e quente vindo de uma das salas do fundao!",
            "opcoes": {
                "sala misteriosa": "ir investigar o cheiro misterioso",
                "predio 1": "voltar para o saguao de entrada do predio 1"
            }
        },
        "sala misteriosa": {
            "titulo": "O cachorro quente magico",
            "descricao": "Voce ve um cachorro quente cheiroso e quentinho em cima da mesa.                                        "
                         "Voce pode come-lo para ganhar alguma habilidade especial...                                        "
                         "ou talvez deixa-lo la ja que ele nao é seu...                                       ",
            "opcoes": {
                "comer": "encher a pança com esse delicioso cachorro quente",
                "biblioteca": "voltar para a Biblioteca"
              }
        },
        "comer": {#O que acontecera a seguir depende do randint por isso nao botei descricoes nem opcoes.
            "titulo": "Sorte ou Azar?",
            "descricao": "",
            "opcoes": {
                "biblioteca": "voltar para a Biblioteca"
              }
        },
        "elevador": {
            "titulo": "Caixote de metal",
            "descricao": "Voce esta no elevador",
            "opcoes": {
                "inicio": "voltar para o saguao de entrada"
            }
        }
    }
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual 
    

cenarios, cenario_atual = carregar_cenarios()


###Jogo central:


while not game_over:
    cenario_atual = cenarios[cenario_atual]
    if cenario_atual == cenarios["comer"] and comeu == False:###Primeira feature(Sorte ou Azar?)
        sorte = random.randint(1, 1000)
        if sorte < 801:
            print("Parabens")
            cenario_atual = cenarios["biblioteca"]
            
        else:
            print("Inspetora: É proibido comer na biblioteca!")
            print("Inspetora: Vá agora para o Multiinsper!")
            print("Você fica preso lá por 4 horas o que te faz não encontrar o professor!")
            time.sleep(1)
            game_over = True
        
        
        
    elif cenario_atual == cenarios["comer"] and comeu == True:
        print("Você ja passou por aqui!")
        cenario_atual = cenarios["biblioteca"]
    else:
        print("")
        print(cenario_atual["titulo"])
        print("-" * len(cenario_atual["titulo"]))
        print(cenario_atual["descricao"])
        print("")
        print("Suas opcoes são:")
        for chave in cenario_atual["opcoes"]:
            print("Digite: {0}{1}{2} para {3}".format(aspas, chave, aspas, cenario_atual["opcoes"][chave]))

        opcoes = cenario_atual["opcoes"] 
        if len(opcoes) == 0:
            print("Acabaram-se suas opções {0}! Mwo mwo mwooooo...".format(player))
            game_over = True
        else:
            escolha = input("-")
        
        if escolha in opcoes:
            cenario_atual = escolha
        else:
            print("Sinto muito {0}!".format(player))
            print("Sua indecisão foi sua ruína!")
            game_over = True
            
"""
print(death(True))
"""



 






































