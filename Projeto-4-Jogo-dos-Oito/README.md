# Projeto 4 - Jogo dos Oito (8-Puzzle) com Inteligência Artificial

Este projeto implementa o clássico **Jogo dos Oito (8-Puzzle)**, resolvido por dois algoritmos de busca: **Busca em Largura (BFS)** e **Busca A\***. O objetivo é demonstrar técnicas de busca cega e informada aplicadas a um problema clássico de IA, com uma interface gráfica interativa.

## Estrutura do Projeto

- **`eight_puzzle.py`**: Implementa a lógica do tabuleiro, movimentos e verificação do objetivo.
- **`search.py`**: Implementa os algoritmos de busca BFS e A\*.
- **`main.py`**: Interface gráfica com o usuário, integração dos algoritmos e interação manual.
- **Arquivos auxiliares**: (README, etc.)

## Funcionalidades

1. **Interface Gráfica Interativa (`main.py`)**:

   - Permite ao usuário jogar manualmente clicando nas peças.
   - Botões para resolver automaticamente usando BFS ou A\*.
   - Animação dos movimentos da solução encontrada.
   - Botão para resetar o tabuleiro ao estado inicial.

2. **Lógica do Tabuleiro (`eight_puzzle.py`)**:

   - Representação do tabuleiro como matriz 3x3.
   - Movimentação do espaço vazio (0) para cima, baixo, esquerda ou direita.
   - Verificação de estado objetivo.

3. **Algoritmos de Busca (`search.py`)**:
   - **Busca em Largura (BFS)**: Garante encontrar o menor caminho para a solução.
   - **Busca A\***: Utiliza a heurística da distância de Manhattan para encontrar soluções de forma mais eficiente.

## Requisitos

Certifique-se de que o Python está instalado (recomendado Python 3.8+).  
Não são necessárias bibliotecas externas além da biblioteca padrão.

## Como Executar

1. Clone o repositório:

   ```bash
   git clone https://github.com/seu-usuario/Projeto-4-Jogo-dos-Oito.git
   cd Projeto-4-Jogo-dos-Oito
   ```

2. Execute o arquivo principal:
   ```bash
   python main.py
   ```

## Como Jogar

- **Movimentação Manual:** Clique nas peças vizinhas ao espaço vazio para movê-las.
- **Resolver Automaticamente:** Clique em "Resolver (BFS)" ou "Resolver (A\*)" para ver a solução automática animada.
- **Resetar:** Clique em "Resetar" para voltar ao estado inicial.

## Exemplo de Funcionamento

- O tabuleiro inicial é exibido na tela.
- O usuário pode tentar resolver manualmente ou pedir para a IA resolver.
- A solução é mostrada passo a passo, destacando o funcionamento dos algoritmos de busca.

## Observações

- O BFS sempre encontra a solução mais curta, mas pode ser mais lento em estados complexos.
- O A\* geralmente encontra a solução mais rápido, pois utiliza uma heurística inteligente.
- O projeto pode ser facilmente adaptado para outros estados iniciais, basta alterar a variável `INITIAL_STATE` em `main.py`.

## 🔗 Link para o vídeo de explicação

[]()

---

Projeto desenvolvido por João Pedro Alves Carneiro Valadão e Michel Alexandrino de Souza para a disciplina Inteligência Artificial, Universidade Federal de Lavras.
