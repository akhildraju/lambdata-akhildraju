import pandas as pd
from sklearn.model_selection import train_test_split


class DatasetUtil:

  dataframe = None

  def __init__(self, df):
    self.dataframe = df

  def train_test_validate_split(self, test_size=0.25, random_state=42):

    if test_size > 0.25:
      test_size = 0.25

    totalrows = len(df)
    test_rows = totalrows * test_size
    remaining_rows = totalrows - test_rows
    val_size = test_rows/remaining_rows

    train, test = train_test_split(self.dataframe, test_size=test_size,
                                   random_state=random_state)
    train, validate = train_test_split(train,
                                       test_size=val_size,
                                       random_state=random_state)

    return train, test, validate

if __name__ == "__main__":

  df = pd.read_csv("http://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data")
  du = DatasetUtil(df)

  tn, tt, v = du.train_test_validate_split(test_size=0.25,
                                           random_state=42)

  print('Test Size=', len(tt))
  print('Validate Size=', len(v))
  print('Train Size=', len(tn))
