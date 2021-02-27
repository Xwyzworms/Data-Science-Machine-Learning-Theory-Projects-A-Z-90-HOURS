# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 15:00:42 2021

@author: xwyzworm
"""

def findCorrelation(dataset,threshold : int):
    """
    Find The columns Which Lower than Threshold from whole dataset
    All Type should be numeric otherwise return error
    dataset : pandas.DataFrame
    threshold : int
    """
    cols = set()
    correlation_matrix = dataset.corr()
    for i in range(len(correlation_matrix.columns)):
        for j in range(i):
            if np.abs(correlation_matrix.iloc[i,j]) > threshold:
                cols.add(correlation_matrix.columns[i])
    return cols

