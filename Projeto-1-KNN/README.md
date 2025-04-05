# Projeto 1 - KNN (K-Nearest Neighbors)

Este projeto implementa o algoritmo K-Nearest Neighbors (KNN) para classificação de espécies de flores do conjunto de dados Iris. O código realiza a classificação com base nas características das flores e gera arquivos de saída contendo os resultados e uma matriz de confusão. Além disso, compara a implementação manual do KNN com a implementação da biblioteca `scikit-learn`.

## Estrutura do Projeto

- **`knn_hc.py`**: Implementação manual (hardcore) do algoritmo KNN.
- **`knn_sklearn.py`**: Implementação do KNN utilizando a biblioteca `scikit-learn`.
- **`compare_classifiers.py`**: Código que compara o desempenho e as métricas das duas implementações (manual e `scikit-learn`).
- **`iris.csv`**: Conjunto de dados Iris utilizado para treinar e testar os modelos.
- **`predictions.txt`**: Arquivo gerado pela implementação manual contendo as espécies reais e as previstas.
- **`confusion_matrix.png`**: Imagem gerada pela implementação manual com a matriz de confusão.
- **`confusion_matrix_sklearn.png`**: Imagem gerada pela implementação com `scikit-learn` com a matriz de confusão.

## Funcionalidades

1. **Classificação com KNN Manual (`knn_hc.py`)**:
   - Implementa o cálculo da distância euclidiana.
   - Realiza a classificação com base nos vizinhos mais próximos.
   - Gera métricas de avaliação (acurácia, precisão e revocação).
   - Salva os resultados em `predictions.txt` e gera a matriz de confusão em `confusion_matrix.png`.

2. **Classificação com KNN usando `scikit-learn` (`knn_sklearn.py`)**:
   - Utiliza a biblioteca `scikit-learn` para treinar e testar o modelo.
   - Gera métricas de avaliação (acurácia, precisão e revocação).
   - Gera a matriz de confusão em `confusion_matrix_sklearn.png`.

3. **Comparação de Classificadores (`compare_classifiers.py`)**:
   - Compara o tempo de execução e as métricas de avaliação das duas implementações.
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
- Métricas de avaliação (acurácia, precisão e revocação) para ambas as implementações.
- Arquivos de saída contendo previsões e matrizes de confusão.

## Observações

- O conjunto de dados Iris é dividido em 80% para treino e 20% para teste.
- O valor de `k` utilizado nos classificadores pode ser ajustado nos respectivos arquivos de código.