"""
Data processing module for feature engineering in credit risk modeling.
"""

import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer


class TransactionAggregator(BaseEstimator, TransformerMixin):
    """
    Transaction Aggregato
    """

    def fit(self, x, y=None):
        return self

    def transform(self, x):
        agg_df = x.groupby('CustomerId').agg({
            'Amount': ['sum', 'mean', 'count', 'std'],
            'Value': ['sum', 'mean', 'std']
            }).reset_index()
        agg_df.columns = [
            'CustomerId', 
            'TotalAmount', 'AvgAmount', 'TxnCount', 'StdAmount',
            'TotalValue', 'AvgValue', 'StdValue'
        ]
        return agg_df


class DatetimeFeatureExtractor(BaseEstimator, TransformerMixin):
    def __init__(self, datetime_col='TransactionStartTime'):
        self.datetime_col = datetime_col

    def fit(self, X, y=None):
        return self

    def transform(self, X):
        X = X.copy()
        X[self.datetime_col] = pd.to_datetime(X[self.datetime_col])
        X['TransactionHour'] = X[self.datetime_col].dt.hour
        X['TransactionDay'] = X[self.datetime_col].dt.day
        X['TransactionMonth'] = X[self.datetime_col].dt.month
        X['TransactionYear'] = X[self.datetime_col].dt.year
        return X.drop(columns=[self.datetime_col])


def build_pipeline(numeric_cols, categorical_cols):
    num_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='median')),
        ('scaler', StandardScaler())
    ])

    cat_pipeline = Pipeline([
        ('imputer', SimpleImputer(strategy='most_frequent')),
        ('encoder', OneHotEncoder(handle_unknown='ignore'))
    ])

    full_pipeline = ColumnTransformer([
        ('num', num_pipeline, numeric_cols),
        ('cat', cat_pipeline, categorical_cols)
    ])

    return full_pipeline


def preprocess_data(raw_data):
    """Step 1: Extract temporal features"""
    dt_processor = DatetimeFeatureExtractor()
    data_with_time = dt_processor.fit_transform(raw_data)

    # Step 2: Aggregate customer-level behavior
    aggregator = TransactionAggregator()
    agg_data = aggregator.fit_transform(data_with_time)

    return agg_data
