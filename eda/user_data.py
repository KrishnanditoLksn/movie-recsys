import pandas as pd


def load_user_data():
    user_cols = ['user_id', 'age', 'sex', 'occupation', 'zip_code']
    users = pd.read_csv('../ml-100k/u.user', sep='|', names=user_cols, encoding='latin-1')
    return users