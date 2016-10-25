#XOR gate ANN

import numpy, theano
from theano import tensor as T
import theano.tensor.nnet as nnet

X = numpy.array([
    [1, 1],
    [1, 0],
    [0, 1],
    [0, 0]])

Y = numpy.array([0, 1, 1, 0])

x = T.dvector()
y = T.dscalar()

def layer(x, w):
    b = numpy.array([1], dtype=theano.config.floatX)
    x_bias = T.concatenate([x, b])
    z = T.dot(w.T, x_bias)
    return nnet.sigmoid(z)

def grad_desc(cost, theta):
    alpha = 0.01
    return theta - (alpha * T.grad(cost, wrt=theta))

theta1 = theano.shared(numpy.array(numpy.random.rand(3,3)))
theta2 = theano.shared(numpy.array(numpy.random.rand(4,1)))

hid1 = layer(x, theta1)

out1 = T.sum(layer(hid1, theta2))

fc = (out1 - y) ** 2

cost = theano.function(inputs=[x, y], outputs=fc, updates=[
    (theta1, grad_desc(fc, theta1)),
    (theta2, grad_desc(fc, theta2))])

run_forward = theano.function(inputs=[x], outputs=out1)

cur_cost = 0
for i in xrange(100000):
    for k in xrange(len(X)):
        cur_cost = cost(X[k], Y[k])
        if i%500 == 0:
            print cur_cost

print(run_forward([0,1]))
print(run_forward([1,1]))
print(run_forward([1,0]))
print(run_forward([0,0]))
