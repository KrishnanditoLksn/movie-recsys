import pandas as pd


def load_movies_rating_data(folder, cols):
    datas = pd.read_csv(folder, names=cols, sep="\t", encoding="latin-1")
    print(datas)


def drop_timestamp_col(folder, cols):
    datas = pd.read_csv(folder, names=cols, sep="\t", encoding="latin-1")
    rate = datas.drop(columns='timestamp', axis=1)
    print(rate)



if __name__ == "__main__":
    columns = ['user_id', 'movie_id', 'rating', 'timestamp']
    path = "../ml-100k/u.data"
    load_movies_rating_data(path, columns)
    drop_timestamp_col(path, columns)
