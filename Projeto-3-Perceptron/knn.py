import numpy as np
from collections import Counter

def euclidean_distance(point1, point2):
    """
    Calcula a distância Euclidiana entre dois pontos.
    """
    return np.sqrt(np.sum((point1 - point2) ** 2))

def predict_knn(X_train, y_train, X_test, k):
    """
    Realiza a predição usando o algoritmo KNN.
    """
    predictions = []
    for test_point in X_test:
        distances = np.linalg.norm(X_train - test_point, axis=1)
        k_indices = np.argsort(distances)[:k]
        k_labels = y_train[k_indices]
        most_common = Counter(k_labels).most_common(1)[0][0]
        predictions.append(most_common)
    return np.array(predictions)

def run_knn(X, y, k=3, dataset_name="Dataset"):
    """
    Divide os dados, executa o KNN e retorna índices, verdadeiros, preditos e nome do dataset.
    """
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X.values, y.values, test_size=0.2, random_state=42, stratify=y)
    y_pred = predict_knn(X_train, y_train, X_test, k)
    # Retorne também os índices do conjunto de teste
    return y_test.index if hasattr(y_test, 'index') else np.arange(len(y_test)), y_test, y_pred, dataset_name