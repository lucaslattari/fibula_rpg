# Fibula RPG

Um projeto de RPG em Python que utiliza conceitos básicos de programação para criar uma experiência interativa de combate, progressão e exploração. 

## Requisitos do Jogo

### Título e Boas-Vindas
- Ao iniciar o jogo, exiba um título e uma mensagem de boas-vindas com um elemento visual ASCII.

### Criação de Personagem
- O jogador deve informar seu nome ao iniciar o jogo.
- O personagem deve começar com os seguintes atributos:
  - **HP (pontos de vida):** 100
  - **Level (nível):** 1
  - **Força:** 3
  - **EXP (experiência):** 0
  - **Inventário:** vazio
  - **Status:** vivo

### Sistema de Combate
- O jogador pode enfrentar monstros sorteados com base no nível do personagem.
- Cada monstro possui os atributos: nome, HP, força e experiência concedida ao ser derrotado.
- Durante o combate, ataques podem causar dano com base na força e sorte de ambos os lados.
- Ações disponíveis para o jogador:
  - **Atacar:** causar dano ao monstro.
  - **Usar item:** consumir itens do inventário, como poções que recuperam HP.
  - **Fugir:** tentar escapar da batalha.
  - **Visualizar status:** exibir os atributos do jogador.
  - **Sair do jogo:** encerrar a partida.

### Progressão do Personagem
- Ao derrotar um monstro, o jogador recebe pontos de experiência e pode subir de nível.
- Subir de nível:
  - Restaura o HP.
  - Dobra a força.
  - Redefine a experiência necessária para o próximo nível.

### Itens e Inventário
- Há uma chance de o jogador receber uma poção ao derrotar um monstro.
- Poções podem ser usadas para recuperar HP.

### Fim de Jogo
- O jogo termina se o jogador perder todo o HP ou optar por sair.
- Exiba uma mensagem de "Game Over" ao final do jogo.

## Requisitos Técnicos
- Utilize funções para organizar as diferentes funcionalidades do jogo, como combate, criação de personagem e sorteio de monstros.
- Utilize a biblioteca `random` para eventos aleatórios, como a sorte dos ataques e o sorteio de monstros.

## Conceitos de Python Abordados
- **Importação de Módulos:** `import random`
- **Trabalhando com Strings e Impressão:** `print`, multi-line strings, raw strings
- **Definição e Chamada de Funções:** `def`, `return`
- **Variáveis e Tipos de Dados:** `str`, `int`, `list`, `bool`
- **Entrada de Dados do Usuário:** `input()`
- **Estruturas de Dados:** Listas
- **Estruturas Condicionais:** `if`, `elif`, `else`
- **Laços de Repetição:** `while`
- **Funções com Parâmetros e Retorno de Valores**
- **Manipulação de Listas:** Adicionar, Remover, Iterar
- **Geração de Números Aleatórios:** `random.choice()`, `random.randint()`, `random.random()`
- **Formatação de Strings Avançada:** f-strings
- **Gerenciamento de Estado do Programa:** `if __name__ == "__main__":`
- **Conceitos Avançados (Opcional):** Programação Orientada a Objetos, Manipulação de Arquivos, etc.

## Sobre o Projeto
Este jogo foi projetado como um exercício para reforçar habilidades de programação em Python, com foco em conceitos essenciais. Novos recursos e funcionalidades podem ser adicionados para torná-lo ainda mais completo e divertido!
