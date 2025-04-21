import time
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler

from kmeans_hardcore import KMeansHardcore
from kmeans_sklearn import run_kmeans_sklearn
from metrics import evaluate_model, evaluate_labels, plot_confusion
from pca_plot import plot_pca_clusters

# Carregar e normalizar dados
iris = load_iris()
X = pd.DataFrame(iris.data, columns=iris.feature_names)
y = pd.Series(iris.target)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Avaliar modelos
for k in [3, 5]:
    print(f"\n========== K = {k} ==========")

    # Hardcore
    print("\n[Hardcore]")
    model_hard = KMeansHardcore(n_clusters=k)
    labels_hard, score_hard, time_hard = evaluate_model(model_hard, X_scaled)
    print(f"Silhouette Score: {score_hard:.4f} | Tempo: {time_hard:.4f}s")
    plot_confusion(y, labels_hard, f"Hardcore K={k}")

    # Sklearn
    print("\n[Sklearn]")
    start = time.time()  # Início da medição do tempo
    labels_sk, centers_sk = run_kmeans_sklearn(X_scaled, k)
    elapsed_sk = time.time() - start  # Tempo total de execução
    score_sk = evaluate_labels(X_scaled, labels_sk)
    print(f"Silhouette Score: {score_sk:.4f} | Tempo: {elapsed_sk:.4f}s")
    plot_confusion(y, labels_sk, f"Sklearn K={k}")

# Visualização PCA para k=3
labels_sk, centers_sk = run_kmeans_sklearn(X_scaled, 3)
print("\n===== PCA - Sklearn K=3 =====")
plot_pca_clusters(X_scaled, labels_sk, centers_sk, 2, "PCA (2D) - Sklearn")
plot_pca_clusters(X_scaled, labels_sk, centers_sk, 1, "PCA (1D) - Sklearn")
