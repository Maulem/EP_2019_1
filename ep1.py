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
medalhao_fogo = False
medalhao_agua = False
medalhao_neve = False
medalhao_3_elementos = False    ###sao 2 variaveis mas representam o mesmo item!
medalhao3_elementos = False    ###sao 2 variaveis mas representam o mesmo item!
contador = 0 ###Contador de erros

###Animação de entrada:







###Animacão da morte:


def death(game_over):    ###Raul perdao por botar print dentro de funcao mas nao sei como fazer para a animacao
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
'''
#print("\x1b[2J\x1b[1;1H") ###Esse comando limpa a tela do console do usuario
'''
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
###Sistema de inventarios dos medalhoes(feature 3):

def medalhoes(fogo, agua, neve):
    if fogo == True and agua == True and neve == True:
        return True
    else:
        return False

###Cenarios gerais:

def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "Rua da perdição",
            "key": "whatever",###quando o len(key)=0 ativa a feature da sala secreta na biblioteca(hot dog)
            "tcha": "whatever",###quando o len(tcha)=0 ativa a feature do easter egg
            "aqua": "whatever",###quando o len(aqua)=0 ativa a feature do medalhao de agua
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
                "key": "whatever",###quando o len(key)=0 ativa a feature da sala secreta na biblioteca(hot dog)
                "tcha": "whatever",###quando o len(tcha)=0 ativa a feature do easter egg
                "aqua": "whatever",###quando o len(aqua)=0 ativa a feature do medalhao de agua
                "opcoes": {
                        "inicio": "voltar pra rua",
                        "biblioteca": "ir para a biblioteca buscar pistas",
                        "elevador": "ir pro elevador para procurar o professor"
            }
        },
        "predio 2": {
                "titulo": "A grande inundação",
                "descricao": "Na entrada do predio 2 vc percebe que esta tudo inundado",
                "key": "whatever",###quando o len(key)=0 ativa a feature da sala secreta na biblioteca(hot dog)
                "tcha": "whatever",###quando o len(tcha)=0 ativa a feature do easter egg
                "aqua": {},###       MEDALHAO DE AGUA ATIVADO
                "opcoes": {"inicio": "voltar pra rua"}
        },            
        "biblioteca": {
            "titulo": "A casa dos livros",
            "descricao": "Voce sente um cheiro misterioso e quente vindo de uma das salas do fundao!",
            "key": "whatever",###quando o len(key)=0 ativa a feature da sala secreta na biblioteca(hot dog)
            "tcha": "whatever",###quando o len(tcha)=0 ativa a feature do easter egg
            "aqua": "whatever",###quando o len(aqua)=0 ativa a feature do medalhao de agua
            "opcoes": {
                "sala misteriosa": "ir investigar o cheiro misterioso",
                
                "predio 1": "voltar para o saguao de entrada do predio 1"
            }
        },
        "sala misteriosa": {
            "titulo": "O cachorro quente magico",
            "key": "whatever",###quando o len(key)=0 ativa a feature da sala secreta na biblioteca(hot dog)
            "tcha": "whatever",###quando o len(tcha)=0 ativa a feature do easter egg
            "aqua": "whatever",###quando o len(aqua)=0 ativa a feature do medalhao de agua
            "descricao": "Voce ve um cachorro quente cheiroso e quentinho em cima da mesa.                                        "
                         "Voce pode come-lo para ganhar alguma habilidade especial...                                        "
                         "ou talvez deixa-lo la ja que ele nao é seu...                                       ",
            "opcoes": {
                "comer": "encher a pança com esse delicioso cachorro quente",
                "biblioteca": "voltar para a Biblioteca"
              }
        },
        "comer": {#O que acontecera a seguir depende do randint por isso nao importa descricao e opcoes.
            "titulo": "Sorte ou Azar?",
            "descricao": "whatever",
            "key": {},###     ATIVA A SALA SECRETA
            "tcha": "whatever",###quando o len(tcha)=0 ativa a feature do easter egg
            "aqua": "whatever",###quando o len(aqua)=0 ativa a feature do medalhao de agua
            "opcoes": {
                "biblioteca": "voltar para a Biblioteca"
              }
        },
        "5 andar": {
            "titulo": "O andar da comida cara",
            "key": "whatever",###quando o len(key)=0 ativa a feature da sala secreta na biblioteca(hot dog)
            "tcha": "whatever",###quando o len(tcha)=0 ativa a feature do easter egg
            "aqua": "whatever",###quando o len(aqua)=0 ativa a feature do medalhao de agua
            "descricao": "Voce sente um cheiro maravilhoso de comida ao sair do elevador.                                        "
                         "Voce avista alguem de costas que parece ser o seu professor...                                        "
                         "Mas não dá pra você enxergar direito, talvez se vc chegar mais perto...                                       ",
            "opcoes": {
                "prof": "ir falar o professor",
                "elevador": "voltar para o elevador"
              }
        },

        "prof": {

            "titulo": "O comilão",
            "key": "whatever",###quando o len(key)=0 ativa a feature da sala secreta na biblioteca(hot dog)
            "tcha": "whatever",###quando o len(tcha)=0 ativa a feature do easter egg
            "aqua": "whatever",###quando o len(aqua)=0 ativa a feature do medalhao de agua
            "descricao": "Voce se aproxima do professor rapidamente.                                                 "
                         "Voce escorrega em um cubo de gelo e sai deslizando pelo chão...                                        "
                         "Ao se aproximar do professor voce percebe que na verdade é só mais um gordinho almoçando!"
                         "Voce entao cai no prato de comida do comilão e ele literalmente te come!                                       ",
            "opcoes": {}
        },

        "cobertura": {
            "titulo": "A vista dos ceus",
            "key": "whatever",###quando o len(key)=0 ativa a feature da sala secreta na biblioteca(hot dog)
            "tcha": "whatever",###quando o len(tcha)=0 ativa a feature do easter egg
            "aqua": "whatever",###quando o len(aqua)=0 ativa a feature do medalhao de agua
            "descricao": "Voce observa uma linda vista daqui de cima...                                              "
                         "Da uma vontadezinha de pular...                                                         "
                         "Mas não, isso seria loucura...                                                            ",
            "opcoes": {
                "pular": "se jogar de cabeça pelo precipicio",
                "elevador": "voltar para o elevador"
              }
        },
        "pular": {
            "titulo": "O voo setentrional",
            "key": "whatever",###quando o len(key)=0 ativa a feature da sala secreta na biblioteca(hot dog)
            "tcha": "whatever",###quando o len(tcha)=0 ativa a feature do easter egg
            "aqua": "whatever",###quando o len(aqua)=0 ativa a feature do medalhao de agua
            "descricao": "Um jato de vento subitamente rasga voçê por dentro.                                        "
                         "O que era para durar segundos dura uma eternidade...                                        "
                         "Você percebe um portal se formando...                                       ",
            "opcoes": {
                "morrer": "morrer estatelado no chão",
                "portal": "se encolher e atravessar o portal"
              }
        },
        "portal": {
            "titulo": "Voo interdimensional",
            "key": "whatever",###quando o len(key)=0 ativa a feature da sala secreta na biblioteca(hot dog)
            "tcha": "whatever",###quando o len(tcha)=0 ativa a feature do easter egg
            "aqua": "whatever",###quando o len(aqua)=0 ativa a feature do medalhao de agua
            "descricao": {},###       DESCRICAO VAZIA PARA ATIVAR O PORTAL
            "opcoes": {
                "prof": "ir falar o professor",
                "elevador": "voltar para o elevador"
              }
        },
        "easter egg": {#O que acontecera a seguir depende do tcha por isso nao importa descricao e opcoes.
            "titulo": "Parabens vc encontrou o Easter Egg escondido!",
            "key": "whatever",###quando o len(key)=0 ativa a feature da sala secreta na biblioteca(hot dog)
            "tcha": {},###   ATIVA O EASTER EGG
            "aqua": "whatever",###quando o len(aqua)=0 ativa a feature do medalhao de agua
            "descricao": "Voce sente um cheiro maravilhoso de comida ao sair do elevador.                                        "
                         "Voce avista alguem de costas que parece ser o seu professor...                                        "
                         "Mas não dá pra você enxergar direito, talvez se vc chegar mais perto...                                       ",
            "opcoes": {
                "prof": "ir falar o professor",
                "elevador": "voltar para o elevador"
              }
        },

        "elevador": {
            "titulo": "Caixote de metal",
            "key": "whatever",###quando o len(key)=0 ativa a feature da sala secreta na biblioteca(hot dog)
            "tcha": "whatever",###quando o len(tcha)=0 ativa a feature do easter egg
            "aqua": "whatever",###quando o len(aqua)=0 ativa a feature do medalhao de agua
            "descricao": "Voce esta no elevador",
            "opcoes": {
                "inicio": "voltar para o saguao de entrada",
                "5 andar": "ir para o andar da comida",
                "cobertura": "observar a vista"
                
            }
        }
    }
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual 


