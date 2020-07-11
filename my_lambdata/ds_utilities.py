import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_wine
from pdb import set_trace as breakpoint

def null_check(X):
    
    """
    X is a pandas dataframe
    Function will return sum of null values

    """
    return f'Total Number of Null Values : {X.isnull().sum()}'

def tvt_split(X):
    
    """
    X is a pandas dataframe
    Function splits data into train, validation and test datasets
    with 80-20 split.

    """
    train, test = train_test_split(X, train_size=0.8, test_size=0.2)
    train, val = train_test_split(train, train_size=0.8, test_size=0.2)
    
    return train, test, val

if __name__ == '__main__':
    # y = int(input("Choose a number: "))
    # print(y, enlarge(y))
    # raw_data = load_wine()
    # df = pd.DataFrame(data=raw_data['data'], columns=raw_data['feature_names'])
    # df['target'] = raw_data['target']
    # breakpoint()
    # print(df.shape)
