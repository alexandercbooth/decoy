def make_decoy_data(df1, frac):
    """To use, pass in a dataframe and a fractional sample size and a decoy dataframe will be returned"""
    rowSize, colSize = df1.shape
    import pandas as pd
    import numpy as np
    import random

    #Generate initial zeroed df of appropriate size
    df2 = pd.DataFrame(np.zeros((rowSize, colSize)))
    df2.columns = list(df1.columns)

    #List of column names grouped by type
    ints = list(df1.select_dtypes(include = ['int']).columns)
    floats = list(df1.select_dtypes(include = ['float']).columns)
    obs = list(df1.select_dtypes(include = ['object']).columns)
    dates = list(df1.select_dtypes(include=['datetime64']).columns)
    #types = [ints, floats, obs, dates]

    for i in obs:
        k = xrange(df1[i].nunique())
        df2[i] = df2[i].apply(lambda x: random.choice(k))
        df2[i] = df2[i].astype(object)

    for i in ints:
        df2[i] = np.random.randint(df1[i].max(),size=len(df1))

    for i in dates:
        dmin, dmax = df1[i].min(), df1[i].max()
        dlist = pd.date_range(dmin, dmax)
        df2[i] = df2[i].apply(lambda x: random.choice(dlist))


    for i in floats:
        df2[i] = df1[i].apply(lambda x: x * random.random())


    print 'Done'

    def test_structure():
        assert df1.dtypes == df2.dtypes

    return df2.sample(frac=frac).reset_index(drop=True)
