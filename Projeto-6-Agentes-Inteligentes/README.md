# Projeto 6 - Agentes Inteligentes: Simulação de Mercado de Jogos Digitais

Este projeto implementa uma **Simulação de Mercado Virtual** utilizando agentes inteligentes com a biblioteca AutoGen. O objetivo é demonstrar conceitos de agentes autônomos interagindo em um ambiente de mercado, onde jogadores tomam decisões de compra e venda e o mercado ajusta preços conforme oferta e demanda.

## Estrutura do Projeto

- **`market_simulation.py`**: Implementa toda a lógica dos agentes (jogadores e mercado) e a simulação das rodadas.

## Funcionalidades

1. **Agentes Inteligentes com AutoGen**:

   - Cada agente é uma instância de uma classe baseada em `autogen.Agent`.

2. **Jogadores Autônomos**:

   - Cada jogador decide de forma autônoma se irá comprar, vender ou esperar, com base no preço do mercado, saldo e itens disponíveis, incluindo um fator de aleatoriedade.

3. **Mercado Dinâmico**:

   - O agente Mercado ajusta o preço dos itens a cada rodada, de acordo com a diferença entre compras e vendas (oferta e demanda).

4. **Simulação de Rodadas**:

   - A cada rodada, todos os jogadores tomam decisões, o mercado ajusta o preço e o novo valor é exibido.

5. **Parâmetros Ajustáveis**:
   - É possível alterar o preço inicial, saldo dos jogadores, número de rodadas e estratégias de decisão para experimentação.

## Requisitos

- Python 3.8 ou superior.
- Biblioteca [pyautogen](https://pypi.org/project/pyautogen/):

  ```bash
  pip install pyautogen
  ```

## Como Executar

1. Clone o repositório ou copie o arquivo para sua máquina.
2. Instale a dependência:

   ```bash
   pip install pyautogen
   ```
3. Execute o arquivo principal:

   ```bash
   python market_simulation.py
   ```
4. Para testar diferentes configurações, altere os parâmetros no início do arquivo `market_simulation.py`.

## Exemplo de Saída

```
--- Round 1 ---
Player0: ação = wait, saldo = 100, itens = 0
Player1: ação = buy, saldo = 92, itens = 1
Player2: ação = buy, saldo = 92, itens = 1
Compras: 2, Vendas: 0
Preço do mercado: 9

--- Round 2 ---
Player0: ação = buy, saldo = 83, itens = 1
Player1: ação = wait, saldo = 92, itens = 1
Player2: ação = wait, saldo = 92, itens = 1
Compras: 1, Vendas: 0
Preço do mercado: 10

... (demais rodadas)
```

## Observações

- O código é totalmente ajustável: basta modificar as variáveis no início do arquivo para testar diferentes cenários.
- O uso da biblioteca AutoGen permite expandir facilmente para outros tipos de agentes ou regras de mercado.
- O projeto pode ser expandido para incluir mais tipos de agentes, itens ou estratégias de negociação.

## 🔗 Link para o vídeo de explicação

[]()

---

Projeto desenvolvido por João Pedro Alves Carneiro Valadão e Michel Alexandrino de Souza para a disciplina Inteligência Artificial, Universidade Federal de Lavras.
