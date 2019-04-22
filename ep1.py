# EP 2019-1: Escape Insper
#
# Alunos: 
# - aluno A: Henrique Mualem Marti, henriquemm3@al.insper.edu.br
# - aluno B: Thiago Lopes, thiagod@al.insper.edu.br


"""
NKO Enterprises Presents: Escape Insper

Created on Tue Apr 16 16:32:14 2019

@author: Maulem and ThiagoD

Objetivos do jogo: Juntar medalhoes do fogo, da agua e da neve, transformando em um medalhao dos 3 elementos,
depois entrar no portal(pulando da cobertura do insper).
"""
###Imports:

import time
import random


###CONTROLADORES DO JOGO PARA USO DO PROFESSOR (DESATIVE TEMPO DAS ANIMACOES E DAS ACOES DO JOGO AQUI!)

t02 = 0.2 #Tempo de 0.2 segundos no time sleep  |ANIMACOES|
t05 = 0.5 #Tempo de 0.5 segundos no time sleep  |ANIMACOES|
t1 = 0.1 #Tempo de 0.1 segundos no time sleep  |ANIMACOES|
t10 = 1 #Tempo de 1 segundo no time sleep  |ANIMACOES|

tx1 = 1 #Tempo de 1 segundo no time sleep |INICIO DO JOGO|

ty1 = 1 #Tempo de 1 segundo no time sleep |QUANDO VC VIAJA DE CENARIO EM CENARIO|


###Variaveis iniciais:

game_win = 0 #500 para vencer o jogo
player = "*****" #nome inicial para evitar bugs
game_over = False #fim de jogo
comeu = False #feature sorte e itens magicos
aspas = '"' #escrever aspas no .format
medalhao_fogo = 0
medalhao_agua = 0  #os medalhoes estavam dando bug com True e False por isso ficou 0 e 1
medalhao_neve = 0
medalhao_3_elementos = False    ###sao 2 variaveis mas representam o mesmo item!
contador = 0 ###Contador de erros de digitacao
vida_player = 100
vida_boneco = 20
vida_EL_RAUL = 100
medalha_EL_RAUL = False #medalha ganha ao derrotar EL RAUL

###Animação de entrada:

time.sleep(t02)
print("Initializing...")
time.sleep(t05)
print("            ______           ______   ______    ___ ___    ______")
time.sleep(t02)
print("|       |  |        |       |        |      |  |   |   |  |      ")
time.sleep(t02)
print("|       |  |        |       |        |      |  |   |   |  |      ")
time.sleep(t02)
print("|   |   |  |----    |       |        |      |  |   |   |  |----  ")
time.sleep(t02)
print("|   |   |  |        |       |        |      |  |       |  |      ")
time.sleep(t02)
print("|___|___|  |______  |_____  |______  |______|  |       |  |______")
time.sleep(t02)



###Animacão da morte:


