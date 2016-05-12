# DECOY
Have proprietary data and want to still run tests on a continuous integration platform? Decoy fabricates your data's structure and returns a pandas dataframe with random data in the same structure

```
In [1]: from decoy import make_decoy_data

In [2]: from sklearn.datasets import load_iris

In [3]: import pandas as pd

In [4]: iris = load_iris()

In [5]: train = pd.DataFrame(iris.data)

In [6]: train['target'] = iris.target

In [7]: df = make_decoy_data(train, .5)
In [8]: train.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 150 entries, 0 to 149
Data columns (total 5 columns):
0         150 non-null float64
1         150 non-null float64
2         150 non-null float64
3         150 non-null float64
target    150 non-null int64
dtypes: float64(4), int64(1)
memory usage: 5.9 KB

In [9]: df.info()
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 75 entries, 0 to 74
Data columns (total 5 columns):
0         75 non-null float64
1         75 non-null float64
2         75 non-null float64
3         75 non-null float64
4         75 non-null int64
dtypes: float64(4), int64(1)
memory usage: 3.0 KB
```
## Install from github
```
pip install git+https://github.com/alexandercbooth/decoy.git
```
