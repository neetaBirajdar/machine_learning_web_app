from keras import layers, Sequential
from keras.datasets import mnist
from keras.models import load_model
import os


    
def train_neutral_network():
    (train_images, train_labels), ( test_images, test_labels) = mnist.load_data()
    model= Sequential([layers.Dense(512, activation="relu"),
                    layers.Dense(10, activation="softmax")])


    model.compile(optimizer="adam", 
                loss= "sparse_categorical_crossentropy",
                metrics=["accuracy"])

    train_images = train_images.reshape((60000, 28*28))
    train_images = train_images.astype("float32")/255


    model.fit(train_images, train_labels, epochs=5, batch_size=128)
    model.save(filepath="./trained_model.keras")
    return model

def detect_number(test_image):
    file_path= "./trained_model.keras"
    # Check if trained file exists
    if os.path.exists(file_path):
        print("Trained File exists")
        # Load the pre-trained model
        model = load_model(file_path)
    else:
        print("Trained File does not exist")
        model = train_neutral_network()
        
    test_digit = test_image.reshape(1, test_image.size)
    predictions = model.predict(test_digit)
    print("\nPredictions:",predictions,"\nPrediction MaxValue:", predictions.argmax(),"\n")
    return predictions.argmax()