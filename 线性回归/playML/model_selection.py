import numpy as np


def train_test_split(X, y, test_ratio=0.2, seed=None):
    """将数据 X 和 y 按照 test_ratio 分割称X_train,X_test,y_train,y_test"""

    assert X.shape[0] == y.shape[0],\
    "the size of X must be equal to the size of y"
    assert 0.0 <= test_ratio <= 1.0,\
    "test_ratio must be valid"

    if seed:
        np.random.seed(seed)

    shuffled_index = np.random.permutation(len(X))

    test_num = int(len(X) * test_ratio)

    index_test = shuffled_index[:test_num]
    index_train = shuffled_index[test_num:]

    X_train = X[index_train]
    y_train = y[index_train]

    X_test = X[index_test]
    y_test = y[index_test]

    return X_train, X_test, y_train, y_test
