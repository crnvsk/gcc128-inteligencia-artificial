import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score
import matplotlib.pyplot as plt
import seaborn as sns
import time

def sklearn_knn_classifier(k):
    # Carrega o dataset
    df = pd.read_csv("iris.csv")

    # Divide em treino e teste (80/20)
    X = df[['SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']]
    y = df['Species']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=123)

    # Treina o classificador KNN
    start_time = time.time()
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    sklearn_time = time.time() - start_time

    # Gera a matriz de confusão
    cm = confusion_matrix(y_test, y_pred, labels=df['Species'].unique())
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=df['Species'].unique(), yticklabels=df['Species'].unique())
    plt.title("Matriz de Confusão (Sklearn)")
    plt.xlabel("Previsão")
    plt.ylabel("Verdadeiro")
    plt.savefig("confusion_matrix_sklearn.png")
    print("Arquivo confusion_matrix_sklearn.png gerado com sucesso!")

    # Calcula métricas de avaliação
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='weighted')
    recall = recall_score(y_test, y_pred, average='weighted')
    print(f"Acurácia (Sklearn): {accuracy:.2f}")
    print(f"Precisão (Sklearn): {precision:.2f}")
    print(f"Revocação (Sklearn): {recall:.2f}")

    return accuracy, precision, recall, sklearn_time

if __name__ == "__main__":
    sklearn_knn_classifier(k=3)