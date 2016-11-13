import theano.tensor as T
import numpy, theano
import theano.tensor.nnet as nnet

X = numpy.array([
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
])

Y = numpy.array([
    [0, 0, 0, 0],
    [0, 0, 0, 1],
    [0, 0, 1, 0],
    [0, 0, 1, 1],
    [0, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 1, 1, 0],
    [0, 1, 1, 1],
    [1, 0, 0, 0],
    [1, 0, 0, 1],
    [1, 0, 1, 0]
])

x = T.dvector('x')
y = T.dvector('y')

def layer(x, w):
    b = numpy.array([1], dtype=theano.config.floatX)
    x_bias = T.concatenate([x, b]).T
    z = T.dot(w, x_bias)
    return nnet.sigmoid(z)

def grad_desc(cost, theta):
    alpha = 0.1
    return theta - (alpha * T.grad(cost, wrt=theta))

theta = theano.shared(numpy.array(numpy.random.rand(4, 11)))

output = layer(x, theta)
squared_error = T.sum((output - y) ** 2)

cost = theano.function(inputs=[x, y],
                       outputs=squared_error,
                       updates=[
                           (theta, grad_desc(squared_error, theta))
                       ])

recognize = theano.function(inputs=[x], outputs=output)

print 'training'
for i in xrange(10000):
    for k in xrange(len(X)):
        cost(X[k], Y[k])
    if i%500 == 0:
        print str(i/100.0) + '%'

print '-------------------------------------theta--------------------------------------'
print theta.get_value()
print '--------------------------------------------------------------------------------'
for k in xrange(len(X[k])):
    print recognize(X[k]), ' -> ', Y[k]
