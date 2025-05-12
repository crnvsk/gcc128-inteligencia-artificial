# Projeto 3 - KNN e MLP Classificadores

Este projeto implementa dois algoritmos de classificação: **K-Nearest Neighbors (KNN)** e **Multi-Layer Perceptron (MLP)**. O objetivo é comparar as implementações manuais e baseadas em bibliotecas, avaliando o desempenho em dois datasets clássicos: **Iris** e **Wine**.

## Estrutura do Projeto

- **`knn.py`**: Implementação manual do algoritmo KNN.
- **`mlp.py`**: Implementação do classificador MLP utilizando a biblioteca `scikit-learn`.
- **`metrics.py`**: Funções para cálculo de métricas (acurácia, precisão, revocação) e geração de matrizes de confusão.
- **`main.py`**: Arquivo principal que executa os classificadores KNN e MLP nos datasets Iris e Wine.

## Funcionalidades

1. **Classificação com KNN (`knn.py`)**:
   - Implementação manual do algoritmo KNN.
   - Calcula a distância euclidiana entre os pontos.
   - Realiza a votação majoritária para determinar a classe dos vizinhos mais próximos.
   - Avalia o desempenho com métricas como acurácia, precisão e revocação.
   - Gera a matriz de confusão para análise.

2. **Classificação com MLP (`mlp.py`)**:
   - Utiliza o `MLPClassifier` da biblioteca `scikit-learn`.
   - Suporte para ajuste de hiperparâmetros como número de camadas ocultas (`hidden_layer_sizes`) e número máximo de iterações (`max_iter`).
   - Avalia o desempenho com métricas como acurácia, precisão e revocação.
   - Gera a matriz de confusão para análise.

3. **Avaliação e Visualização (`metrics.py`)**:
   - **`calculate_metrics`**: Calcula acurácia, precisão e revocação.
   - **`plot_confusion_matrix`**: Gera uma matriz de confusão para comparar as previsões com os rótulos reais.

4. **Execução Principal (`main.py`)**:
   - Carrega os datasets Iris e Wine.
   - Normaliza os dados para o MLP utilizando `StandardScaler`.
   - Executa os classificadores KNN e MLP para ambos os datasets.
   - Exibe as métricas e gera as matrizes de confusão.

## Requisitos

Certifique-se de que as seguintes bibliotecas estão instaladas:

- `numpy`
- `pandas`
- `scikit-learn`
- `matplotlib`
- `seaborn`

Para instalar as dependências, execute:

```bash
pip install numpy pandas scikit-learn matplotlib seaborn
```

## Como Executar

1. Clone o repositório:
    ```bash 
    git clone https://github.com/seu-usuario/Projeto-3-Perceptron.git
    cd Projeto-3-Perceptron
    ```

2. Execute o arquivo principal:
    ```bash
    python main.py
    ```

## Resultados

Os resultados incluem:
- **Métricas de Avaliação**:
Acurácia, precisão e revocação para os classificadores KNN e MLP.
- **Matriz de Confusão**:
Compara as previsões com os rótulos reais para análise detalhada.

### Exemplo de Saída no Console
```plaintext
=== Executando KNN no Dataset Iris ===
Iris - KNN (k=3)
Acurácia: 0.97
Precisão: 0.97
Revocação: 0.97

=== Executando MLP no Dataset Iris ===
Iris - MLP (hidden_layer_sizes=(100,), max_iter=500)
Acurácia: 1.00
Precisão: 1.00
Revocação: 1.00
```

### Gráficos Gerados
1. **Matriz de Confusão**:
    - Mostra como as previsões se relacionam com os rótulos reais.
2. **Visualização de Métricas**:
    - Exibe as métricas de desempenho diretamente no console.

## Conjuntos de Dados

1. Iris:
- Contém 150 amostras divididas igualmente entre 3 classes:
    - `Iris-setosa`
    - `Iris-versicolor`
    - `Iris-virginica`
- Cada amostra possui 4 características:
    - Comprimento da sépala (`SepalLengthCm`)
    - Largura da sépala (`SepalWidthCm`)
    - Comprimento da pétala (`PetalLengthCm`)
    - Largura da pétala (`PetalWidthCm`)

2. Wine:
- Contém 178 amostras divididas entre 3 classes de vinho.
- Cada amostra possui 13 características químicas.

## Observações

- O dataset Iris é simples e pode levar a métricas perfeitas no MLP, mas pode gerar avisos de convergência devido ao limite de iterações.
- O dataset Wine é mais complexo e pode exigir ajustes nos hiperparâmetros do MLP para melhor desempenho.

## Melhorias Recentes
- Adicionado suporte para normalização dos dados no MLP.
- Ajuste de hiperparâmetros para evitar problemas de convergência no MLP.
- Implementação manual do KNN para aprendizado didático.

## 🔗 Link para o vídeo de explicação



---

Projeto desenvolvido por João Pedro Alves Carneiro Valadão e Michel Alexandrino de Souza para a disciplina Inteligência Artificial, realizada na Universidade Federal de Lavras.