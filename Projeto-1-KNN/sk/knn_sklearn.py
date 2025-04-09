import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score
import matplotlib.pyplot as plt
import seaborn as sns
import time
import os

# Caminho absoluto para o arquivo iris.csv
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
iris_csv_path = os.path.join(BASE_DIR, "../iris.csv")

# ------ Funções ------ #

def sklearn_knn_classifier(k):
    # Carrega o dataset
    df = pd.read_csv(iris_csv_path)

    # Divide em treino e teste (80/20)
    X = df[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
    y = df['Species']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)

    # Treina o classificador KNN
    start_time = time.time()
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    sklearn_time = time.time() - start_time

    # Salva as previsões em um arquivo .txt
    predictions_df = pd.DataFrame({'TrueSpecies': y_test, 'PredictedSpecies': y_pred})
    predictions_df.to_csv(f"predictions_sklearn_k{k}.txt", index=False, sep='\t')

    # Gera a matriz de confusão
    cm = confusion_matrix(y_test, y_pred, labels=df['Species'].unique())
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=df['Species'].unique(), yticklabels=df['Species'].unique())
    plt.title(f"Matriz de Confusão (Sklearn, k={k})")
    plt.xlabel("Previsão")
    plt.ylabel("Verdadeiro")
    plt.savefig(f"confusion_matrix_sklearn_k{k}.png")

    # Calcula métricas de avaliação
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted')
    recall = recall_score(y_test, y_pred, average='weighted')

    return accuracy, precision, recall, sklearn_time

def evaluate_multiple_k_values_sklearn(k_values):
    results = []
    for k in k_values:
        print(f"Calculando para k={k}...")
        accuracy, precision, recall, sklearn_time = sklearn_knn_classifier(k)
        results.append({
            'k': k,
            'accuracy': accuracy,
            'precision': precision,
            'recall': recall,
            'time': sklearn_time
        })

    # Exibe os resultados finais
    print("\nResultados finais (Sklearn):")
    for result in results:
        print(f"k={result['k']} -> Acurácia: {result['accuracy']:.2f}, Precisão: {result['precision']:.2f}, Revocação: {result['recall']:.2f}, Tempo: {result['time']:.4f}s")

    return results

# ------ Código Principal ------ #

if __name__ == "__main__":
    # Testa múltiplos valores de k
    k_values = [1, 3, 5, 7]

    # Inicia a medição do tempo total
    start_time = time.time()

    # Executa o algoritmo
    evaluate_multiple_k_values_sklearn(k_values)

    # Calcula o tempo total de execução
    end_time = time.time()
    elapsed_time = end_time - start_time

    # Exibe o tempo total de execução
    print(f"\nTempo total de execução: {elapsed_time:.2f} segundos")