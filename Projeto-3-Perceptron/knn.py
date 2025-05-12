import numpy as np
from metrics import calculate_metrics, plot_confusion_matrix
from collections import Counter
from sklearn.model_selection import train_test_split

def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))

def predict_knn(X_train, y_train, X_test, k):
    predictions = []
    for test_point in X_test:
        # Calcula a distância entre o ponto de teste e todos os pontos de treino
        distances = [euclidean_distance(test_point, train_point) for train_point in X_train]

        # Obtém os índices dos k vizinhos mais próximos
        k_indices = np.argsort(distances)[:k]

        # Obtém os rótulos dos k vizinhos mais próximos
        k_labels = [y_train[i] for i in k_indices]

        # Determina o rótulo mais comum (votação majoritária)
        most_common = Counter(k_labels).most_common(1)[0][0]

        predictions.append(most_common)
    return np.array(predictions)

def run_knn(X, y, k=3, dataset_name="Dataset"):
    # Dividir os dados em treino e teste (80/20)
    X_train, X_test, y_train, y_test = train_test_split(X.values, y.values, test_size=0.2, random_state=42)

    # Fazer previsões usando o KNN 
    y_pred = predict_knn(X_train, y_train, X_test, k)

    # Calcular métricas
    accuracy, precision, recall = calculate_metrics(y_test, y_pred)

    # Exibir métricas
    print(f"\n{dataset_name} - KNN (k={k})")
    print(f"Acurácia: {accuracy:.2f}")
    print(f"Precisão: {precision:.2f}")
    print(f"Revocação: {recall:.2f}")

    # Plotar matriz de confusão
    plot_confusion_matrix(y_test, y_pred, labels=np.unique(y), title=f"Matriz de Confusão - {dataset_name} (KNN)")