import numpy as np

from itertools import zip_longest
from tensorflow.examples.tutorials.mnist import input_data
from skimage.transform import resize


def grouper(iterable, batch_size, fill_value=None):
    """ Helper method for returning batches of size batch_size of a dataset.
        grouper('ABCDEF', 3) -> 'ABC', 'DEF'
    """
    args = [iter(iterable)] * batch_size
    return zip_longest(*args, fillvalue=fill_value)

class MNISTIterator(object):

    def __init__(self):
        self.og = input_data.read_data_sets("MNIST_data/", one_hot=True)

    def train_epoch_in_batches(self, batch_size, size=None):
        train_list = list(range(len(self.og.train.images)))
        np.random.shuffle(train_list)
        for batch_i in grouper(train_list, batch_size):
            if size is not None:
                batch = [(resize(
                                 np.reshape(self.og.train.images[i], (28, 28)),
                                 (size, size)),
                          self.og.train.labels[i])
                        for i in batch_i if i is not None]
            else:
                batch = [(self.og.train.images[i], self.og.train.labels[i])
                        for i in batch_i if i is not None]
            yield zip(*batch)

    def test_epoch_in_batches(self, batch_size, size=None):
        test_list = list(range(len(self.og.test.images)))
        np.random.shuffle(test_list)
        for batch_i in grouper(test_list, batch_size):
            if size is not None:
                batch = [(resize(
                                 np.reshape(self.og.test.images[i], (28, 28)),
                                 (size, size)),
                          self.og.test.labels[i])
                        for i in batch_i if i is not None]
            else:
                batch = [(self.og.test.images[i], self.og.test.labels[i])
                        for i in batch_i if i is not None]
            yield zip(*batch)
