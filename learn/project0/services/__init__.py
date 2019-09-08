import pandas as pd
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))   # refers to application_top
APP_STATIC = os.path.join(APP_ROOT, '../static')


def load_data():
    # This option made "appearing all columns" work. Was showing fewer columns
    pd.set_option('display.expand_frame_repr', False)
    pd.set_option('display.max_rows', 10)
    pd.set_option('display.max_columns', 100)
    in_file = 'titanic_data.csv'
    with open(os.path.join(APP_STATIC, in_file)) as f:
        full_data = pd.read_csv(f)
    return full_data


def separate_truth_from_data(data):
    truth = data['Survived']
    data.drop('Survived', axis=1, inplace=True)
    return truth, data
