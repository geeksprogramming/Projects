# scripts/data_loader.py

import pandas as pd


def load_economic_data(csv_path):
    """
    Load and clean DSP-style economic data.
    Returns cleaned DataFrame with renamed columns.
    """
    df = pd.read_csv(csv_path)

    df = df.rename(columns={
        'Country': 'country_name',
        'Average_Monthly_Income': 'income_index',
        'Cost_of_Living': 'cost_of_living_index',
        'Region': 'urbanization_score'
    })

    df.dropna(inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df


def split_by_income_tier(df):
    """
    Split economic data into three tiers: low, mid, high
    based on income_index quantiles.
    Returns three separate DataFrames.
    """
    high = df[df['income_index'] >= df['income_index'].quantile(0.66)]
    mid = df[(df['income_index'] < df['income_index'].quantile(0.66)) &
             (df['income_index'] >= df['income_index'].quantile(0.33))]
    low = df[df['income_index'] < df['income_index'].quantile(0.33)]

    return low, mid, high