def death(game_over):    ###Raul perdao por botar print dentro de funcao mas nao sei como fazer para a animacao
    if game_over == True:###funcionar só usando return.
        time.sleep(t10)
        print()
        print('                  uuuuuuu')
        time.sleep(t1)
        print('             uu$$$$$$$$$$$uu')
        time.sleep(t1)
        print('           uu$$$$$$$$$$$$$$$$$uu')
        time.sleep(t1)
        print('          u$$$$$$$$$$$$$$$$$$$$$u      ')
        time.sleep(t1)
        print('         u$$$$$$$$$$$$$$$$$$$$$$$u      ')
        time.sleep(t1)
        print('        u$$$$$$$$$$$$$$$$$$$$$$$$$u     ')
        time.sleep(t1)
        print('        u$$$$$$$$$$$$$$$$$$$$$$$$$u     ')
        time.sleep(t1)
        print('        u$$$$$$"   "$$$"   "$$$$$$u     ')
        time.sleep(t1)
        print('        "$$$$"      u$u       $$$$"      ')
        time.sleep(t1)
        print('         $$$u       u$u       u$$$      ')
        time.sleep(t1)
        print('         $$$u      u$$$u      u$$$      ')
        time.sleep(t1)
        print('          "$$$$uu$$$   $$$uu$$$$"      ')
        time.sleep(t1)
        print('           "$$$$$$$"   "$$$$$$$"     ')
        time.sleep(t1)
        print('             u$$$$$$$u$$$$$$$u')
        time.sleep(t1)
        print('              u$"$"$"$"$"$"$u')
        time.sleep(t1)
        print('   uuu        $$u$ $ $ $ $u$$       uuu')
        time.sleep(t1)
        print('  u$$$$        $$$$$u$u$u$$$       u$$$$')
        time.sleep(t1)
        print('   $$$$$uu      "$$$$$$$$$"     uu$$$$$$')
        time.sleep(t1)
        print(' u$$$$$$$$$$$uu    """""    uuuu$$$$$$$$$$')
        time.sleep(t1)
        print(' $$$$"""$$$$$$$$$$uuu   uu$$$$$$$$$"""$$$"')
        time.sleep(t1)
        print('  """      ""$$$$$$$$$$$uu ""$"""')
        time.sleep(t1)
        print('            uuuu ""$$$$$$$$$$uuu')
        time.sleep(t1)
        print('   u$$$uuu$$$$$$$$$uu ""$$$$$$$$$$$uuu$$$')
        time.sleep(t1)
        print('   $$$$$$$$$$""""           ""$$$$$$$$$$$"')
        time.sleep(t1)
        print('    "$$$$$"                      ""$$$$""')
        time.sleep(t1)
        print('      $$$"                         $$$$"')
        print()
        time.sleep(t10)
        
        return "                  Game over!"

###Animação de vencer o jogo:


def win(game):        ###Raul perdao por botar print dentro de funcao mas nao sei como fazer para a animacao
    if game == True:  ###funcionar só usando return.
        time.sleep(t02)
        print("                                                        ") 
        time.sleep(t02)
        print("     \   /   ____            |       |   |   |\    |   |")
        time.sleep(t02)
        print("      \ /   |    |  |   |    |       |   |   | \   |   |")
        time.sleep(t02)    
        print("       |    |    |  |   |    |   |   |   |   |  \  |   |")
        time.sleep(t02)
        print("       |    |    |  |   |    |   |   |   |   |   \ |   |")
        time.sleep(t02)
        print("       |    |____|  |___|    |___|___|   |   |    \|   o")  
        time.sleep(t02)
        print("")
        return "Parabens!"

###Introdução ao game:


print("Bem vindo ao Escape Insper")
print("Digite o nome do seu jogador:")
player = input("Nome:")

'''print("\x1b[2J\x1b[1;1H") '''###Esse comando limpa a tela do console do usuario ##decidi nao usar porque nao sei se vc gostaria

print("") ###Esse comando pula uma linha para ficar organizado apos usar o comando acima.
print("Bem vindo {0} ao Escape Insper!".format(player))
time.sleep(tx1)
print("")
print("Descrição do jogo:")
time.sleep(tx1)
print("Você é um aluno do Insper que teve uma crise de insonia e dormiu alguns dias seguidos perdendo aulas e chegando no dia da entrega do EP.")
print("")
time.sleep(tx1)
print("Você então vai tentar pedir para o professor adiar a entrega, mas para isso primeiro vai ter que achar ele. ")
print("")
time.sleep(tx1)
print("Então boa sorte na sua jornada {0}!".format(player))
print("")
time.sleep(tx1)

###Sistema de inventarios dos medalhoes:

