# implementing a perceptron model to mimic an and gate
# by changing the input it can be trained for the or gate as well
# here becasue the system is linearly seperable no hidden layers are deployed
# but with xor and other such problems hidden layers will be needed

import numpy as np

# input for the and gate
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

# output for the and gate
Y = np.array([0, 0, 0, 1])

# parameter matrix
theta = np.random.rand(1,3)
tolerance = 0.1
alpha = 0.1

def layer(x, w):
    b = np.array([1])
    x_bias = np.concatenate([x, b])
    z = np.sum(np.dot(w, x_bias.T))
    return (1 if z > 0 else 0)


while True:
    error = []
    for idx in xrange(len(X)):
        out = layer(X[idx], theta)
        error_i = Y[idx] - out
        theta = theta + alpha * error_i
        error.append(abs(error_i))
    print error
    if np.sum(error) < tolerance:
        break

print 'output--->'
for ip in X:
    print layer(ip, theta)
