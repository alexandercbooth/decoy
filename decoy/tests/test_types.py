import sys, os
sys.path.insert(0,'../..')
from sklearn.datasets import load_iris
import pandas as pd

from decoy import make_decoy_data

iris = load_iris()

train = pd.DataFrame(iris.data)
train['target'] = iris.target

df = make_decoy_data(train, .5)
def test_dtypes():
    for i in train.columns:
        assert train[i].dtypes == df[i].dtypes
