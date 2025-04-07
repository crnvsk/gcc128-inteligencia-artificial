import time
from knn_hc import evaluate_multiple_k_values
from knn_sklearn import evaluate_multiple_k_values_sklearn

def compare_classifiers():
    # Valores de k para testar
    k_values = [1, 3, 5, 7]

    # Executa o classificador hardcore
    print("Executando o classificador hardcore para múltiplos valores de k...")
    start_time_hc = time.time()
    hc_results = evaluate_multiple_k_values(k_values)
    hc_time = time.time() - start_time_hc

    # Executa o classificador Sklearn
    print("\nExecutando o classificador Sklearn para múltiplos valores de k...")
    start_time_sklearn = time.time()
    sklearn_results = evaluate_multiple_k_values_sklearn(k_values)
    sklearn_time = time.time() - start_time_sklearn

    # Exibe a comparação de desempenho
    print("\n--- Comparação de Desempenho ---")
    print(f"Tempo total de execução (Hardcore): {hc_time:.2f} segundos")
    print(f"Tempo total de execução (Sklearn): {sklearn_time:.2f} segundos")

    # Exibe a comparação de métricas para cada valor de k
    print("\n--- Comparação de Métricas por k ---")
    for i, k in enumerate(k_values):
        print(f"\nk={k}:")
        print(f"  Hardcore -> Acurácia: {hc_results[i]['accuracy']:.2f}, Precisão: {hc_results[i]['precision']:.2f}, Revocação: {hc_results[i]['recall']:.2f}")
        print(f"  Sklearn  -> Acurácia: {sklearn_results[i]['accuracy']:.2f}, Precisão: {sklearn_results[i]['precision']:.2f}, Revocação: {sklearn_results[i]['recall']:.2f}")

if __name__ == "__main__":
    compare_classifiers()