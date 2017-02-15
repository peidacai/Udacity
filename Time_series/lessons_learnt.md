## Time Series lessons learnt

### Characteristics of a time series

1. It is over a continuous time interval.

2. There are sequential measurements across that interval.

3. There is equal spacing between every two consecutive measurements.

4. Each time unit within the time interval has at most one data point.

### Simple forecasting methods:

#### Averaging

Next time period value is the simple average of all past values. The best predictor of what will happen in the next time period is the average of everything that has happened up until now.

#### Moving average

Next time period value is the average of the time series over a defined time period (say 7 days or 30 days).

#### Naive method

Next time period value is the value of the last time period, e.g. today's value is simply equal to yesterday's value.

This method is commonly used when starting a time series. If there is not enough data to create a predictive model, the Naive method can supplement forecasts for the near future.

#### Seaonal Naive method

This method assumes that the magnitude of the seasonal pattern will remain constant.

### Cyclical versus Seasonality

#### Cyclical

Related to business cycles. No fixed period

In general, the average length of the cyclical patterns is longer than the length of the seasonal pattern. The magnitude of the cyclical pattern also tends to change more than that of the seaonal patterns.

Cyclical patterns are much harder to predict compared to seasonality. For example, the decline in stock markets are often sudden and violent

#### Seasonality

Unchanging and associated with some aspect of the calendar (say, annually)

### Time series scenarios

1. No Trend, No-Seasonal
2. No Trend, Seasonal Constant
3. No Trend, Seasonal Increasing

4. Trend-linear, No-Seasonal
5. Trend-linear, Seasonal Constant
6. Trend-linear, Seasonal Increasing

7. Trend-Exponential, No-Seasonal
8. Trend-Exponential, Seasonal Constant
9. Trend-Exponential, Seasonal Increasing

### ETS (Error, Trend, Seasonality) models

1. Simple Exponential Smoothing Method
2. Holt's Linear Trend Method (Double exponential smoothing)
3. Exponential Trend Method
4. Holt-Winters Seasonal Method

### AutoRegressive Integrated Moving Average (ARIMA)

Stationarity: Mean and variance are constant over time.

Check for stationarity. If not stationary, need to perform differencing to make stationary.

Determine autocorrelation (how correlated a time series is with its past values)

Examine the Autocorrelation Function (ACF) plot to determine autocorrelation

Use ACF plot to help determine whether to use AR or MA or both and how many lags we should be using.

Generally, model should be sufficient with either AR or MA term. Models that use both terms are less common.

Once time series stationary (differenced):

Use AR terms:
Lag -1 term has positive autocorrelation: use AR terms;
ACF that decreases more gradually;
PACF that cuts off sharply after a few lags;
PACF drops off at lag -k, it suggests an AR-k model.

Use MA terms:
Lag -1 term has negative autocorrelation: use MA terms;
ACF that cuts off sharply after a few lags;
PACF that decreases more gradually.

Selection process is manual and involves several rounds of differencing, reviewing the plots and comparing models. However, BI tools such as Alteryx can automated this selection process.

#### Partial correlation (PACF)

The correlation between 2 variables controlling for the values of another set of variables.

Inspecting the Partial Autocorrelation function (PACF) will determine how many AR terms to use to explain the autocorrelation pattern in the time series.

A purely AR model forecasts the variable using a combination of past values of the variable. Similar to linear regression, the more AR terms, the more previous periods used in the forecast.

The number of differences required to make the time series stationary determines the "integrated" terms. If it takes 2 differencing to make series stationary, then the ARIMA model requires 2 "I" terms.

### Testing the model

#### Hold-out samples (Test set)

Ideally, size of the test set should be at least the number of periods which we are forecasting for. I.e. if we are forecasting next 1 year of monthly sales, the test set should be at least the latest 12 month sales.