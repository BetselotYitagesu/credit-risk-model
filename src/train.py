import pandas as pd
from src.data_processing import preprocess_data, build_pipeline

# Load data
df = pd.read_csv('data/raw/data.csv')

# Preprocess and aggregate
agg_data = preprocess_data(df)

# Define columns
numeric_cols = ['TotalAmount', 'AvgAmount', 'TxnCount', 'StdAmount']
categorical_cols = ['ChannelId', 'ProductCategory']

# Build pipeline
pipeline = build_pipeline(numeric_cols, categorical_cols)

# Fit-transform your features
X = pipeline.fit_transform(agg_data)


