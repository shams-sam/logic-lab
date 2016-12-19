import network
import numpy

training_data = [
    (numpy.array([[0], [0]]), numpy.array([[0]])),
    (numpy.array([[0], [1]]), numpy.array([[1]])),
    (numpy.array([[1], [0]]), numpy.array([[1]])),
    (numpy.array([[1], [1]]), numpy.array([[0]])),
]

net = network.Network([2, 3, 1])
net.SGD(training_data, 5000, 4, 1.0, 0.0, training_data, [])
for elem in training_data:
    print net.feed_forward(elem[0]), elem[1]
