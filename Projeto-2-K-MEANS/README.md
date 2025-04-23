# Projeto 2 - K-Means Clustering

Este projeto implementa o algoritmo de agrupamento **K-Means** para análise e visualização de dados. O código compara uma implementação manual do K-Means (`KMeansHardcore`) com a implementação otimizada da biblioteca `scikit-learn`. O objetivo é explorar a funcionalidade do K-Means, avaliar a qualidade dos clusters gerados e visualizar os resultados.

## Estrutura do Projeto

- **`kmeans_hardcore.py`**: Implementação manual (hardcore) do algoritmo K-Means.
- **`kmeans_sklearn.py`**: Implementação do K-Means utilizando a biblioteca `scikit-learn`.
- **`metrics.py`**: Funções para avaliação de métricas e visualização.
- **`pca_plot.py`**: Função para visualização dos clusters com PCA.
- **`iris.csv`**: Conjunto de dados Iris (opcional, caso queira carregar de um arquivo CSV).
- **`main.py`**: Arquivo principal que executa o projeto.

## Funcionalidades

1. **Agrupamento com K-Means Manual (`kmeans_hardcore.py`)**:
   - Implementa o cálculo da distância euclidiana.
   - Realiza a atualização iterativa dos centróides até a convergência.
   - Suporte para diferentes valores de `k` (número de clusters).
   - Mede o tempo de execução e avalia a qualidade dos clusters com o **Silhouette Score**.

2. **Agrupamento com K-Means usando `scikit-learn` (`kmeans_sklearn.py`)**:
   - Utiliza a biblioteca `scikit-learn` para treinar e testar o modelo.
   - Suporte para diferentes valores de `k` (número de clusters).
   - Mede o tempo de execução e avalia a qualidade dos clusters com o **Silhouette Score**.

3. **Avaliação e Visualização (`metrics.py` e `pca_plot.py`)**:
   - **`evaluate_model`**: Mede o tempo de execução e calcula o Silhouette Score.
   - **`plot_confusion`**: Gera uma matriz de confusão para comparar os clusters com as classes reais.
   - **`plot_pca_clusters`**: Reduz a dimensionalidade dos dados com PCA e visualiza os clusters em 2D ou 1D.

4. **Execução Principal (`main.py`)**:
   - Carrega o dataset Iris, normaliza os dados e executa os dois algoritmos de K-Means.
   - Avalia os clusters gerados e gera visualizações.

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
   git clone https://github.com/seu-usuario/Projeto-2-K-MEANS.git
   cd Projeto-2-K-MEANS
   ```

2. Execute o arquivo principal:
   ```bash
   python main.py
   ```

## Resultados

Os resultados incluem:
- **Silhouette Score**: Avalia a qualidade dos clusters gerados.
- **Matriz de Confusão**: Compara os clusters gerados com as classes reais do dataset Iris.
- **Gráficos PCA**: Visualiza os clusters em 2D e 1D.

### Exemplo de Saída no Console
```plaintext
========== K = 3 ==========

[Hardcore]
Silhouette Score: 0.5528 | Tempo: 0.0123s

[Sklearn]
Silhouette Score: 0.5532 | Tempo: 0.0012s
```

### Gráficos Gerados
1. **Matriz de Confusão**:
   - Mostra como os clusters se relacionam com as classes reais.
2. **Gráficos PCA**:
   - Visualiza os clusters em 2D e 1D.

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

## Observações

- O dataset Iris é carregado diretamente da biblioteca `scikit-learn` ou do arquivo `iris.csv`.
- O número de clusters (`k`) pode ser ajustado no arquivo `main.py`.

## Melhorias Recentes

- Adicionado suporte para medir o tempo de execução de ambos os algoritmos.
- Geração de gráficos PCA para visualização dos clusters.
- Comparação detalhada entre as implementações manual e `scikit-learn`.

## 🔗 Link para o vídeo de explicação

[https://youtu.be/B_ucFXOh9l4](https://youtu.be/B_ucFXOh9l4)

---

Projeto desenvolvido por João Pedro Alves Carneiro Valadão e Michel Alexandrino de Souza para a disciplina Inteligência Artificial, realizada na Universidade Federal de Lavras.
