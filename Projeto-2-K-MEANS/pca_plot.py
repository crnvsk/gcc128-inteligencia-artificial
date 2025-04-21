from sklearn.decomposition import PCA
import matplotlib.pyplot as plt

def plot_pca_clusters(X_scaled, labels, centroids, n_components=2, title=""):
    pca = PCA(n_components=n_components)
    X_pca = pca.fit_transform(X_scaled)
    centroids_pca = pca.transform(centroids)

    plt.figure(figsize=(8, 6))
    if n_components == 2:
        plt.scatter(X_pca[:, 0], X_pca[:, 1], c=labels, cmap='viridis', s=50, alpha=0.6)
        plt.scatter(centroids_pca[:, 0], centroids_pca[:, 1], c='red', s=200, marker='X')
        plt.xlabel("Componente 1")
        plt.ylabel("Componente 2")
    else:
        plt.scatter(range(len(X_pca)), X_pca[:, 0], c=labels, cmap='viridis', s=20)
        plt.scatter(range(len(centroids_pca)), centroids_pca[:, 0], c='red', marker='X', s=100)
        plt.ylabel("Componente Principal 1")
    plt.title(title)
    plt.grid(True)
    plt.show()
