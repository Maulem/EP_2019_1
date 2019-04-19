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



def carregar_cenarios():
    cenarios = {
        "inicio": {
            "titulo": "Saguao do perigo",
            "descricao": "Voce esta no saguao de entrada do insper",
            "opcoes": {
                "andar professor": "Tomar o elevador para o andar do professor",
                "biblioteca": "Ir para a biblioteca"
            }
        },
        "andar professor": {
            "titulo": "Andar do desespero",
            "descricao": "Voce chegou ao andar da sala do seu professor",
            "opcoes": {
                "inicio": "Tomar o elevador para o saguao de entrada",
                "professor": "Falar com o professor"
            }
        },
        "professor": {
            "titulo": "O monstro do Python",
            "descricao": "Voce foi pedir para o professor adiar o EP. "
                         "O professor revelou que é um monstro disfarçado "
                         "e devorou sua alma.",
            "opcoes": {}
        },
        "biblioteca": {
            "titulo": "Caverna da tranquilidade",
            "descricao": "Voce esta na biblioteca",
            "opcoes": {
                "inicio": "Voltar para o saguao de entrada"
            }
        }
    }
    nome_cenario_atual = "inicio"
    return cenarios, nome_cenario_atual

aspas = '"'
def main():
    print("Na hora do sufoco!")
    print("------------------")
    print()
    print("Parecia uma boa idéia: vou só jogar um pouquinho/assistir Netflix/"
        "embaçar em geral. Amanhã eu começo o EP. Mas isso não deu certo...")
    print()
    print("É o dia de entregar o EP e você está muuuuito atrasado! Você está "
        "na entrada do Insper, e quer procurar o professor para pedir um "
        "adiamento do EP (boa sorte...)")
    print()

    cenarios, nome_cenario_atual = carregar_cenarios()

    game_over = False
    while not game_over:
        cenario_atual = cenarios[nome_cenario_atual]

        print("")
        print(cenario_atual["titulo"])
        print("-" * len(cenario_atual["titulo"]))
        print(cenario_atual["descricao"])
        print("")
        print("Suas opcoes são:")
        for chave in cenario_atual["opcoes"]:
            print("Digite: {0}{1}{2} para {3}".format(aspas, chave, aspas, cenario_atual["opcoes"][chave]))

        opcoes = cenario_atual['opcoes']
        if len(opcoes) == 0:
            print("Acabaram-se suas opções! Mwo mwo mwooooo...")
            game_over = True
        else:
            escolha = input("-")
            if escolha in opcoes:
                nome_cenario_atual = escolha
            else:
                print("Sua indecisão foi sua ruína!")
                game_over = True

    print("Você morreu!")


# Programa principal.
if __name__ == "__main__":
    main()
