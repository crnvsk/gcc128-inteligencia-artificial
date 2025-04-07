import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score
import matplotlib.pyplot as plt
import seaborn as sns
import time

def sklearn_knn_classifier(k):
    # Carrega o dataset
    df = pd.read_csv("iris.csv")

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

    # Gera a matriz de confusão
    cm = confusion_matrix(y_test, y_pred, labels=df['Species'].unique())
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=df['Species'].unique(), yticklabels=df['Species'].unique())
    plt.title(f"Matriz de Confusão (Sklearn, k={k})")
    plt.xlabel("Previsão")
    plt.ylabel("Verdadeiro")
    plt.savefig(f"confusion_matrix_sklearn_k{k}.png")
    print(f"Arquivo confusion_matrix_sklearn_k{k}.png gerado com sucesso!")

    # Calcula métricas de avaliação
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted')
    recall = recall_score(y_test, y_pred, average='weighted')
    print(f"Acurácia (Sklearn, k={k}): {accuracy:.2f}")
    print(f"Precisão (Sklearn, k={k}): {precision:.2f}")
    print(f"Revocação (Sklearn, k={k}): {recall:.2f}")

    return accuracy, precision, recall, sklearn_time

def evaluate_multiple_k_values_sklearn(k_values):
    results = []
    for k in k_values:
        print(f"\nExecutando o classificador Sklearn para k={k}...")
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

if __name__ == "__main__":
    # Testa múltiplos valores de k
    k_values = [1, 3, 5, 7]
    evaluate_multiple_k_values_sklearn(k_values)