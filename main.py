import random

# Função para exibir o título de abertura
def mostrar_titulo():
    title = r"""
                    //    \
                   ((     ))
               ===  \_v_//  ===
 Art by          ====)_^_(====
Roland Waylor    ===/ O O \===
                 = | /_ _\ | =
                =   \/_ _\/   =
                     \_ _/
                     (o_o)
                      VwV
    """
    print(title)
    print("Bem-vindo ao FIBULA RPG!")


# Função para iniciar um novo jogo
def iniciar_novo_jogo():
    nome = input("Qual o seu nome? ")
    hp = 100
    lv = 1
    forca = 3
    exp = 0
    inventario = []
    status = True  # Vivo ou morto?

    return nome, hp, lv, forca, exp, inventario, status


# Função para sortear um monstro
def sortear_monstro(jogador_lv):
    # Lista de monstros: [nome, hp, força, exp]
    slime = ["slime", 10, 2, 10]
    goblin = ["goblin", 20, 4, 20]
    troll = ["troll", 40, 8, 40]
    orc = ["orc", 80, 16, 80]
    mumia = ["múmia", 160, 32, 160]
    quimera = ["quimera", 320, 64, 320]
    dragao = ["dragão", 1000, 100, 1000]

    if jogador_lv < 5:
        return random.choice([slime, goblin, troll])
    elif jogador_lv < 10:
        return random.choice([troll, orc, mumia, quimera])
    else:
        return dragao


# Função para exibir game over
def game_over():
    print("O jogo acabou.")
    print("Obrigado por jogar!")
    exit(1)

# Função para o ataque do jogador ou inimigo
def ataque(atacante_nome, atacante_forca, defensor_nome, defensor_hp, defensor_forca):

    atacante_sorte  = random.randint(0, 6)
    defensor_sorte  = random.randint(0, 6)

    if atacante_sorte == 6:
        print(f"O {atacante_nome} acertou um ataque crítico!")
    elif atacante_sorte > 0:
        print(f"O {atacante_nome} acertou um ataque!")
    else:
        print(f"O {atacante_nome} errou o golpe!")

    dano = atacante_forca * atacante_sorte - defensor_forca * defensor_sorte

    if dano > 0:
        print(f"O {defensor_nome} sofreu um dano de {dano}")
        defensor_hp = defensor_hp - dano
    else:
        print(f"O {defensor_nome} não sofreu dano!")

    if defensor_hp <= 0:
        print(f"O {defensor_nome} morreu!")
        return 0, False # Defensor morreu
    else:
        return defensor_hp, True # Defensor está vivo

# Função para calcular o level up
def calcular_level(jogador_lv, jogador_exp, jogador_hp, jogador_forca, exp_monstro):
    jogador_exp = jogador_exp + exp_monstro
    experiencia_necessaria = 3**jogador_lv

    if jogador_exp > experiencia_necessaria:  # Subiu de level?
        print("Level up!")
        jogador_lv += 1
        jogador_hp = 100
        jogador_forca = jogador_forca * 2

    return jogador_lv, jogador_exp, jogador_hp, jogador_forca


# Função para obter uma poção
def obter_pocao():
    chance = random.random()
    if chance <= 0.2:
        print("Você ganhou uma poção!")
        return "Poção"
    else:
        return None
    
# Função para usar item
def usar_item(jogador_inventario, jogador_hp):
    if not jogador_inventario:  # Inventário vazio
        print("Seu inventário está vazio!\n")
    else:
        print("Inventário:")
        for index, item in enumerate(jogador_inventario):
            print(f"{index + 1}. {item}")
        opcao_item = int(input("Escolha o item (ou 0 para cancelar): "))
        if opcao_item == 0:
            print("\n")
        else:
            item_escolhido = jogador_inventario[opcao_item - 1]
            if item_escolhido == "Poção":
                print("Você usou uma poção!")
                jogador_hp += 20
                if jogador_hp > 100:
                    jogador_hp = 100
                print(f"Seu HP agora é {jogador_hp}\n")
                jogador_inventario.pop(opcao_item - 1)
            else:
                print("Item inválido!\n")
    return jogador_hp, jogador_inventario

# Função para fugir
def fugir(jogador_nome):
    sucesso = random.choice([True, False])
    if sucesso:
        print(f"{jogador_nome} fugiu com sucesso!\n")
        return True  # Fugiu com sucesso
    else:
        print(f"{jogador_nome} não conseguiu escapar!\n")
        return False  # Não conseguiu fugir

# Função principal do jogo
def main():
    mostrar_titulo()
    jogador_nome, jogador_hp, jogador_lv, jogador_forca, jogador_exp, jogador_inventario, jogador_status = iniciar_novo_jogo()
    print("\n")

    jogador_enfrentando_monstro = False

    while True:
        if not jogador_enfrentando_monstro:
            monstro_nome, monstro_hp, monstro_forca, monstro_exp = sortear_monstro(jogador_lv)
            
            print(f"\nUm {monstro_nome} aleatório aparece!")
            print(f"HP: {monstro_hp}\n")
            jogador_enfrentando_monstro = True
            monstro_vivo = True
        else:
            print(f"\nVocê está enfrentando um {monstro_nome}!")
            print(f"HP: {monstro_hp}\n")

        print(f"{jogador_nome}: {jogador_hp}/100")
        print(f"Level: {jogador_lv}")
        print("O que você deseja fazer?")
        print("1. Atacar")
        print("2. Usar item")
        print("3. Fugir")
        print("4. Visualizar status")
        print("5. Sair do jogo")
        opcao = int(input())

        if opcao == 1:
            print("\n")
            # Jogador ataca o monstro
            monstro_hp, monstro_vivo = ataque(jogador_nome, jogador_forca, monstro_nome, monstro_hp, monstro_forca)
            print("\n")
            if monstro_vivo:
                # Monstro ataca o jogador
                jogador_hp, jogador_vivo = ataque(monstro_nome, monstro_forca, jogador_nome, jogador_hp, jogador_forca)
                print("\n")
                if not jogador_vivo:
                    game_over()
            else:
                # Jogador ganhou experiência
                print(f"Você ganhou {monstro_exp} XP!")
                jogador_lv, jogador_exp, jogador_hp, jogador_forca = calcular_level(jogador_lv, jogador_exp, jogador_hp, jogador_forca, monstro_exp)
                # Pode ganhar item
                pocao = obter_pocao()
                if pocao is not None:
                    jogador_inventario.append(pocao)
                jogador_enfrentando_monstro = False
                continue
        elif opcao == 2:
            jogador_hp, jogador_inventario = usar_item(jogador_inventario, jogador_hp)
            continue
        elif opcao == 3:
            fugiu = fugir(jogador_nome)
            if fugiu:
                jogador_enfrentando_monstro = False
                continue
            else:
                # Monstro ataca o jogador
                jogador_hp, jogador_vivo = ataque(monstro_nome, monstro_forca, jogador_nome, jogador_hp, jogador_forca)
                print("\n")
                if not jogador_vivo:
                    game_over()
        elif opcao == 4:
            print(f"\n{jogador_nome}")
            print(f"HP: {jogador_hp/100}")
            print(f"LV: {jogador_lv}")
            print(f"EXP: {jogador_exp}")
            exp_proximo_nivel = 5 ** jogador_lv
            print(f"Falta {exp_proximo_nivel - jogador_exp} XP para evoluir")
            print(f"Força: {jogador_forca}")
            print(f"Inventário: {jogador_inventario}\n")
            continue
        elif opcao == 5:
            game_over()
        else:
            print("Opção inválida!\n")
            continue

if __name__ == "__main__":
    main()
