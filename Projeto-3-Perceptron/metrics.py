from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score

def calculate_metrics(y_true, y_pred):
    """
    Calcula e retorna acurácia, precisão e recall.
    """
    accuracy = accuracy_score(y_true, y_pred)
    precision = precision_score(y_true, y_pred, average='weighted')
    recall = recall_score(y_true, y_pred, average='weighted')
    return accuracy, precision, recall
