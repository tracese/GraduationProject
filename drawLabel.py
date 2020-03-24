import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split

# ----------------------给数据集添加标签------------------- #
def addLabel():
    df = pd.read_csv('./data/000001.csv', index_col='date')
    df = df[:100][['open', 'low', 'high', 'close', 'volume', 'p_change']].copy()
    m = df.shape[0]
    df['label'] = np.zeros((m, 1))

    for i in range(m):
        p_change = df['p_change'].iloc[i]
        if p_change >= 0:
            df['label'].iloc[i] = 1
        else:
            df['label'].iloc[i] = -1
    df.drop(['p_change'],axis=1)
    return df


# ----------------------切割数据集------------------- #
def split_train_test():
    df = addLabel()
    X = df.iloc[:, :-1].values
    Y = df.iloc[:, -1].values
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3)
    X_train = np.mat(X_train)
    X_test = np.mat(X_test)
    Y_train = np.mat(Y_train).T
    Y_test = np.mat(Y_test).T
    return X_train, Y_train, X_test, Y_test


# addLabel()
split_train_test()
