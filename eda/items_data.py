import pandas as pd


def load_items_data(path, cols):
    datas = pd.read_csv(path, names=cols, sep="|", encoding="latin-1")
    return datas


def load_movie_url(path, cols):
    datas = pd.read_csv(path, names=cols, sep="|", encoding="latin-1")
    return datas['URL']


def remove_except_movie_title(path, columns):
    movies = pd.read_csv(path, names=columns, sep="|", encoding="latin-1")
    return movies[['movie_id', 'title']]


if __name__ == '__main__':
    folder = '../ml-100k/u.item'
    column = ['movie_id', 'title', 'release date', 'video release date', 'IMDb',
              'URL', 'unknown', 'Action', 'Adventure',
              'Animation', 'Children\'s', 'Comedy', 'Crime', 'Documentary', 'Drama',
              'Fantasy',
              'Film-Noir', 'Horror', 'Musical', 'Mystery', 'Romance', 'Sci-Fi',
              'Thriller', 'War', 'Western']
    print(load_items_data(folder, column))
    print(load_movie_url(folder, column))
    print(remove_except_movie_title(folder, column))
