import pandas as pd
from sklearn.datasets import load_iris, load_wine
from sklearn.preprocessing import StandardScaler
from knn import run_knn
from mlp import run_mlp

if __name__ == "__main__":
    # Dataset Iris
    iris = load_iris()
    X_iris = pd.DataFrame(iris.data, columns=iris.feature_names)
    y_iris = pd.Series(iris.target)

    print("\n=== Executando KNN no Dataset Iris ===")
    run_knn(X_iris, y_iris, k=3, dataset_name="Iris")

    print("\n=== Executando MLP no Dataset Iris ===")
    scaler = StandardScaler()
    X_iris_scaled = scaler.fit_transform(X_iris)
    run_mlp(X_iris_scaled, y_iris, hidden_layer_sizes=(100,), max_iter=500, dataset_name="Iris")

    # Dataset Wine
    wine = load_wine()
    X_wine = pd.DataFrame(wine.data, columns=wine.feature_names)
    y_wine = pd.Series(wine.target)

    print("\n=== Executando KNN no Dataset Wine ===")
    run_knn(X_wine, y_wine, k=3, dataset_name="Wine")

    print("\n=== Executando MLP no Dataset Wine ===")
    scaler = StandardScaler()
    X_wine_scaled = scaler.fit_transform(X_wine)
    run_mlp(X_wine_scaled, y_wine, hidden_layer_sizes=(100,), max_iter=300, dataset_name="Wine")