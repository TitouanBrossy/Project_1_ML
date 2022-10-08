# -*- coding: utf-8 -*-
import numpy as np

def load_training_data():
    """Load training data and id"""
    path_dataset = "train.csv"
    all_data = np.genfromtxt(path_dataset, delimiter=",", skip_header=1, usecols=[0, 31])
    #predictions = np.genfromtxt(path_dataset, delimiter=",", dtype = str, skip_header=1, usecols=(1))
    ids = all_data[:,0]
    predictions = all_data[:,1]
    data = all_data[:,2:]
    return ids, predictions, data

def load_test_data():
    """Load test data and id"""
    path_dataset = "test.csv"
    all_data = np.genfromtxt(path_dataset, delimiter=",", skip_header=1, usecols=[0, 31])
    ids = all_data[:,0]
    data = all_data[:,2:]
    return ids, data