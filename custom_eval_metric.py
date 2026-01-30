import numpy as np

def weighted_accuracy(y_true, y_pred):
    """
    Custom weighted accuracy metric:
    - Class 0 weight = 1
    - Class 1 weight = 2
    """

    weights = {0: 1, 1: 2}
    correct_weighted = 0
    total_weighted = 0

    for true, pred in zip(y_true, y_pred):
        weight = weights.get(true, 1)
        total_weighted += weight
        if true == pred:
            correct_weighted += weight

    return correct_weighted / total_weighted


# Sample test case
if __name__ == "__main__":
    y_true = np.array([0, 1, 1, 0, 1])
    y_pred = np.array([0, 1, 0, 0, 1])

    score = weighted_accuracy(y_true, y_pred)
    print("Weighted Accuracy:", score)
