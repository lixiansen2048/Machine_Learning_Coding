import numpy as np
from math import sqrt


def accuracy_score(y_true, y_predict):
    assert y_true.shape[0] == y_predict.shape[0], \
        "the size of y_true must be equal to the size of y_predict"

    return sum(y_true == y_predict) / len(y_true)


def Mean_Sqared_Error(y_true, y_predict):
    # 均方误差
    assert len(y_true) == len(y_predict), \
        "the size of y_true must be equal to the size of y_predict"

    return np.sum((y_true - y_predict) ** 2) / len(y_predict)


def Root_Mean_Sqared_Error(y_true, y_predict):
    # 均方根误差
    return sqrt(np.sum((y_true - y_predict) ** 2) / len(y_predict))


def Mean_Absolute_Error(y_true, y_predict):
    # 平均绝对误差
    return np.sum(abs(y_true - y_predict)) / len(y_predict)


def r2_score(y_true, y_predict):
    return 1 - Mean_Sqared_Error(y_true, y_predict) / np.var(y_true)
