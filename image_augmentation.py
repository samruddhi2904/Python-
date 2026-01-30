import tensorflow as tf
from tensorflow.keras import layers

def create_image_augmentation_pipeline():
    """
    Creates an image augmentation pipeline using Keras:
    - Random rotation (±20 degrees)
    - Random horizontal flip
    - Random zoom (0.2x)
    """

    data_augmentation = tf.keras.Sequential([
        layers.RandomRotation(0.2),
        layers.RandomFlip("horizontal"),
        layers.RandomZoom(0.2)
    ])

    return data_augmentation


# Sample usage
if __name__ == "__main__":
    augmentation_pipeline = create_image_augmentation_pipeline()
    print("Image augmentation pipeline created successfully.")
