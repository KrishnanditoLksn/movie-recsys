import pandas as pd


def load_user_data(path, cols):
    users = pd.read_csv(path, names=cols, sep='|', encoding="utf-8")
    return users


def get_head_user_datas(path, cols):
    top_five = pd.read_csv(path, names=cols, sep='|', encoding="utf-8")
    print("TOP 5 DATAS :  ", top_five.head(5))

