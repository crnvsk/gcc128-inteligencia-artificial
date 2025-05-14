import numpy as np
from metrics import calculate_metrics, plot_confusion_matrix
from collections import Counter
from sklearn.model_selection import train_test_split

def euclidean_distance(point1, point2):
    return np.sqrt(np.sum((point1 - point2) ** 2))

def predict_knn(X_train, y_train, X_test, k):
    predictions = []
    for test_point in X_test:
        distances = [euclidean_distance(test_point, train_point) for train_point in X_train]
        k_indices = np.argsort(distances)[:k]
        k_labels = [y_train[i] for i in k_indices]
        most_common = Counter(k_labels).most_common(1)[0][0]
        predictions.append(most_common)
    return np.array(predictions)

def run_knn(X, y, k=3, dataset_name="Dataset"):
    from sklearn.model_selection import train_test_split
    # Use stratify=y para manter a proporção das classes
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    y_pred = predict_knn(X_train.values, y_train.values, X_test.values, k)
    # Retorne também os índices do conjunto de teste
    return y_test.index, y_test.values, y_pred, dataset_name