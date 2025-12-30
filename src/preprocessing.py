import numpy as np
import pandas as pd

def compute_log_returns(df, price_col="Close"):
    returns = np.log(df[price_col]).diff()
    return returns.dropna()

def rolling_volatility(returns, window=30):
    return returns.rolling(window).std()
