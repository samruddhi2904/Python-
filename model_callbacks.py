import tensorflow as tf
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from tensorflow.keras.utils import to_categorical

def create_early_stopping_callback():
    """
    Creates an EarlyStopping callback that:
    - Monitors validation loss
    - Stops training if no improvement for 3 epochs
    - Restores best model weights
    """

    early_stopping = EarlyStopping(
        monitor="val_loss",
        patience=3,
        restore_best_weights=True
    )

    return early_stopping


# Sample usage
if __name__ == "__main__":
    # Load dataset
    X, y = load_iris(return_X_y=True)
    y = to_categorical(y)

    X_train, X_val, y_train, y_val = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    # Simple model
    model = Sequential([
        Dense(32, activation="relu", input_shape=(X.shape[1],)),
        Dense(16, activation="relu"),
        Dense(y.shape[1], activation="softmax")
    ])

    model.compile(
        optimizer="adam",
        loss="categorical_crossentropy",
        metrics=["accuracy"]
    )

    # Train with EarlyStopping
    model.fit(
        X_train,
        y_train,
        validation_data=(X_val, y_val),
        epochs=50,
        callbacks=[create_early_stopping_callback()],
        verbose=1
    )
