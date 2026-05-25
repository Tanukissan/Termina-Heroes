import random as rng
import os
import time as T

img_prota = "(˶ᵔᗜᵔ˶)ﾉﾞ" 
img_inimigo = ""

personagem={"ATK": rng.randint(1, 5),
            "DEF": rng.randint(1, 5), 
            "INT": rng.randint(1, 5), 
            "CHAR":rng.randint(1, 5), 
            "ESQ":5, 
            "HP":10, 
            "MP":10}

enemy = {"ATK": rng.randint(1, 5),
         "DEF": rng.randint(1, 5), 
         "INT": rng.randint(1, 5), 
         "CHAR":rng.randint(1, 5), 
         "ESQ": 5, 
         "HP": 10, 
         "MP": 6}

def limpar():
    os.system('cls' if os.name == 'nt' else 'clear')

def espera(segundos):
    T.sleep(segundos)

def combate(jogador, inimigo):
    print(f"{jogador} está enfrentando {inimigo}!")
    # Lógica de combate aqui
    resposta = 0
    
    while inimigo["HP"] > 0 and jogador["HP"] > 0:
        while resposta not in [1, 2]:
         if resposta == 2:
            jogador["DEF"] -= 2  # Remove o bônus de defesa temporário
        
         if acao_inimigo == "defender":
            inimigo["DEF"] -= 2  # Remove o bônus de defesa temporário
        
         print("============================================" \
            f"\n HP: {jogador['HP']}  {img_prota}   vs   {img_inimigo}  HP: {inimigo['HP']}" \
             "\n============================================" )
         print("Escolha sua ação: " \
            "\n1. Atacar / 2. Defender"
            "\n (╹ -╹)?  ")
         resposta = int(input("Digite o número da sua escolha: "))

         if resposta == 1:
            esquiva = rng.randint(1, 100)
            if esquiva <= inimigo["ESQ"]:
                print(f"{inimigo} conseguiu esquivar do ataque!")
            else:
                dano = max(0, rng.randint(jogador["ATK"]-1, jogador["ATK"]+1) - inimigo["DEF"])
                inimigo["HP"] -= dano
                print(f"{jogador} atacou e causou {dano} de dano!")
         elif resposta == 2:
            print(f"{jogador} se defende, reduzindo o dano do próximo ataque!")
            jogador["DEF"] += 2  # Aumenta a defesa temporariamente
         else:
            print("Opção inválida! Tente novamente.")
        
        espera(3)
        limpar()

        acao_inimigo = rng.choice(["atacar", "defender"])
        if acao_inimigo == "atacar":
            esquiva = rng.randint(1, 100)
            if esquiva <= jogador["ESQ"]:
                print(f"{jogador} conseguiu esquivar do ataque!")

            else:
                dano = max(0, rng.randint(inimigo["ATK"]-1, inimigo["ATK"]+1) - jogador["DEF"])
                jogador["HP"] -= dano
                print(f"{inimigo} atacou e causou {dano} de dano!")

        elif acao_inimigo == "defender":
            print(f"{inimigo} se defende, reduzindo o dano do próximo ataque!")
            inimigo["DEF"] += 2  # Aumenta a defesa temporariamente 
    
    if jogador["HP"] <= 0:
        return False
    else:
        return True
        


print(f"Seja bem-vindo ao Termina Heroes!" \
"\nVocê poderá se aventurar em um mundo de fantasia que existe dentro de seu terminal," \
"\nrepleto de monstros e eventos misteriosos..." \
"\n" \
"\n Este será o seu personagem {img_prota} , poderia dar um nome a ele?")

jogador = input("Digite o nome do personagem: ")

print(f"Certo, o nome dele será {jogador} a partir de agora! ദ്ദി(ᵔᗜᵔ)")

limpar()

print(f"Olá, {jogador}! Vamos começar a criar seu personagem." \
       "\nConfira os atributos do seu personagem logo abaixo:")

for atributo, valor in personagem.items():
    print(f"{atributo}: {valor}")

print("Gostaria de seguir com esses valores ou prefere alterar algum pelo sistema de pontos?" \
      "\n*No sistema de pontos você terá 10 pontos para distribuir "
      "\n(máx/5 p/ atributo)")
resposta = input("Seguir com estes atributos? (S/n): ")

if resposta.lower() == 'n':
    pontos = 10
    contador = 0
    limpar()
    print(f"Ótimo, {jogador}! Você tem {pontos}")

    for atributo in list(personagem.keys())[:4]:
        personagem[atributo] = int(input(f"{atributo}: "))
            
        if personagem[atributo] > 5 or personagem[atributo] < 1:
            print("Valor inválido! O valor deve ser entre 1 e 5.")
            personagem[atributo] = int(input(f"{atributo}: "))
        pontos -= personagem[atributo]

        if pontos < 0:
            print("Você excedeu o número de pontos disponíveis! Tente novamente.")
            pontos += personagem[atributo]
            personagem[atributo] = int(input(f"{atributo}: "))

        print(f"Pontos restantes: {pontos}")
        contador += 1

        if contador >= 4:
            break

print("Atributos finais do personagem:")
for atributo, valor in personagem.items():
    print(f"{atributo}: {valor}")

print(f"Ótimo, {jogador}! Agora que seu personagem está pronto, vamos começar a aventura!")

espera(4)
limpar()

print(f"{jogador} está neste momento acampando na floresta dos arredores da cidade de Initia." \
        "\nDevido a recente aparição de um dragão na região, o portão da cidade está fechado, o que faremos?" \
        "\n1. Tentar entrar na cidade pela força." \
        "\n2. Procurar por uma rota alternativa para entrar na cidade." \
        "\n3. Pedir ajuda a alguém.")

print("  (╹ -╹)?  ")

resposta = int(input("Digite o número da sua escolha: "))
espera(2)

if resposta == 1:
    print(f"Então {jogador} se dirige até o portão da cidade." \
            "\nAo chegar lá ele se depara com um único cão de guarda amarrado do lado de fora, dormindo tranquilamente..." \
            "\n    ∘ ∘ ∘ ( °ヮ° ) ?                 zᶻ ૮˶- ﻌ -˶ა⌒)ᦱ " \
            "\n ")
    resposta = int(input("O que você faz? (1. Atacar o cão de guarda / 2. Tentar passar despercebido): "))
    espera(2)

    if resposta == 1:
        limpar()
        if personagem["ATK"] > 5:
            print(f"{jogador} ataca o cão de guarda e consegue derrotá-lo facilmente! Ele entra na cidade sem problemas.")
        else:
            print(f"{jogador} ataca o cão de guarda, mas mesmo ferido ele consegue revidar!")
            img_inimigo = "૮ • ﻌ - ა ⌒)ᦱ"
            if combate(personagem, {"ATK": 3, "DEF": 2, "INT": 1, "CHAR": 1, "ESQ": 5, "HP": 5, "MP": 0}) == False:
                print("Infelizmente, você foi derrotado pelo cão de guarda... Fim de jogo!")
            else:
                print(f"{jogador} conseguiu derrotar o cão de guarda e entra na cidade!")
    




