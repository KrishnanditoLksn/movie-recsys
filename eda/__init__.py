from eda.user_data import load_user_data, get_head_user_datas

if __name__ == '__main__':
    path = '../ml-100k/u.user'
    cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
    print(load_user_data(path, cols))
    get_head_user_datas(path, cols)
