import pandas as pd
from scipy.sparse import csr_matrix
from sklearn.linear_model import LogisticRegression


def fit_predict(x_train: csr_matrix, y_train: pd.Series, x_test: csr_matrix) -> pd.Series:
    """
    Создаёт модель логистической регрессии и делает предсказание

    :param x_train: признаки обучающей выборки
    :param y_train: ответы к обучающей выборке
    :param x_test: признаки тестовой выборки
    :return: вероятности класса 1 для тестовой выборки
    """
    lr = LogisticRegression(random_state=17, max_iter=500, C=0.71, n_jobs=-1).fit(x_train, y_train)
    return lr.predict_proba(x_test)[:, 1]
