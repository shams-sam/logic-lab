import numpy, random
from scipy import misc
from config import *
import random

#--------------------------------------------------------------------------------
#   .     .
# ,-| ,-. |- ,-.   ,-. ,-. ,-. ,-. ,-. ,-. ,-. . ,-. ,-.
# | | ,-| |  ,-|   | | |   | | |   |-' `-. `-. | | | | |
# `-^ `-^ `' `-^   |-' '   `-' `-' `-' `-' `-' ' ' ' `-|
#                  |                                  ,|
#                  '                                  `'
#--------------------------------------------------------------------------------

class Processor:
    def import_bmp(self, path, flatten):
        image_mat = misc.imread(path, flatten = flatten)
        return image_mat

    def folder_namer(self, num):
        return str(num).zfill(3)

    def file_namer(self, num, hand_label, finger_key, image_index):
        folder_name = self.folder_namer(num)
        return '_'.join([folder_name, hand_label + finger_key, image_index + '.bmp'])

    def get_path(self, path, num, hand_label, finger_key, image_index):
        return '/'.join([path, self.folder_namer(num), hand_label, self.file_namer(num, hand_label, finger_key, image_index)])

    def data_prefetch(self):
        offset = 0 if config['zero_indexed'] else 1
        X = numpy.empty((nn_config[0], 1), int)
        Y = numpy.empty((nn_config[2], 1), int)
        for num in xrange(0 + offset, config['m'] + offset):
            for hand_label in hand_labels:
                for finger_key in finger_keys:
                    for image_index  in image_indices:
                        finger_print = self.import_bmp(self.get_path(config['dataset_path'], num, hand_label, finger_key, image_index), 0)
                        finger_print = finger_print.reshape(nn_config[0], 1)
                        X = numpy.concatenate((X, finger_print), axis = 1)
                        Y_i = numpy.zeros(100)
                        Y_i[num] = 1
                        Y = numpy.concatenate((Y, Y_i.reshape(config['output_bit_encoding'], 1)), axis = 1)
        X = numpy.delete(X, (0), axis = 1).T
        X = X/255.0
        Y = numpy.delete(Y, (0), axis = 1).T
        return zip(X, Y)

    def get_dataset(self):
        data = []
        print 'fetching dataset ... '
        for elem in self.data_prefetch():
            data.append([elem[0].reshape(nn_config[0], 1), elem[1].reshape(config['output_bit_encoding'], 1)])
        random.shuffle(data)
        return data
