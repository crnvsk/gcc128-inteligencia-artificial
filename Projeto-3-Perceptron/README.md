# Projeto 3 - Perceptron (MLPClassifier)

Este projeto implementa dois algoritmos de classificação: **K-Nearest Neighbors (KNN)** e **Multi-Layer Perceptron (MLP)**. O objetivo é comparar as implementações manuais e baseadas em bibliotecas, avaliando o desempenho em dois datasets clássicos: **Iris** e **Wine**.

## Estrutura do Projeto

- **`knn.py`**: Implementação manual do algoritmo KNN.
- **`mlp.py`**: Implementação do classificador MLP utilizando a biblioteca `scikit-learn`.
- **`metrics.py`**: Funções para cálculo de métricas (acurácia, precisão, revocação) e geração de matrizes de confusão.
- **`main.py`**: Arquivo principal que executa os classificadores KNN e MLP nos datasets Iris e Wine.
- **Arquivos de saída `.txt`**: Após a execução, os resultados completos (métricas, matrizes de confusão e classificações) são salvos nos arquivos:
  - `classificacao_iris.txt`
  - `classificacao_wine.txt`

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

Todos os resultados (métricas de avaliação, matrizes de confusão e classificações) são salvos nos arquivos `.txt` gerados após a execução do projeto.

### Exemplo de Saída
```plaintext
Os arquivos `classificacao_iris.txt` e `classificacao_wine.txt` apresentam, para cada classificador (KNN e MLP):

- Tabela de classificação (rótulo real x rótulo previsto)
- Métricas: acurácia, precisão e revocação
- Matriz de confusão

Exemplo de trecho do arquivo `classificacao_iris.txt`:
```plaintext
###--- KNN ---###

 Id     Species           Predicted_Species
  0  setosa           setosa
  1  virginica        virginica
  ...

--------------------------------------------------

Accuracy: 1.0000
Precision: 1.0000
Recall: 1.0000

--------------------------------------------------

                    setosa            versicolor        virginica         
setosa              10                0                 0                 
versicolor          0                 10                0                 
virginica           0                 0                 10
```

### Visualização dos Resultados

- Não são gerados gráficos automaticamente.
- Toda a análise (métricas e matrizes de confusão) está disponível nos arquivos `.txt` para consulta detalhada.

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

[https://youtu.be/R8wd_EnAtjY](https://youtu.be/R8wd_EnAtjY)

---

Projeto desenvolvido por João Pedro Alves Carneiro Valadão e Michel Alexandrino de Souza para a disciplina Inteligência Artificial, realizada na Universidade Federal de Lavras.
