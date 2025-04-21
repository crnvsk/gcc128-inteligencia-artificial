from sklearn.cluster import KMeans

def run_kmeans_sklearn(X, k, random_state=42):
    model = KMeans(n_clusters=k, random_state=random_state, n_init=10)
    model.fit(X)
    return model.labels_, model.cluster_centers_