cenarios, cenario_atual = carregar_cenarios()


###Jogo central:


while not game_over:
    
    medalhao_3_elementos = medalhoes(medalhao_fogo, medalhao_agua, medalhao_neve)#checa se vc conseguiu os 3 medalhoes
    
    cenario_atual = cenarios[cenario_atual]
    
    sala_key = cenario_atual["key"]#parte da feature de sorte e azar
    
    descricao = cenario_atual["descricao"]#parte da feature do portal
    
    sala_easter = cenario_atual["tcha"]#parte da feature do easter egg
    
    aqua_medalhao = cenario_atual["aqua"]#parte da feature do medalhao de agua

    spawn_monster = random.randint(0, 1001)

#Feature de monstros aleatorios
    if spawn_monster < 899:
        print()
    
    
#Feature sorte/azar

    elif len(sala_key) == 0 and comeu == False:###Primeira feature(Sorte ou Azar?)
        sorte = random.randint(0, 1001)
        if sorte < 801:
            print('Nome da sala:"comer"')
            print("Ao comer o cahorro quente vc sente uma gosma se formar no fundo do seu estomago!")
            print("Você então cospe essa gosma e um pedaço atinge sua camisa se tornando um simbolo de fogo")
            print("")
            print("Parabens {0}!".format(player))
            print("Você adiquiriu o medalhão do fogo!")
            cenario_atual = "biblioteca"
            del cenarios["biblioteca"]["descricao"]
            cenarios["biblioteca"]["descricao"] = "Uma biblioteca agora vazia e monotona!"
            del cenarios["biblioteca"]["opcoes"]
            cenarios["biblioteca"]["opcoes"] = {"predio 1": "voltar para o saguao de entrada do predio 1"}
            comeu = True
            Medalhao_fogo = True

        else:
            print("Inspetora: É proibido comer na biblioteca!")
            print("Inspetora: Vá agora para o Multiinsper!")
            print("Você fica preso lá por 4 horas o que te faz não encontrar o professor!")
            time.sleep(1)
            game_over = True

