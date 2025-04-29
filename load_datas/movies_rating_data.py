import numpy as np
import pandas as pd
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import train_test_split


def load_movies_rating_data(folder, cols):
    datas = pd.read_csv(folder, names=cols, sep="\t", encoding="latin-1")
    print(datas)


def drop_timestamp_col(folder, cols):
    datas = pd.read_csv(folder, names=cols, sep="\t", encoding="latin-1")
    rate = datas.drop(columns='timestamp', axis=1)
    print(rate)


def split_user_id_data(folder, cols):
    datas = pd.read_csv(folder, names=cols, sep="\t", encoding="latin-1")
    return datas['user_id']


def split_original_data(folder, cols):
    datas = pd.read_csv(folder, names=cols, sep="\t", encoding="latin-1")
    return datas


def rmse(y_true, y_pred):
    return np.sqrt(mean_squared_error(y_true, y_pred))


def score(model, x_test):
    id_pairs = zip(x_test['user_id'], x_test['movie_id'])
    y_pred = np.array([model(user, movie) for (user, movie) in id_pairs])
    y_true = np.array(x_test['rating'])
    return rmse(y_true, y_pred)


def baseline(user_id, movie_id):
    return 3.0


if __name__ == "__main__":
    columns = ['user_id', 'movie_id', 'rating', 'timestamp']
    path = "../ml-100k/u.data"
    load_movies_rating_data(path, columns)
    drop_timestamp_col(path, columns)

    x = split_original_data(path, columns)
    y = split_user_id_data(path, columns)

    X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.25)
    # base = baseline(231, 885)
    print(score(baseline, X_test))
