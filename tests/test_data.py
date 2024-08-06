import unittest
import pandas as pd

class TestData(unittest.TestCase):

    def setUp(self):
        self.train_df = pd.read_csv('data/raw/train.csv')

    def test_columns_exist(self):
        required_columns = ['Id', 'MSSubClass', 'MSZoning', 'LotFrontage', 'LotArea']
        for column in required_columns:
            self.assertIn(column, self.train_df.columns, f'{column} is missing from the dataset')

    def test_no_missing_values_after_cleaning(self):
        clean_df = pd.read_csv('data/processed/train_clean.csv')
        missing_values = clean_df.isnull().sum().sum()
        self.assertEqual(missing_values, 0, 'Cleaned dataset contains missing values')

if __name__ == '__main__':
    unittest.main()
