from pandas import read_csv, DataFrame

def load_data() -> Tuple(DataFrame, DataFrame):
    '''return Tuple(Dataframe of features, Dataframe of target)'''
    return read_csv(r'/dataset/X.csv')