import pandas as pd


def load_data():
    # This option made "appearing all columns" work. Was showing fewer columns
    pd.set_option('display.expand_frame_repr', False)
    pd.set_option('display.max_rows', 10)
    pd.set_option('display.max_columns', 100)
    in_file = 'titanic_data.csv'
    full_data = pd.read_csv(in_file)
    return full_data


def separate_truth_from_data(data):
    truth = data['Survived']
    data.drop('Survived', axis=1, inplace=True)
    return truth, data
