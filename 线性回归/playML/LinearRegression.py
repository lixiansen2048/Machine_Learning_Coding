import numpy as np
from .metrics import r2_score


class LinearRegression:

    def __init__(self):
        # 初始化模型
        self.coef_ = None
        self.interception_ = None
        self._theta = None

    def fit_normal(self, X_train, y_train):
        # 根据训练集训练线性规划模型
        assert X_train.shape[0] == y_train.shape[0], \
            "the size of X_train must be equal to the size of y_train"

        X_b = np.hstack([np.ones((len(X_train), 1)), X_train])
        self._theta = np.linalg.inv(X_b.T.dot(X_b)).dot(X_b.T).dot(y_train)

        self.interception_ = self._theta[0]
        self.coef_ = self._theta[1:]
        return self

    def fit_gd(self, X_train, y_train, eta=0.01, n_iters=1e4):
        # 根据训练集，使用梯度下降法训练模型
        assert X_train.shape[0] == y_train.shape[0], \
            "the size of X_train must be equal to the size of y_train"

        def J(X_b, y, theta):
            m = len(X_b)
            try:
                return np.sum((y - X_b.dot(theta)) ** 2) / m
            except:
                return float('inf')

        def dJ(X_b, y, theta):
            # res = np.empty(len(theta))
            # res[0] = np.sum(X_b.dot(theta) - y)
            # for i in range(1,len(theta)):
            #     res[i] = (X_b.dot(theta) - y).dot(X_b[:,i])
            # return res * 2 / len(X_b)
            return X_b.T.dot(X_b.dot(theta) - y) * 2. / len(X_b)

        def gradient_descent(initial_theta, X_b, y, eta, n_iters=1e4, epsilon=1e-8):
            theta = initial_theta
            i_iter = 0

            while i_iter < n_iters:
                gradient = dJ(X_b, y, theta)
                last_theta = theta
                theta = theta - eta * gradient

                if abs(J(X_b, y, theta) - J(X_b, y, last_theta)) < epsilon:
                    break
                i_iter += 1
            return theta

        X_b = np.hstack([np.ones((len(X_train), 1)), X_train])
        initial_theta = np.zeros(X_b.shape[1])
        self._theta = gradient_descent(initial_theta, X_b, y_train, eta, n_iters)

        self.interception_ = self._theta[0]
        self.coef_ = self._theta[1:]

        return self

    def fit_sgd(self,X_train,y_train,n_iters=5,t0=5,t1=50):
        # 根据训练集，使用梯度下降法训练模型
        assert X_train.shape[0] == y_train.shape[0], \
            "the size of X_train must be equal to the size of y_train"

        def dJ_sgd(theta,X_b_i,y_i):
            return X_b_i.T.dot(X_b_i.dot(theta) - y_i) * 2


        def sgd(initial_theta, X_b,y):
            def learning_rate(t):
                return t0 / (t + t1)

            theta = initial_theta
            m = len(X_b)

            for cur_iter in range(n_iters):
                indexes = np.random.permutation(m)
                X_b_new = X_b[indexes]
                y_new = y[indexes]
                for i in range(m):
                    gradient = dJ_sgd(theta,X_b_new[i],y_new[i])
                    theta = theta - learning_rate(cur_iter * m + i) * gradient
            return theta

        X_b = np.hstack([np.ones((len(X_train),1)),X_train])
        initial_theta = np.zeros(X_b.shape[1])

        self._theta = sgd(initial_theta,X_b,y_train)
        self.interception_ = self._theta[0]
        self.coef_ = self._theta[1:]

        return self

    def predict(self, X_predict):
        X_b = np.hstack([np.ones((len(X_predict), 1)), X_predict])
        return X_b.dot(self._theta)

    def score(self, X_test, y_test):
        y_predict = self.predict(X_test)
        return r2_score(y_test, y_predict)

    def __repr__(self):
        return "LinearRegression()"
