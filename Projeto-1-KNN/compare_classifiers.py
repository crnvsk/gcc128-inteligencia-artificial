import time
from knn_hc import main_algorithm
from knn_sklearn import sklearn_knn_classifier

def compare_classifiers():
    # Executa o classificador hardcore
    print("Executando o classificador hardcore...")
    start_time_hc = time.time()
    hc_metrics = main_algorithm(k_input=3)
    hc_time = time.time() - start_time_hc

    # Executa o classificador Sklearn
    print("\nExecutando o classificador Sklearn...")
    sklearn_metrics = sklearn_knn_classifier(k=3)

    # Exibe a comparação de desempenho
    print("\n--- Comparação de Desempenho ---")
    print(f"Tempo de execução (Hardcore): {hc_time:.2f} segundos")
    print(f"Tempo de execução (Sklearn): {sklearn_metrics[3]:.2f} segundos")
    print("\n--- Comparação de Métricas ---")
    print(f"Acurácia (Hardcore): {hc_metrics[0]:.2f}")
    print(f"Acurácia (Sklearn): {sklearn_metrics[0]:.2f}")
    print(f"Precisão (Hardcore): {hc_metrics[1]:.2f}")
    print(f"Precisão (Sklearn): {sklearn_metrics[1]:.2f}")
    print(f"Revocação (Hardcore): {hc_metrics[2]:.2f}")
    print(f"Revocação (Sklearn): {sklearn_metrics[2]:.2f}")

if __name__ == "__main__":
    compare_classifiers()