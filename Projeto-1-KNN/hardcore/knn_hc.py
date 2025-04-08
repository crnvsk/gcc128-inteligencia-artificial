import time
import numpy as np
import pandas as pd
import math
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Caminho absoluto para o arquivo iris.csv
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
iris_csv_path = os.path.join(BASE_DIR, "../iris.csv")

# ------ Funções ------ #

# Calcula a distância Euclidiana entre duas amostras
def euclidean_distance(linha1, linha2):
    sl = (linha1['SepalLengthCm'] - linha2['SepalLengthCm']) ** 2
    sw = (linha1['SepalWidthCm'] - linha2['SepalWidthCm']) ** 2
    pl = (linha1['PetalLengthCm'] - linha2['PetalLengthCm']) ** 2
    pw = (linha1['PetalWidthCm'] - linha2['PetalWidthCm']) ** 2
    return math.sqrt(sl + sw + pl + pw)

# Retorna os índices dos k vizinhos mais próximos
def k_nearest_neighbors(train_df, test_row, k):
    distances = []
    for idx, train_row in train_df.iterrows():
        dist = euclidean_distance(train_row, test_row)
        distances.append((idx, dist))
    distances.sort(key=lambda x: x[1])
    neighbors = [idx for idx, _ in distances[:k]]
    return neighbors

# Classifica a espécie com base nos vizinhos mais próximos
def classify_species(train_df, nearest_neighbors_list):
    species_list = []
    for neighbors in nearest_neighbors_list:
        species_counts = train_df.loc[neighbors, 'Species'].value_counts()
        most_common_species = species_counts.idxmax()
        species_list.append(most_common_species)
    return species_list

# Avalia o algoritmo para múltiplos valores de k
def evaluate_multiple_k_values(k_values):
    # Carrega o dataset
    df = pd.read_csv(iris_csv_path)

    # Embaralha o dataset com seed fixa
    SEED = 123
    np.random.seed(SEED)
    df_shuffled = df.sample(frac=1, random_state=SEED).reset_index(drop=True)

    # Divide em treino e teste (80/20)
    df_train = df_shuffled[0:120].copy()
    df_test = df_shuffled[120:].copy()

    results = []

    for k in k_values:
        print(f"Calculando para k={k}...")
        # Encontra os vizinhos mais próximos
        nearest_neighbors_list = []
        for _, test_row in df_test.iterrows():
            neighbors = k_nearest_neighbors(df_train, test_row, k)
            nearest_neighbors_list.append(neighbors)

        # Prediz a espécie dos testes
        species_predictions = classify_species(df_train, nearest_neighbors_list)

        # Adiciona as previsões ao dataframe de teste
        df_test['PredictedSpecies'] = species_predictions

        # Salva os resultados em um arquivo .txt
        df_test[['Species', 'PredictedSpecies']].to_csv(f"predictions_k{k}.txt", index=False, sep='\t')

        # Gera uma matriz de confusão e salva como .png
        cm = confusion_matrix(df_test['Species'], df_test['PredictedSpecies'], labels=df['Species'].unique())
        plt.figure(figsize=(8, 6))
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=df['Species'].unique(), yticklabels=df['Species'].unique())
        plt.title(f"Matriz de Confusão (k={k})")
        plt.xlabel("Previsão")
        plt.ylabel("Verdadeiro")
        plt.savefig(f"confusion_matrix_k{k}.png")

        # Calcula métricas de avaliação
        accuracy = accuracy_score(df_test['Species'], df_test['PredictedSpecies'])
        precision = precision_score(df_test['Species'], df_test['PredictedSpecies'], average='weighted')
        recall = recall_score(df_test['Species'], df_test['PredictedSpecies'], average='weighted')

        # Armazena os resultados
        results.append({
            'k': k,
            'accuracy': accuracy,
            'precision': precision,
            'recall': recall
        })

    # Exibe os resultados finais
    print("\nResultados finais (Hardcore):")
    for result in results:
        print(f"k={result['k']} -> Acurácia: {result['accuracy']:.2f}, Precisão: {result['precision']:.2f}, Revocação: {result['recall']:.2f}")

    return results

# ------ Código Principal ------ #

if __name__ == "__main__":
    # Testa múltiplos valores de k
    k_values = [1, 3, 5, 7]

    # Inicia a medição do tempo
    start_time = time.time()

    # Executa o algoritmo
    evaluate_multiple_k_values(k_values)

    # Calcula o tempo total de execução
    end_time = time.time()
    elapsed_time = end_time - start_time

    # Exibe o tempo de execução
    print(f"\nTempo total de execução: {elapsed_time:.2f} segundos")