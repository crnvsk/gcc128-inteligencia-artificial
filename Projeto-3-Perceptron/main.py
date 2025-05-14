import pandas as pd
from sklearn.datasets import load_iris, load_wine
from sklearn.preprocessing import StandardScaler
from knn import run_knn
from mlp import run_mlp
from metrics import calculate_metrics, confusion_matrix
import numpy as np

def write_classification_file(filepath, results):
    """
    Salva os resultados de classificação em um arquivo de texto.
    """
    try:
        with open(filepath, "w", encoding="utf-8") as f:
            for algorithm_name, ids, y_true, y_pred, target_names in results:
                f.write(f"###--- {algorithm_name} ---###\n\n")
                f.write(" Id".ljust(8) + "Species".ljust(18) + "Predicted_Species\n")
                for idx, real, pred in zip(ids, y_true, y_pred):
                    f.write(f"{str(idx).rjust(3)}  {target_names[real].ljust(16)} {target_names[pred]}\n")
                f.write("\n" + "-"*50 + "\n\n")
                acc, prec, rec = calculate_metrics(y_true, y_pred)
                f.write(f"Accuracy: {acc:.4f}\n")
                f.write(f"Precision: {prec:.4f}\n")
                f.write(f"Recall: {rec:.4f}\n\n")
                f.write("-"*50 + "\n\n")
                # Matriz de confusão
                cm = confusion_matrix(y_true, y_pred)
                f.write("".ljust(20))
                for name in target_names:
                    f.write(name.ljust(18))
                f.write("\n")
                for i, row in enumerate(cm):
                    f.write(target_names[i].ljust(20))
                    for val in row:
                        f.write(str(val).ljust(18))
                    f.write("\n")
                f.write("\n")
    except Exception as e:
        print(f"Erro ao salvar o arquivo {filepath}: {e}")

if __name__ == "__main__":
    # Dataset Iris
    iris = load_iris()
    X_iris = pd.DataFrame(iris.data, columns=iris.feature_names)
    y_iris = pd.Series(iris.target)
    iris_target_names = iris.target_names

    print("\n=== Executando KNN no Dataset Iris ===")
    idx_iris_knn, y_test_iris_knn, y_pred_iris_knn, _ = run_knn(X_iris, y_iris, k=5, dataset_name="Iris")

    print("\n=== Executando MLP no Dataset Iris ===")
    scaler_iris = StandardScaler()
    X_iris_scaled = scaler_iris.fit_transform(X_iris)
    idx_iris_mlp, y_test_iris_mlp, y_pred_iris_mlp, _ = run_mlp(X_iris_scaled, y_iris, hidden_layer_sizes=(100,), max_iter=500, dataset_name="Iris")

    # Dataset Wine
    wine = load_wine()
    X_wine = pd.DataFrame(wine.data, columns=wine.feature_names)
    y_wine = pd.Series(wine.target)
    wine_target_names = wine.target_names

    print("\n=== Executando KNN no Dataset Wine ===")
    idx_wine_knn, y_test_wine_knn, y_pred_wine_knn, _ = run_knn(X_wine, y_wine, k=5, dataset_name="Wine")

    print("\n=== Executando MLP no Dataset Wine ===")
    scaler_wine = StandardScaler()
    X_wine_scaled = scaler_wine.fit_transform(X_wine)
    idx_wine_mlp, y_test_wine_mlp, y_pred_wine_mlp, _ = run_mlp(X_wine_scaled, y_wine, hidden_layer_sizes=(100,), max_iter=500, dataset_name="Wine")

    # Salva classificações Iris em um único arquivo
    iris_results = [
        ("KNN", idx_iris_knn, y_test_iris_knn, y_pred_iris_knn, iris_target_names),
        ("MLP", idx_iris_mlp, y_test_iris_mlp, y_pred_iris_mlp, iris_target_names)
    ]
    write_classification_file("Projeto-3-Perceptron/classificacao_iris.txt", iris_results)

    # Salva classificações Wine em um único arquivo
    wine_results = [
        ("KNN", idx_wine_knn, y_test_wine_knn, y_pred_wine_knn, wine_target_names),
        ("MLP", idx_wine_mlp, y_test_wine_mlp, y_pred_wine_mlp, wine_target_names)
    ]
    write_classification_file("Projeto-3-Perceptron/classificacao_wine.txt", wine_results)