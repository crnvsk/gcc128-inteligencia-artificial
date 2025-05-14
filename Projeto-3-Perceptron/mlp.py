import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from metrics import calculate_metrics, plot_confusion_matrix
import numpy as np

def run_mlp(X, y, hidden_layer_sizes=(100,), max_iter=300, dataset_name="Dataset"):
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)
    mlp = MLPClassifier(hidden_layer_sizes=hidden_layer_sizes, max_iter=max_iter, random_state=42)
    mlp.fit(X_train, y_train)
    y_pred = mlp.predict(X_test)
    # Retorne também os índices do conjunto de teste
    return y_test.index, y_test.values, y_pred, dataset_name