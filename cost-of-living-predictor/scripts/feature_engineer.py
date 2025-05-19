# scripts/feature_engineer.py

import pandas as pd
from sklearn.preprocessing import LabelEncoder

def encode_features(df, region_col='urbanization_score', vision_col='vision_category'):
    le_region = LabelEncoder()
    le_vision = LabelEncoder()

    df['urbanization_code'] = le_region.fit_transform(df[region_col])
    df['vision_code'] = le_vision.fit_transform(df[vision_col])

    return df, le_region, le_vision

def add_engineered_features(df):
    df['cost_to_income'] = df['cost_of_living_index'] / df['income_index']
    df['region_income_mean'] = df.groupby('urbanization_code')['income_index'].transform('mean')
    df['income_rolling'] = df['income_index'].rolling(window=5, min_periods=1).mean()
    df['cost_lag1'] = df['cost_of_living_index'].shift(1).bfill()
    df.reset_index(drop=True, inplace=True)
    return df