from sklearn.metrics import silhouette_score, confusion_matrix
import time
import matplotlib.pyplot as plt
import seaborn as sns

def evaluate_model(model, X):
    start = time.time()
    model.fit(X)
    elapsed = time.time() - start
    labels = model.labels
    score = silhouette_score(X, labels)
    return labels, score, elapsed

def evaluate_labels(X, labels):
    score = silhouette_score(X, labels)
    return score

def plot_confusion(y_true, y_pred, title="Matriz de Confusão"):
    cm = confusion_matrix(y_true, y_pred)
    plt.figure(figsize=(5, 4))
    sns.heatmap(cm, annot=True, fmt="d", cmap="Blues")
    plt.title(title)
    plt.xlabel("Cluster")
    plt.ylabel("Classe Real")
    plt.show()
