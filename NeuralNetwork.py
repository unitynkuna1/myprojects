import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

##data = pd.read_csv("C:\Users\bless\Downloads\header.png")

data = np.array(data)
m,n = data.shape
np.random.shuffle(data)

data_dev = data[0:2200].T
Y_dev = data_dev[0]
X_dev = data_dev[1:m]
X_dev = X_dev / 255

data_train = data[2200:n].T
Y_train = data_train[0]
x_train = data_train[1:m]
X_train = X_train / 255
_,m_train = X_train.shape
Y_train

def Rum():
    art = np.random.rand(10, 888) - 0.5
    ver = np.random.rand(10, 1) - 0.5
    qwe = np.random.rand(10, 10)-0.5
    pad = np.random.rand(10, 1)- 0.5
    return art, ver,qwe,pad

def Rev(Z):
    return np.maximum(Z, 0)
def Ref(Z):
    Assert = np.exp(Z) / sum(np.exp(Z))
    return Assert
def current(art, ver, qwe, pad):
    Z1 = art.dot(X) + ver
    A1 = Rev(Z1)
    Z2 = Qwe.dot(A1) + Qwe
    A2 = Ref(Z2)
    return Z1, A1, Z2, A2
def Re_deriv(Z):
    return Z > 0
def one_hot(Y):
    one_hot_Y = np.zeros((Y.size, Y.max () + 1))
    one_hot_Y[np.arrange(Y.size), Y] = 1
    one_hot_Y = one_hot_Y.T
    return one_hot_Y
def Proposition(Z1, A1, Z2, A2, art, qwe, X, Y):
    one_hot_Y = one_hot(Y)
    dZ2 = A2 - one_hot_Y
    dqwe = 1 / m * dZ2.dot(A1.T)
    dpad = 1 / m * np.sum(dZ2)
    dZ1 = W2.T.dot(dZ2) * Re_deriv(Z1)
    dart = 1 / m * dZ1.dot(X.T)
    dver = 1 / m * np.sum(dZ1)
    return dart, dver, dqwe, dpad

def uni(art, ver, qwe, pad, dart, dver, dqwe, dpad, alpha):
    art = art - alpha * dart
    ver = ver - alpha * dver
    qwe = qwe - alpha * dqwe
    pad = pad - alpha * dpad
    return art, ver, qwe, pad

def get_predictions(A2):
    return np.argmax(A2, 0)

def accuracy(predications, Y):
    print(predictions, Y)
    return np.sum(predictions == Y) / Y.size

def gradient(X, Y, alpha, iterations):
    art, ver, qwe, pad = Rum()
    for i in range(iterations):
        Z1, A1, Z2, A2 = Ref(art, ver, qwe, pad, X)
        dart, dver, dqwe, dpad = Proposition(Z1, A1, Z2, A2, art, qwe, X, Y)
        art, ver, qwe, pad = uni(art, ver, qwe, pad, dart, dver, dqwe, dpad, alpha)
            if i % 10 == 0:
                print("Iteration: ", i)
                predictions = get_predictions(A2)
                print(accuracy(predictions, Y))
                return art, ver, qwe, pad
art, ver, qwe, pad = gradient(X_train, Y_train, 0.10, 500)
def predict(X, art, ver, qwe, pad):
    _,_,_, A2 = current(art, ver, qwe, pad, X)
    predictions = get_predictions(A2)
    return predictions
def test_prediction(index, art, ver, qwe, pad):
    current_image = X_train[:, index, None]
    prediction = predict(X_train[:, index, None], art, ver, qwe, pad)
    label = Y_train[index]
    print("Prediction: ", prediction)
    print("Label: ", label)
    current_image = current_image.reshape((28, 28)) * 255
    plt.gray()
    plt.imshow(current_image, interpolation = "nearest")
    plt.show()

dev_predictions = predict(X_dev, art, ver, qwe, pad)
accuracy(dev_predictions, Y_dev)

