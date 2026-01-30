from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.datasets import load_iris

def tune_random_forest():
    """
    Uses GridSearchCV to find the best hyperparameters
    for a Random Forest classifier.
    """

    # Load sample dataset
    X, y = load_iris(return_X_y=True)

    # Define model
    rf = RandomForestClassifier(random_state=42)

    # Define hyperparameter grid
    param_grid = {
        "max_depth": [3, 5, 7],
        "n_estimators": [50, 100]
    }

    # Grid search
    grid_search = GridSearchCV(
        estimator=rf,
        param_grid=param_grid,
        cv=5,
        scoring="accuracy"
    )

    grid_search.fit(X, y)

    print("Best Parameters:", grid_search.best_params_)
    print("Best Accuracy:", grid_search.best_score_)

    return grid_search.best_params_


# Sample execution
if __name__ == "__main__":
    tune_random_forest()
