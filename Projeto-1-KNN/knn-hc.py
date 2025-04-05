import numpy as np
import pandas as pd
import math
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score
import matplotlib.pyplot as plt
import seaborn as sns
import time
import os

# ------ Funções ------ #

# Calcula a distância Euclidiana entre duas amostras
def distanciaEuclidiana(linha1, linha2):
    sl = (linha1['SepalLengthCm'] - linha2['SepalLengthCm']) ** 2
    sw = (linha1['SepalWidthCm'] - linha2['SepalWidthCm']) ** 2
    pl = (linha1['PetalLengthCm'] - linha2['PetalLengthCm']) ** 2
    pw = (linha1['PetalWidthCm'] - linha2['PetalWidthCm']) ** 2
    return math.sqrt(sl + sw + pl + pw)

# Retorna os índices dos k vizinhos mais próximos
def k_nearest_neighbors(train_df, test_row, k):
    distances = []
    for idx, train_row in train_df.iterrows():
        dist = distanciaEuclidiana(train_row, test_row)
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

# ------ Código Principal ------ #

def main_algorithm(k_input):
    # Carrega o dataset
    df = pd.read_csv("iris.csv")

    # Embaralha o dataset com seed fixa
    SEED = 123
    np.random.seed(SEED)
    df_shuffled = df.sample(frac=1, random_state=SEED).reset_index(drop=True)

    # Divide em treino e teste (80/20)
    df_train = df_shuffled[0:120].copy()
    df_test = df_shuffled[120:].copy()

    # Encontra os vizinhos mais próximos
    k = k_input
    nearest_neighbors_list = []
    for _, test_row in df_test.iterrows():
        neighbors = k_nearest_neighbors(df_train, test_row, k)
        nearest_neighbors_list.append(neighbors)

    # Prediz a espécie dos testes
    species_predictions = classify_species(df_train, nearest_neighbors_list)

    # Adiciona as previsões ao dataframe de teste
    df_test['PredictedSpecies'] = species_predictions

    # Salva os resultados em um arquivo .txt
    df_test[['Species', 'PredictedSpecies']].to_csv("predictions.txt", index=False, sep='\t')
    print("Arquivo predictions.txt gerado com sucesso!")

    # Gera uma matriz de confusão e salva como .png
    cm = confusion_matrix(df_test['Species'], df_test['PredictedSpecies'], labels=df['Species'].unique())
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=df['Species'].unique(), yticklabels=df['Species'].unique())
    plt.title("Matriz de Confusão")
    plt.xlabel("Previsão")
    plt.ylabel("Verdadeiro")
    plt.savefig("confusion_matrix.png")
    print("Arquivo confusion_matrix.png gerado com sucesso!")

    # Exibe métricas de avaliação
    accuracy = accuracy_score(df_test['Species'], df_test['PredictedSpecies'])
    precision = precision_score(df_test['Species'], df_test['PredictedSpecies'], average='weighted')
    recall = recall_score(df_test['Species'], df_test['PredictedSpecies'], average='weighted')
    print(f"Acurácia: {accuracy:.2f}")
    print(f"Precisão: {precision:.2f}")
    print(f"Revocação: {recall:.2f}")

# Executa o algoritmo principal com k=3 (ou outro valor desejado)
if __name__ == "__main__":
    main_algorithm(k_input=3)