def medalhoes(fogo, agua, neve):
    if fogo == 1 and agua == 1 and neve == 1:
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
                "opcoes": {"inicio": "voltar pra rua"}###Opcoes nunca podem estar em branco senao eh game over!
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
            "key": {},###     |ATIVA A SALA SECRETA|
            "tcha": "whatever",###quando o len(tcha)=0 ativa a feature do easter egg
            "aqua": "whatever",###quando o len(aqua)=0 ativa a feature do medalhao de agua
            "opcoes": {
                "biblioteca": "voltar para a Biblioteca"###Opcoes nunca podem estar em branco senao eh game over!
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
        "morrer": {

            "titulo": "Morte certa",
            "key": "whatever",###quando o len(key)=0 ativa a feature da sala secreta na biblioteca(hot dog)
            "tcha": "whatever",###quando o len(tcha)=0 ativa a feature do easter egg
            "aqua": "whatever",###quando o len(aqua)=0 ativa a feature do medalhao de agua
            "descricao": "Voce se esborracha no chao.                                                         "
                         "Voce tem uma recordacao de toda a sua vida...                                                      "
                         "E percebe que talvez devesse ter pulado com os 3 medalhoes no portal!                              "
                         "Voce morre!                                       ",
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
            "descricao": {},###       |DESCRICAO VAZIA PARA ATIVAR O PORTAL|
            "opcoes": {
                "prof": "ir falar o professor",###Opcoes nunca podem estar em branco senao eh game over!
                "elevador": "voltar para o elevador"###Opcoes nunca podem estar em branco senao eh game over!
              }
        },
        "Fim": {#O que acontecera a seguir depende do tcha por isso nao importa descricao e opcoes.
            "titulo": "Parabens vc encontrou o Easter Egg escondido!",
            "key": "whatever",###quando o len(key)=0 ativa a feature da sala secreta na biblioteca(hot dog)
            "tcha": {},###       |ATIVA O FIM DO JOGO|
            "aqua": "whatever",###quando o len(aqua)=0 ativa a feature do medalhao de agua
            "descricao": "Voce sente um cheiro maravilhoso de comida ao sair do elevador.      ###Descricao nunca podem estar em branco senao ativa uma feature!                                  ",
            "opcoes": {
                "prof": "ir falar o professor",###Opcoes nunca podem estar em branco senao eh game over!
                "elevador": "voltar para o elevador"###Opcoes nunca podem estar em branco senao eh game over!
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


while not game_over and game_win != 500:
    
    medalhao_3_elementos = medalhoes(medalhao_fogo, medalhao_agua, medalhao_neve)#checa se vc conseguiu os 3 medalhoes
    
    cenario_atual = cenarios[cenario_atual]
    
    sala_key = cenario_atual["key"]#parte da feature de sorte e azar
    
    descricao = cenario_atual["descricao"]#parte da feature do portal
    
    sala_fim = cenario_atual["tcha"]#parte da feature do easter egg
    
    aqua_medalhao = cenario_atual["aqua"]#parte da feature do medalhao de agua

    spawn_monster = random.randint(0, 1001)
    
#Feature de um chefao que oferece uma dica se vc o vencer

    if spawn_monster < 60 and medalha_EL_RAUL == False:
        print("A wild mexican EL RAUL appears!")
        print("O que você pretende fazer em relação a esse mexicano que parece seu professor?")
        print('Opções: "enfrentar" ou "fugir"')
        luta = input("-")
        if luta == "enfrentar":
            print("")
            print("El RAUL tem 100 pontos de vida!")
            print("Você tem {0} pontos de vida!".format(vida_player))
            print("")
            time.sleep(2)
            while vida_player > 0 and vida_EL_RAUL >0:
                atq_player = random.randint(5, 30)
                print("")
                print("Você deu {0} de ataque!".format(atq_player))
                print("")
                time.sleep(2)
                vida_EL_RAUL -= atq_player
                if vida_EL_RAUL < 0:
                    vida_EL_RAUL = 0
                print("EL RAUL tem {0} pontos de vida!".format(vida_EL_RAUL))
                time.sleep(4)
                print("")
                print("")
                atq_EL_RAUL = random.randint(1, 20)
                print("Ele te deu {0} de dano!".format(atq_EL_RAUL))
                print("")
                time.sleep(2)
                vida_player -= atq_EL_RAUL
                if vida_player < 0:
                    vida_player = 0
                print("Você tem {0} pontos de vida!".format(vida_player))
                print("")
                time.sleep(2)
            if vida_player > 0:
                print("Após vencer EL RAUL ele decide adiar o ep e te conta uma coisa interessante!")
                print("")
                time.sleep(5)
                print("Juntando os medalhoes do Fogo, da Agua e da Neve e pulando da cobertura do insper você vera algo interessante!")
                print("")
                time.sleep(5)
                print("Apos fala isso EL RAUL some que nem fumaça!")
                print("")
                print("Voce volta misteriosamente para o inicio!")
                print("")
                time.sleep(5)
                cenario_atual = "inicio"
                medalha_EL_RAUL = True
            else:
                game_over = True
        else:
            print("Voce volta misteriosamente para o inicio!")
            print("")
            cenario_atual = "inicio"

#Feature de monstros aleatorios e combate
    elif spawn_monster < 120 and medalhao_neve == False:
        print("Um boneco de neve doidão apareceu!")
        print("Você quer enfrenta-lo ou fugir?")
        print('Opções: "enfrentar" ou "fugir"')
        luta = input("-")
        if luta == "enfrentar":
            print("")
            print("O boneco de neve tem 20 pontos de vida!")
            print("Você tem {0} pontos de vida!".format(vida_player))
            print("")
            time.sleep(2)
            while vida_player > 0 and vida_boneco >0:
                atq_player = random.randint(5, 16)
                print("")
                print("Você deu {0} de ataque!".format(atq_player))
                print("")
                time.sleep(2)
                vida_boneco -= atq_player
                if vida_boneco < 0:
                    vida_boneco = 0
                print("O boneco de neve tem {0} pontos de vida!".format(vida_boneco))
                time.sleep(4)
                print("")
                print("")
                atq_boneco = random.randint(1, 6)
                print("Ele te deu {0} de dano!".format(atq_boneco))
                print("")
                time.sleep(2)
                vida_player -= atq_boneco
                if vida_player < 0:
                    vida_player = 0
                print("Você tem {0} pontos de vida!".format(vida_player))
                print("")
                time.sleep(2)
            print("No seu ataque final vc escorrega na agua deixada pelo boneco e cai de bunda no chao!")
            print("")
            time.sleep(2)
            print("Esse pequeno tremor faz haver um disturbio na rede eletrica que torna as luzes mais intensas...")
            print("")
            time.sleep(2)
            print("O boneco de neve acaba derretendo!")
            print("")
            time.sleep(2)
            print("Fatality!")
            print("")
            time.sleep(3)
            print("Voce volta misteriosamente para o inicio com um medalhao de neve como recompensa pela sua batalha!")
            time.sleep(4)
            cenario_atual = "inicio"
            medalhao_neve = 1
        else:
            print("Voce volta misteriosamente para o inicio!")
            print("")
            cenario_atual = "inicio"

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
            medalhao_fogo = 1

        else:
            print("Inspetora: É proibido comer na biblioteca!")
            print("Inspetora: Vá agora para o Multiinsper!")
            print("Você fica preso lá por 4 horas o que te faz não encontrar o professor!")
            time.sleep(1)
            game_over = True

#Sala que só curiosos vao encontrar(Easter Egg!)

    elif len(sala_key) == 0 and comeu == True: 
        print("Olha só temos um espertinho por aqui!")#A unica maneira de se chegar aqui é com o portal! (Digite "comer")
        time.sleep(2)
        print("Parabens vc achou o Easter Egg secreto!")
        time.sleep(2)
        print("Esse jogo foi criado pelo Maulem e pelo ThiagoD!")
        time.sleep(2)
        print("Obrigado por jogar o nosso jogo {0}!".format(player))
        time.sleep(2)
        print("Parabenizamos voce pela sua inteligencia!")
        time.sleep(5)
        print(death(True))
        print("")
        print("Zoeira o jogo ainda não acabou!")
        time.sleep(2)
        print("Parabens {0}, vc ganhou o medalhao dos 3 elementos completo!".format(player))
        print("Sugestão: pule novamente {0}!".format(player))
        time.sleep(3)
        cenario_atual = "biblioteca"
        medalhao_agua = 1 
        medalhao_neve = 1 
        medalaho_fogo = 1 ###Para nao bugar o inventario

#Portal

    elif len(descricao) == 0:
        
        if medalhao_3_elementos == True:
            cenario_atual = "Fim"
        else:
            print("Você percebe que pode ir pra qualquer lugar desde que saiba o nome dele!")
            print("Pra onde você quer ir?")
            destino = input("-")
            while destino not in cenarios:
                print("Destino invalido")
                destino = input("-")
            cenario_atual = destino

#Fim do jogo(Vitoria):

    elif len(sala_fim) == 0:
        print("Parabens vc terminou o jogo!")
        print("Esse jogo foi criado pelo Maulem e pelo ThiagoD!")
        print("Obrigado por jogar o nosso jogo {0}!".format(player))
        time.sleep(5)
        print(death(True))
        print("")
        print("Zoeira o jogo ainda não acabou!")
        time.sleep(3)
        print("")
        print("Agora acabou!")
        time.sleep(3)
        print(win(True))
        game_win = 500 #condicao pra vencer o jogo

#Quando vc entra no predio 2

    elif len(aqua_medalhao) == 0:
        print("")
        print("Você entra no predio e percebe uma inundacao!")
        time.sleep(2)
        print("Um monstro sobe no seu peito formando um simbolo de agua")
        time.sleep(2)
        print("Você adiquiriu o medalhão de agua!")
        time.sleep(2)
        cenario_atual = "inicio"
        del cenarios["inicio"]["opcoes"]
        cenarios["inicio"]["opcoes"] = {"predio 1": "entrar no predio 1"}
        del cenarios["inicio"]["descricao"]
        cenarios["inicio"]["descricao"] = "Ja que o predio 2 ta inundado só resta o predio 1!"
        medalhao_agua = 1

#Jogo normal qdo nao acontece nada de diferente

    else:
        print("")
        print("Medalhões:") ###|INVENTARIO|
        print("Agua:{0}".format(medalhao_agua))
        print("Neve:{0}".format(medalhao_neve))
        print("Fogo:{0}".format(medalhao_fogo))
        print("")
        print("{0}.".format(cenario_atual["titulo"]))
        print("-" * len(cenario_atual["titulo"]))
        time.sleep(ty1)
        print(cenario_atual["descricao"])
        time.sleep(ty1)
        print("")
        print("Suas opcoes são:")
        for chave in cenario_atual["opcoes"]:
            print("Digite: {0}{1}{2} para {3}.".format(aspas, chave, aspas, cenario_atual["opcoes"][chave]))

        opcoes = cenario_atual["opcoes"] 
        if len(opcoes) == 0:
            print("Acabaram-se suas opções {0}!".format(player))
            time.sleep(ty1)
            game_over = True
        else:
            escolha = input("-")

            while escolha not in opcoes and contador < 4:
                if contador < 5:
                    print("Escolha invalida!")
                    escolha = input("-")
                    contador+=1
                else:
                    print("Que pena {0}! Acabaram as suas chances!".format(player))
                    game_over = True
        if contador >= 4:
            print("Que pena {0}! Você perdeu!".format(player))
            time.sleep(ty1)
            game_over = True
        else:
            cenario_atual = escolha
            contador = 0

#Animacao de morte            

if game_over == True:
    print(death(True))
