import numpy as np

from tensorflow.examples.tutorials.mnist import input_data
from utils import grouper


class MNISTIterator(object):

    def __init__(self):
        self.og = input_data.read_data_sets("MNIST_data/", one_hot=True)

    @property
    def io_shape(self):
        return 784, 10

    def train_epoch_in_batches(self, batch_size):
        train_list = list(range(len(self.og.train.images)))
        np.random.shuffle(train_list)
        for batch_i in grouper(train_list, batch_size):
            batch = [(self.og.train.images[i], self.og.train.labels[i])
                    for i in batch_i if i is not None]
            yield zip(*batch)

    def test_epoch_in_batches(self, batch_size):
        test_list = list(range(len(self.og.test.images)))
        np.random.shuffle(test_list)
        for batch_i in grouper(test_list, batch_size):
            batch = [(self.og.test.images[i], self.og.test.labels[i])
                    for i in batch_i if i is not None]
            yield zip(*batch)
