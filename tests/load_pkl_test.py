import pickle


def load_top5_data():
    with open('../pkl_files/top_fives.pkl', 'rb') as file:
        data = pickle.load(file)

    print(data)
    print(data.zip_code)


if __name__ == "__main__":
    load_top5_data()
