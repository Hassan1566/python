import tensorflow as tf
from tensorflow.keras import datasets, layers, models
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix

# 1. Load the Fashion-MNIST dataset
(train_images, train_labels), (test_images, test_labels) = datasets.fashion_mnist.load_data()

# Define the text labels for the dataset categories
class_names = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
               'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

# 2. Normalize pixel values to the range [0, 1]
train_images = train_images / 255.0
test_images = test_images / 255.0

# 3. Reshape the images to (28, 28, 1) for the CNN input layer
train_images = train_images.reshape((train_images.shape[0], 28, 28, 1))
test_images = test_images.reshape((test_images.shape[0], 28, 28, 1))

print(f"Training images shape: {train_images.shape}")
print(f"Test images shape: {test_images.shape}")

# 4. Visualize a few sample images with their corresponding labels
plt.figure(figsize=(10,4))
for i in range(5):
    plt.subplot(1, 5, i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(train_images[i].reshape(28, 28), cmap=plt.cm.binary)
    plt.xlabel(class_names[train_labels[i]])
plt.show()

# 1. Design the multi-layer CNN Architecture
model = models.Sequential([
    # First Convolutional Layer
    layers.Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)),
    layers.MaxPooling2D((2, 2)),
    
    # Second Convolutional Layer
    layers.Conv2D(64, (3, 3), activation='relu'),
    layers.MaxPooling2D((2, 2)),
    
    # Dropout layer for regularization to prevent overfitting
    layers.Dropout(0.25),
    
    # Flatten layer to feed into Dense layers
    layers.Flatten(),
    
    # Hidden Dense Layer
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.5),
    
    # Output Layer (10 classes for 10 fashion categories)
    layers.Dense(10, activation='softmax')
])

# 2. Compile the model
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Display the model architecture summary
model.summary()

# Train the model with a 20% validation split
EPOCHS = 10
history = model.fit(train_images, train_labels, 
                    epochs=EPOCHS, 
                    validation_split=0.2, 
                    batch_size=64)

# 1. Evaluate the model on test data
test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)
print(f"\nTest Accuracy: {test_acc*100:.2f}%")
print(f"Test Loss: {test_loss:.4f}\n")

# 2. Generate predictions
predictions = model.predict(test_images)
pred_labels = np.argmax(predictions, axis=1)

# 3. Print the Classification Report
print("Classification Report:\n")
print(classification_report(test_labels, pred_labels, target_names=class_names))

# 4. Print the Confusion Matrix
print("Confusion Matrix:\n")
print(confusion_matrix(test_labels, pred_labels))

# 1. Plot Training & Validation Loss and Accuracy Curves
plt.figure(figsize=(12, 5))

# Plot Accuracy Curves
plt.subplot(1, 2, 1)
plt.plot(history.history['accuracy'], label='Training Accuracy', marker='o')
plt.plot(history.history['val_accuracy'], label = 'Validation Accuracy', marker='x')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.title('Training and Validation Accuracy')
plt.legend(loc='lower right')
plt.grid(True)

# Plot Loss Curves
plt.subplot(1, 2, 2)
plt.plot(history.history['loss'], label='Training Loss', marker='o')
plt.plot(history.history['val_loss'], label = 'Validation Loss', marker='x')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.title('Training and Validation Loss')
plt.legend(loc='upper right')
plt.grid(True)

plt.show()

# 2. Plot a few test images with their predicted and true labels
plt.figure(figsize=(12, 6))
for i in range(5):
    plt.subplot(1, 5, i+1)
    plt.xticks([])
    plt.yticks([])
    plt.grid(False)
    plt.imshow(test_images[i].reshape(28, 28), cmap=plt.cm.binary)
    
    predicted_label = pred_labels[i]
    true_label = test_labels[i]
    
    # Color green if correct, red if incorrect
    color = 'green' if predicted_label == true_label else 'red'
    
    plt.xlabel(f"Pred: {class_names[predicted_label]}\nTrue: {class_names[true_label]}", color=color)
plt.tight_layout()
plt.show()