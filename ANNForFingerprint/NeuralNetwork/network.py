import matplotlib.pyplot as plt
import numpy as np

from theano import tensor as T

import data

def data_loader():
    data_processor = data.Processor()
    dataset = data_processor.get_dataset()
    data_length = len(dataset)
    training_set = dataset[:(data_length*6/10)]
    validation_set = dataset[(data_length*6/10): (data_length*8/10)]
    test_set = dataset[(data_length*8/10):]
    print "training_length:", len(training_set),
    print "validation_length:", len(validation_set),
    print "test_length:", len(test_set)
    return [
        training_set,
        validation_set,
        test_set
    ]

def sigmoid(z):
    return 1.0/(1.0+np.exp(-z))

def sigmoid_prime(z):
    return sigmoid(z)*(1-sigmoid(z))


class CrossEntropyCost(object):
    @staticmethod
    def func(a, y):
        return np.sum(np.nan_to_num(-y * np.log(a) - (1-y) * np.log(1-a)))
    @staticmethod
    def deriv(z, a, y):
        return (a - y)

class Network(object):
    def __init__(self, layer_sizes):
        self.layer_count = len(layer_sizes)
        self.layer_sizes = layer_sizes
        self.cost=CrossEntropyCost
        # large weight initialization
        self.parameters = [np.random.randn(y, x) for x, y in zip(self.layer_sizes[:-1], self.layer_sizes[1:])]
        self.biases = [np.random.randn(y, 1) for y in self.layer_sizes[1:]]

    def feed_forward(self, a):
        for b, w in zip(self.biases, self.parameters):
            a = sigmoid(np.dot(w, a) + b)
        return a

    def SGD(self,
            training_data,
            epochs,
            training_batch_size,
            eta,
            lmbda = 0.0,
            test_data = [],
            debug = ['tr_cost', 'tr_acc', 'test_cost', 'test_acc']):
        n_test_data = len(test_data)
        n = len(training_data)
        test_cost, test_accuracy = [], []
        training_cost, training_accurary = [], []
        for j in xrange(epochs):
            batches = [training_data[k: k + training_batch_size] for k in xrange(0, n, training_batch_size)]
            for batch in batches:
                self.grad_desc(batch, eta, lmbda, n)
            print "Epoch : %s" % j
            if j / 600 == 1:
                eta /= 3
            if 'tr_cost'   in debug: print "training_cost : {}".format(self.total_cost(training_data, lmbda))
            if 'tr_acc'    in debug: print "training_acc  : {}".format(self.accuracy(training_data))
            if 'test_cost' in debug: print "testing_cost : {}".format(self.total_cost(test_data, lmbda))
            if 'test_acc'  in debug: print "testing_acc  : {}".format(self.accuracy(test_data))

    def grad_desc(self, batch, eta, lmbda, n):
        acc_b = [np.zeros(b.shape) for b in self.biases]
        acc_w = [np.zeros(w.shape) for w in self.parameters]
        for x, y in batch:
            delta_b, delta_w = self.back_propagate(x, y)
            acc_b = [b + db for b, db in zip(acc_b, delta_b)]
            acc_w = [w + dw for w, dw in zip(acc_w, delta_w)]
        self.parameters = [(1 - eta * (lmbda/n)) * w - (eta/len(batch)) * aw
                           for w, aw in zip(self.parameters, acc_w)]
        self.biases = [b - (eta/len(batch)) * ab
                       for b, ab in zip(self.biases, acc_b)]

    def back_propagate(self, x, y):
        acc_b = [np.zeros(b.shape) for b in self.biases]
        acc_w = [np.zeros(w.shape) for w in self.parameters]
        activation = x
        activations = [x]
        zs = []
        for b, w in zip(self.biases, self.parameters):
            z = np.dot(w, activation) + b
            zs.append(z)
            activation = sigmoid(z)
            activations.append(activation)
        delta = self.cost.deriv(zs[-1], activations[-1], y)
        acc_b[-1] = delta
        acc_w[-1] = np.dot(delta, activations[-2].T)
        for l in xrange(2, self.layer_count):
            z = zs[-l]
            sp = sigmoid_prime(z)
            delta = np.dot(self.parameters[-l+1].T, delta) * sp
            acc_b[-l] = delta
            acc_w[-l] = np.dot(delta, activations[-l-1].T)
        return (acc_b, acc_w)

    def total_cost(self, data, lmbda):
        cost = 0.0
        for x, y in data:
            a = self.feed_forward(x)
            cost += self.cost.func(a, y)/len(data)
        cost += 0.5 * (lmbda/len(data)) * sum(
            np.linalg.norm(w)**2 for w in self.parameters)
        return cost

    def accuracy(self, data):
        results = [(np.argmax(self.feed_forward(x)), np.argmax(y))
                   for (x, y) in data]
        return sum(int(x==y) for (x, y) in results)
