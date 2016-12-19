import network

def run():
    training_data, validation_data, test_data = network.data_loader()
    print len(training_data), len(validation_data), len(test_data)
    net = network.Network([7298, 300, 100])
    net.SGD(training_data, 5000, 10, 0.01, 0.0, test_data, ['tr_acc', 'tr_cost'])

run()