# Repositório de Projetos - GCC128: Inteligência Artificial

Este repositório foi criado para armazenar os projetos desenvolvidos na disciplina **GCC128 - Inteligência Artificial**, oferecida pela **Universidade Federal de Lavras (UFLA)**. A disciplina aborda conceitos fundamentais de Inteligência Artificial, com foco em algoritmos de aprendizado de máquina, agrupamento, classificação, busca em espaços de estados, otimização com algoritmos evolutivos, sistemas multiagentes, além de outras técnicas relacionadas.

---

## **Estrutura do Repositório**

O repositório contém os seguintes projetos:

### **1. Projeto 1 - KNN (K-Nearest Neighbors)**
- Implementação do algoritmo de classificação K-Nearest Neighbors (KNN).
- Comparação entre uma implementação manual e a implementação da biblioteca `scikit-learn`.
- Avaliação de desempenho e geração de matrizes de confusão.
- [Leia mais sobre o Projeto 1](./Projeto-1-KNN/README.md)

### **2. Projeto 2 - K-Means Clustering**
- Implementação do algoritmo de agrupamento K-Means.
- Comparação entre uma implementação manual e a implementação da biblioteca `scikit-learn`.
- Avaliação da qualidade dos clusters com o **Silhouette Score** e visualização com PCA.
- [Leia mais sobre o Projeto 2](./Projeto-2-K-MEANS/README.md)

### **3. Projeto 3 - Perceptron (MLPClassifier)**
- Implementação dos algoritmos de classificação K-Nearest Neighbors (KNN) e Multi-Layer Perceptron (MLP).
- Comparação entre uma implementação manual do KNN e a implementação do MLP utilizando a biblioteca `scikit-learn`.
- Avaliação de desempenho dos classificadores em diferentes conjuntos de dados (Iris e Wine), com métricas como acurácia, precisão, revocação e matriz de confusão.
- [Leia mais sobre o Projeto 3](./Projeto-3-Perceptron/README.md)

### **4. Projeto 4 - Jogo dos Oito (8-Puzzle)**
- Implementação do clássico Jogo dos Oito (8-Puzzle) com interface gráfica interativa.
- Permite ao usuário jogar manualmente ou solicitar a solução automática utilizando os algoritmos de Busca em Largura (BFS) e Busca A*.
- Animação dos movimentos da solução encontrada, destacando o funcionamento dos algoritmos de busca.
- Não requer bibliotecas externas além da biblioteca padrão do Python.
- [Leia mais sobre o Projeto 4](./Projeto-4-Jogo-dos-Oito/README.md)

### **5. Projeto 5 - Algoritmos Genéticos**
- Implementação de um Algoritmo Genético (AG) para otimização da função f(x) = x² − 3x + 4 no intervalo X = [−10, +10].
- Codificação binária dos indivíduos, seleção por torneio, crossover de um ponto e mutação.
- Parâmetros ajustáveis: tamanho da população, número de gerações, taxa de crossover e taxa de mutação.
- Exibe o melhor indivíduo de cada geração e o melhor resultado final.
- Não requer bibliotecas externas além da biblioteca padrão do Python.
- [Leia mais sobre o Projeto 5](./Projeto-5-Algoritmos-Geneticos/README.md)

### **6. Projeto 6 - Agentes Inteligentes: Simulação de Mercado de Jogos Digitais**
- Implementação de uma simulação de mercado virtual utilizando agentes inteligentes com a biblioteca AutoGen.
- Dois tipos de agentes: jogadores (que tomam decisões de compra, venda ou espera) e o mercado (que ajusta o preço conforme oferta e demanda).
- Simulação de rodadas, com exibição detalhada das ações dos agentes, saldo, itens e preço do mercado.
- Parâmetros ajustáveis para experimentação de diferentes cenários.
- [Leia mais sobre o Projeto 6](./Projeto-6-Agentes-Inteligentes/README.md)

---

## **Objetivo**

O objetivo deste repositório é consolidar o aprendizado prático da disciplina, permitindo a aplicação de conceitos teóricos em problemas reais. Cada projeto explora diferentes aspectos da inteligência artificial, como:
- **Classificação**: Identificação de padrões e categorização de dados.
- **Agrupamento**: Descoberta de grupos em dados não rotulados.
- **Avaliação de Modelos**: Uso de métricas como matriz de confusão e Silhouette Score.
- **Visualização**: Representação gráfica dos resultados para melhor interpretação.
- **Busca e Resolução de Problemas**: Aplicação de algoritmos clássicos de busca para resolver o Jogo dos Oito, ilustrando conceitos de busca em espaços de estados e solução automática de problemas.
- **Otimização com Algoritmos Evolutivos**: Utilização de Algoritmos Genéticos para resolver problemas de otimização, demonstrando conceitos de seleção, crossover, mutação e análise de desempenho ao longo das gerações.
- **Sistemas Multiagentes e Simulação de Mercado**: Modelagem de agentes autônomos (jogadores e mercado) interagindo em um ambiente virtual, com tomada de decisão, adaptação e ajuste dinâmico de preços, utilizando a biblioteca AutoGen.

---

## **Como Utilizar**

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/gcc128-inteligencia-artificial.git
   cd gcc128-inteligencia-artificial
   ```

2. Navegue até o projeto desejado:
   ```bash
   cd Projeto-1-KNN
   # ou
   cd Projeto-2-K-MEANS
   # ou
   cd Projeto-3-Perceptron
   # ou
   cd Projeto-4-Jogo-dos-Oito
   # ou
   cd Projeto-5-Algoritmos-Geneticos
   # ou
   cd Projeto-6-Agentes-Inteligentes
   ```

3. Siga as instruções no arquivo `README.md` de cada projeto para executar o código.

---

## **Requisitos**

Certifique-se de ter o Python 3.8 ou superior instalado, além das seguintes bibliotecas:
- `numpy`
- `pandas`
- `scikit-learn`
- `matplotlib`
- `seaborn`
- `pyautogen`

Para instalar as dependências, execute:
```bash
pip install -r requirements.txt
```

---

## **Contribuidores**

Este repositório foi desenvolvido por:
- **João Pedro Alves Carneiro Valadão**
- **Michel Alexandrino de Souza**

---

## **Licença**

Este repositório está licenciado sob a licença MIT. Consulte o arquivo `LICENSE` para mais detalhes.