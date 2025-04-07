# Projeto 1 - KNN (K-Nearest Neighbors)

Este projeto implementa o algoritmo K-Nearest Neighbors (KNN) para classificação de espécies de flores do conjunto de dados Iris. O código realiza a classificação com base nas características das flores e gera arquivos de saída contendo os resultados e matrizes de confusão. Além disso, compara a implementação manual do KNN com a implementação da biblioteca `scikit-learn`.

## Estrutura do Projeto

- **`knn_hc.py`**: Implementação manual (hardcore) do algoritmo KNN, com suporte para testar múltiplos valores de `k`.
- **`knn_sklearn.py`**: Implementação do KNN utilizando a biblioteca `scikit-learn`, também com suporte para testar múltiplos valores de `k`.
- **`compare_classifiers.py`**: Código que compara o desempenho e as métricas das duas implementações (manual e `scikit-learn`).
- **`iris.csv`**: Conjunto de dados Iris utilizado para treinar e testar os modelos.
- **`predictions_k{k}.txt`**: Arquivos gerados pela implementação manual contendo as espécies reais e as previstas para diferentes valores de `k`.
- **`confusion_matrix_k{k}.png`**: Imagens geradas pela implementação manual com as matrizes de confusão para diferentes valores de `k`.
- **`confusion_matrix_sklearn_k{k}.png`**: Imagens geradas pela implementação com `scikit-learn` com as matrizes de confusão para diferentes valores de `k`.

## Funcionalidades

1. **Classificação com KNN Manual (`knn_hc.py`)**:
   - Implementa o cálculo da distância euclidiana.
   - Realiza a classificação com base nos vizinhos mais próximos.
   - Suporte para testar múltiplos valores de `k` (ex.: `k=1, 3, 5, 7`).
   - Gera métricas de avaliação (acurácia, precisão e revocação) para cada valor de `k`.
   - Salva os resultados em arquivos `predictions_k{k}.txt` e gera matrizes de confusão em `confusion_matrix_k{k}.png`.

2. **Classificação com KNN usando `scikit-learn` (`knn_sklearn.py`)**:
   - Utiliza a biblioteca `scikit-learn` para treinar e testar o modelo.
   - Suporte para testar múltiplos valores de `k` (ex.: `k=1, 3, 5, 7`).
   - Gera métricas de avaliação (acurácia, precisão e revocação) para cada valor de `k`.
   - Gera matrizes de confusão em `confusion_matrix_sklearn_k{k}.png`.

3. **Comparação de Classificadores (`compare_classifiers.py`)**:
   - Compara o tempo de execução e as métricas de avaliação das duas implementações (manual e `scikit-learn`).
   - Exibe os resultados no console.

## Requisitos

Certifique-se de que as seguintes bibliotecas estão instaladas:

- `numpy`
- `pandas`
- `matplotlib`
- `seaborn`
- `scikit-learn`

Para instalar as dependências, execute:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn
```

## Como Executar

1. **Classificação com KNN Manual**:
   ```bash
   python knn_hc.py
   ```

2. **Classificação com KNN usando `scikit-learn`**:
   ```bash
   python knn_sklearn.py
   ```

3. **Comparação de Classificadores**:
   ```bash
   python compare_classifiers.py
   ```

## Resultados

Os resultados incluem:
- Métricas de avaliação (acurácia, precisão e revocação) para diferentes valores de `k` em ambas as implementações.
- Arquivos de saída contendo previsões (`predictions_k{k}.txt`) e matrizes de confusão (`confusion_matrix_k{k}.png` e `confusion_matrix_sklearn_k{k}.png`).

## Observações

- O conjunto de dados Iris é dividido em 80% para treino e 20% para teste.
- O valor de `k` utilizado nos classificadores pode ser ajustado nos respectivos arquivos de código.
- As implementações foram testadas para os valores de `k = [1, 3, 5, 7]`, mas você pode adicionar outros valores conforme necessário.

## Melhorias Recentes

- Adicionado suporte para testar múltiplos valores de `k` em ambas as implementações.
- Geração de arquivos e matrizes de confusão para cada valor de `k`.
- Comparação detalhada entre as implementações manual e `scikit-learn`.

## Conjunto de Dados

O conjunto de dados Iris contém 150 amostras divididas igualmente entre 3 classes:
- `Iris-setosa`
- `Iris-versicolor`
- `Iris-virginica`

Cada amostra possui 4 características:
- Comprimento da sépala (`SepalLengthCm`)
- Largura da sépala (`SepalWidthCm`)
- Comprimento da pétala (`PetalLengthCm`)
- Largura da pétala (`PetalWidthCm`)