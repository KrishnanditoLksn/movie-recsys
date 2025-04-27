import pandas as pd


def load_user_data(path, cols):
    users = pd.read_csv(path, names=cols, sep='|', encoding="utf-8")
    users.to_pickle('../pkl_files/users.pkl')
    return users


def get_head_user_datas(path, cols):
    top_five = pd.read_csv(path, names=cols, sep='|', encoding="utf-8")
    top_five.to_pickle('../pkl_files/top_fives.pkl')
    print("TOP 5 DATAS :  ", top_five.head(5))



if __name__ == '__main__':
    path = '../ml-100k/u.user'
    cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
    print(load_user_data(path, cols))
    get_head_user_datas(path, cols)