#Sala que só curiosos vao encontrar

    elif len(sala_key) == 0 and comeu == True: 
        print("Olha só temos um espertinho por aqui!")#a unica maneira de se chegar aqui é com o portal!
        print("Parabens {0}, vc ganhou o medalhao dos 3 elementos completo!".format(player))
        print("Sugestão: pule novamente {0}!".format(player))
        time.sleep(3)
        cenario_atual = "biblioteca"
        medalhao3_elementos = True

#Portal

    elif len(descricao) == 0:
        
        if medalhao_3_elementos == True or medalhao3_elementos == True:
            cenario_atual = "easter egg"
        else:
            print("Você percebe que pode ir pra qualquer lugar desde que saiba o nome dele!")
            print("Pra onde você quer ir?")
            destino = input("-")
            while destino not in cenarios:
                print("Destino invalido")
                destino = input("-")
            cenario_atual = destino

#Easter egg:

    elif len(sala_easter) == 0:
        print("Parabens vc achou o easter egg secreto!")
        print("Esse jogo foi criado pelo Maulem e pelo ThiagoD!")
        print("Obrigado por jogar o nosso jogo {0}!".format(player))
        time.sleep(5)
        print(death(True))
        print("")
        print("Zoeira o jogo ainda não acabou!")
        print("")
        print("Você percebe que pode ir pra qualquer lugar desde que saiba o nome dele!")
        print("Pra onde você quer ir?(se nao lembrar de nenhum digita 'inicio')")
        destino = input("-")
        while destino not in cenarios:
            print("Destino invalido")
            destino = input("-")
        cenario_atual = destino

#Quando vc entra no predio 2

    elif len(aqua_medalhao) == 0:
        print("")
        print("Você entra no predio e percebe uma inundacao!")
        print("Um monstro sobe no seu peito formando um simbolo de agua")
        print("Você adiquiriu o medalhão de agua!")
        cenario_atual = "inicio"
        del cenarios["inicio"]["opcoes"]
        cenarios["inicio"]["opcoes"] = {"predio 1": "entrar no predio 1"}
        del cenarios["inicio"]["descricao"]
        cenarios["inicio"]["descricao"] = "Ja que o predio 2 ta inundado só resta o predio 1!"
        Medalhao_agua = True

#Jogo normal qdo nao acontece nada de diferente

    else:
        print("")
        print("{0}.".format(cenario_atual["titulo"]))
        print("-" * len(cenario_atual["titulo"]))
        print(cenario_atual["descricao"])
        print("")
        print("Suas opcoes são:")
        for chave in cenario_atual["opcoes"]:
            print("Digite: {0}{1}{2} para {3}.".format(aspas, chave, aspas, cenario_atual["opcoes"][chave]))

        opcoes = cenario_atual["opcoes"] 
        if len(opcoes) == 0:
            print("Acabaram-se suas opções {0}!".format(player))
            time.sleep(5)
            game_over = True
        else:
            escolha = input("-")

        while escolha not in opcoes and contador < 4:
            if contador < 4:
                print("Escolha invalida!")
                escolha = input("-")
                contador+=1
            else:
                print("Que pena {0}! Acabaram as suas chances!".format(player))
                game_over = True
        if contador >= 4:
            print("Que pena {0}! Você morreu!".format(player))
            time.sleep(1)
            game_over = True
        else:
            cenario_atual = escolha
            contador = 0

print(death(True))
























































