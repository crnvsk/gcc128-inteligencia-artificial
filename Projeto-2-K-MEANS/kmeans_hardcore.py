import numpy as np

class KMeansHardcore:
    def __init__(self, n_clusters=3, max_iter=300, tol=1e-4):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.tol = tol

    def fit(self, X):
        np.random.seed(42)
        random_idx = np.random.permutation(X.shape[0])[:self.n_clusters]
        self.centroids = X[random_idx]
        
        for _ in range(self.max_iter):
            distances = self._euclidean_distance(X, self.centroids)
            self.labels = np.argmin(distances, axis=1)

            new_centroids = np.array([
                X[self.labels == j].mean(axis=0) for j in range(self.n_clusters)
            ])

            if np.linalg.norm(self.centroids - new_centroids) < self.tol:
                break

            self.centroids = new_centroids

    def predict(self, X):
        distances = self._euclidean_distance(X, self.centroids)
        return np.argmin(distances, axis=1)

    def _euclidean_distance(self, X, centroids):
        return np.linalg.norm(X[:, np.newaxis] - centroids, axis=2)
