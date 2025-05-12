import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from metrics import calculate_metrics, plot_confusion_matrix
import numpy as np

def run_mlp(X, y, hidden_layer_sizes=(100,), max_iter=300, dataset_name="Dataset"):
    # Dividir os dados em treino e teste (80/20)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Treinar o classificador MLP
    mlp = MLPClassifier(hidden_layer_sizes=hidden_layer_sizes, max_iter=max_iter, random_state=42)
    mlp.fit(X_train, y_train)
    y_pred = mlp.predict(X_test)

    # Calcular métricas
    accuracy, precision, recall = calculate_metrics(y_test, y_pred)

    # Exibir métricas
    print(f"\n{dataset_name} - MLP (hidden_layer_sizes={hidden_layer_sizes}, max_iter={max_iter})")
    print(f"Acurácia: {accuracy:.2f}")
    print(f"Precisão: {precision:.2f}")
    print(f"Revocação: {recall:.2f}")

    # Plotar matriz de confusão
    plot_confusion_matrix(y_test, y_pred, labels=np.unique(y), title=f"Matriz de Confusão - {dataset_name} (MLP)")