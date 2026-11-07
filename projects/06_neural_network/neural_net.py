"""A tiny neural network written from scratch (no libraries).

Task: a robot has two bump sensors (left, right). It should turn when
exactly one sensor is pressed - this is the XOR problem, which a single
neuron cannot solve but a network with one hidden layer can.

Shows: forward pass, sigmoid activation, loss, and backpropagation.

Run:  python neural_net.py
"""
import math
import random

random.seed(42)

DATA = [([0, 0], 0), ([0, 1], 1), ([1, 0], 1), ([1, 1], 0)]
HIDDEN = 4
LEARNING_RATE = 0.5
EPOCHS = 10000


def sigmoid(z):
    return 1.0 / (1.0 + math.exp(-z))


class TinyNet:
    def __init__(self, n_in, n_hidden):
        r = lambda: random.uniform(-1, 1)
        self.w1 = [[r() for _ in range(n_in)] for _ in range(n_hidden)]
        self.b1 = [r() for _ in range(n_hidden)]
        self.w2 = [r() for _ in range(n_hidden)]
        self.b2 = r()

    def forward(self, x):
        self.x = x
        self.h = [sigmoid(sum(w * xi for w, xi in zip(ws, x)) + b)
                  for ws, b in zip(self.w1, self.b1)]
        self.out = sigmoid(sum(w * h for w, h in zip(self.w2, self.h)) + self.b2)
        return self.out

    def backward(self, target, lr):
        # Gradient of squared error through the output sigmoid.
        d_out = (self.out - target) * self.out * (1 - self.out)
        for j, h in enumerate(self.h):
            d_h = d_out * self.w2[j] * h * (1 - h)   # uses w2 before it changes
            self.w2[j] -= lr * d_out * h
            for i, xi in enumerate(self.x):
                self.w1[j][i] -= lr * d_h * xi
            self.b1[j] -= lr * d_h
        self.b2 -= lr * d_out


if __name__ == "__main__":
    net = TinyNet(2, HIDDEN)
    for epoch in range(EPOCHS + 1):
        loss = 0.0
        for x, y in DATA:
            loss += (net.forward(x) - y) ** 2
            net.backward(y, LEARNING_RATE)
        if epoch % 2000 == 0:
            print(f"epoch {epoch:5d}  loss {loss / len(DATA):.4f}")

    print("\nleft right -> turn?")
    for x, y in DATA:
        p = net.forward(x)
        print(f"  {x[0]}     {x[1]}   -> {p:.2f} ({'turn' if p > 0.5 else 'straight'}),"
              f" expected {'turn' if y else 'straight'}")
