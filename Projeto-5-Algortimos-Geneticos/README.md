# Projeto 5 - Algoritmos Genéticos

Este projeto implementa um **Algoritmo Genético (AG)** para encontrar o valor máximo da função f(x) = x² − 3x + 4, considerando o intervalo X = [−10, +10]. O objetivo é demonstrar conceitos fundamentais de algoritmos evolutivos aplicados à otimização de funções.

## Estrutura do Projeto

- **`genetic_algorith.py`**: Implementa toda a lógica do algoritmo genético, incluindo codificação, avaliação, seleção, crossover, mutação e execução das gerações.

## Funcionalidades

1. **Codificação Binária**:

   - Cada indivíduo é representado por um vetor binário de 5 bits, mapeando para valores inteiros no intervalo [-10, 10].

2. **População Inicial Aleatória**:

   - Geração de uma população inicial de indivíduos binários de forma aleatória.

3. **Função de Fitness**:

   - Utiliza a função f(x) = x² − 3x + 4 para avaliar a qualidade de cada indivíduo.

4. **Seleção por Torneio**:

   - Seleção de pais baseada em torneios entre indivíduos, favorecendo os mais aptos.

5. **Crossover de Um Ponto**:

   - Recombinação dos genes dos pais com taxa ajustável (padrão 70%).

6. **Mutação**:

   - Cada bit do indivíduo tem uma pequena chance de ser invertido (padrão 1%).

7. **Parâmetros Variáveis**:

   - Permite ajustar facilmente o tamanho da população, número de gerações, taxa de crossover e taxa de mutação para experimentação.

8. **Execução por Gerações**:
   - O algoritmo é executado por um número definido de gerações, exibindo o melhor indivíduo de cada geração e o melhor resultado final.

## Requisitos

- Python 3.8 ou superior.
- Não são necessárias bibliotecas externas além da biblioteca padrão.

## Como Executar

1. Clone o repositório ou copie o arquivo para sua máquina.
2. Execute o arquivo principal:
   ```bash
   python genetic_algorith.py
   ```
3. Para testar diferentes configurações, altere os parâmetros no início do arquivo `genetic_algorith.py`.

## Exemplo de Saída

```
Geração 1: Melhor x = -9, Fitness = 112, Melhor Indivíduo = [0, 0, 1, 1, 0]
Geração 2: Melhor x = -9, Fitness = 112, Melhor Indivíduo = [0, 0, 0, 0, 1]
Geração 3: Melhor x = -9, Fitness = 112, Melhor Indivíduo = [0, 0, 0, 0, 1]
Geração 4: Melhor x = -9, Fitness = 112, Melhor Indivíduo = [0, 0, 0, 0, 1]
Geração 5: Melhor x = -9, Fitness = 112, Melhor Indivíduo = [0, 0, 0, 0, 1]
...
Melhor solução encontrada: x = -9, Fitness = 112, Melhor Indivíduo = [0, 0, 0, 0, 1]
```

## Observações

- O código é totalmente ajustável: basta modificar as variáveis no início do arquivo para testar diferentes cenários.
- O algoritmo pode ser expandido para outras funções ou intervalos, bastando adaptar a função de fitness e o mapeamento binário.
- O método de seleção por torneio garante diversidade e pressão seletiva adequada mesmo em populações pequenas.

## 🔗 Link para o vídeo de explicação

[]()

---

Projeto desenvolvido por João Pedro Alves Carneiro Valadão e Michel Alexandrino de Souza para a disciplina Inteligência Artificial, Universidade Federal de Lavras.
