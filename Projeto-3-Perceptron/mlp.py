import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

def run_mlp(X, y, hidden_layer_sizes=(100,), max_iter=300, dataset_name="Dataset"):
    """
    Divide os dados, treina o MLP e retorna índices, verdadeiros, preditos e nome do dataset.
    """
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    mlp = MLPClassifier(hidden_layer_sizes=hidden_layer_sizes, max_iter=max_iter, random_state=42)
    mlp.fit(X_train, y_train)
    y_pred = mlp.predict(X_test)
    return y_test.index if hasattr(y_test, 'index') else np.arange(len(y_test)), y_test, y_pred, dataset_name