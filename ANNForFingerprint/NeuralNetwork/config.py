#--------------------------------------------------------------------------------
# ,-. ,-. ,-. ," . ,-.
# |   | | | | |- | | |
# `-' `-' ' ' |  ' `-|
#             '     ,|
#--------------------------------------------------------------------------------

config = {
    # number of training examples
    'm' : 5,
    # image dimensions
    'image_dimension'    : {
        'height' : 89,
        'width'  : 82
    },
    'output_bit_encoding' : 100,
    # dataset path relative to this file
    'dataset_path' : './../FingerprintDataset',
    # dataset indexed with 0 or 1
    'zero_indexed' : True,
    # label to denote left hand
    'left_label' : 'L',
    # label to denote right hand
    'right_label' : 'R',
    'alpha' : 0.1
}

# thumb -> 0
# 2nd finger -> 1
# 3rd finger -> 2
# 4th finger -> 3
finger_keys = ['0', '1', '2', '3']
# finger_keys = ['0', '1']
image_indices = ['0', '1', '2', '3', '4']
# image_indices = ['0', '1']

# hand labels
hand_labels = [config['left_label'], config['right_label']]
# hand_labels = [config['left_label']]

# number of nodes in each layer
nn_config = [config['image_dimension']['height'] * config['image_dimension']['width'], 30, config['output_bit_encoding']]
