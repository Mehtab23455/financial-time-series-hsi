# Empirical Results

## Results and Findings

This study analyzes the volatility characteristics of the Hang Seng Index (HSI)
using both classical econometric models and machine learning baselines. The goal
is to evaluate volatility dynamics and compare traditional GARCH models with
data-driven forecasting approaches.

---

## Price and Return Behavior

The Hang Seng Index price series exhibits strong non-stationarity and long-term
trends. After transforming prices into daily log returns, the return series
fluctuates around a zero mean with no persistent trend, indicating stationarity.
This transformation is standard in financial econometrics and enables valid
statistical inference.

---

## Volatility Clustering

Visual inspection of the return series and rolling volatility reveals pronounced
volatility clustering. Periods of high volatility tend to be followed by further
high-volatility periods, while tranquil periods persist over time. This behavior
is inconsistent with constant-variance assumptions and motivates conditional
volatility modeling.

---

## ARCH Effects

Formal ARCH-LM tests strongly reject the null hypothesis of homoskedasticity.
The extremely small p-values provide statistical evidence of conditional
heteroskedasticity in HSI returns, confirming the presence of time-varying
volatility.

---

## GARCH Model Estimation

A GARCH(1,1) model is estimated to capture volatility dynamics. All parameters
are positive and statistically significant. The estimated persistence parameter
(α + β) is close to unity, indicating that volatility shocks decay slowly over
time.

The conditional volatility series produced by the GARCH model aligns closely
with observed periods of market stress, suggesting that the model adequately
captures the temporal structure of volatility in the HSI.

---

## Machine Learning Baseline Comparison

To complement the econometric analysis, machine learning models are implemented
as alternative volatility forecasting baselines. Lagged squared returns and
historical volatility measures are used as input features, with next-period
realized volatility proxied by squared returns.

An XGBoost regression model is trained using a rolling-window, out-of-sample
framework to prevent look-ahead bias. Forecast accuracy is evaluated using mean
squared error (MSE) and compared against GARCH-based volatility forecasts.

The results indicate that XGBoost captures short-term nonlinear patterns in
volatility and performs competitively with the GARCH(1,1) model in
out-of-sample forecasting. However, performance gains are not consistently
large across all periods, particularly during extreme market stress.

These findings highlight the bias–variance tradeoff in financial time series
forecasting. While machine learning models offer greater flexibility, they are
more susceptible to overfitting noisy financial data. In contrast, GARCH models
provide stable and interpretable volatility forecasts with strong persistence
properties.

---

## Summary of Empirical Findings

Overall, both econometric and machine learning approaches confirm the presence
of strong volatility clustering and persistence in the Hang Seng Index. Machine
learning methods provide useful complementary insights but do not uniformly
dominate traditional GARCH models, underscoring the continued relevance of
classical volatility modeling in financial applications.