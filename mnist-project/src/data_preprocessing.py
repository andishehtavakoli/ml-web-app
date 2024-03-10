import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import datasets

from loguru import logger

def mnist_data_load():

    try:
        # Load data
        data = datasets.load_digits()
        logger.info('Reading data ..')
        logger.info(f'data shape : {data.images.shape}')

    except Exception as e:
        print(e)
    return data

def mnist_data_prepare(data):

    # Combine images and labels
    images_labels = list(zip(data.images, data.target))
    logger.info(f'data shape after combination: {np.shape(data.images)}')

    # Flate the combined data
    X = data.images.reshape((len(data.images), -1))
    logger.info(f'data shape after flatten: {X.shape}')
    y = data.target

    return X, y