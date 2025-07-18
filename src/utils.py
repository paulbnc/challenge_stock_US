from pandas import read_csv, DataFrame
import os
from typing import Tuple, Optional

ROOT_DIR = os.path.dirname(os.getcwd())

def load_data() -> Optional[Tuple[DataFrame, DataFrame]]:
    '''Return Tuple(DataFrame of features, DataFrame of target), or None if files are missing'''
    x_path = os.path.join(ROOT_DIR, 'dataset', 'X.csv')
    y_path = os.path.join(ROOT_DIR, 'dataset', 'y.csv')
    
    try:
        x_df = read_csv(x_path)
        y_df = read_csv(y_path)
        return x_df, y_df
    except FileNotFoundError:
        print(f'Files not found. Expected at:\n- {x_path}\n- {y_path}')
    except Exception as e:
        print(f'An error occurred while loading data: {e}')
    return None
