
# What makes Time Series Special

As the name suggests, TS is a collection of data points collected at constant time intervals. These are analyzed to determine the long term trend so as to forecast the future or perform some other form of analysis.  

![Alt text](time_series.jpeg?raw=true "Time Series")


But what makes a TS different from say a regular regression problem? There are 2 things:

* It is time dependent. So the basic assumption of a linear regression model that the observations are independent doesn’t hold in this case.      
* Along with an increasing or decreasing trend, most TS have some form of seasonality trends, i.e. variations specific to a particular time frame. For example, if you see the sales of a woolen jacket over time, you will invariably find higher sales in winter seasons.  

## Check Stationarity of a Time Series

Stationarity is defined using very strict criterion. However, for practical purposes we can assume the series to be stationary if it has constant statistical properties over time, ie. the following:  
* Constant mean  
* Constant variance  
* An autocovariance that does not depend on time.  

**Dickey-Fuller Test**: This is one of the statistical tests for checking stationarity. Here the null hypothesis is that the TS is non-stationary. The test results comprise of a Test Statistic and some Critical Values for difference confidence levels. If the ‘Test Statistic’ is less than the ‘Critical Value’, we can reject the null hypothesis and say that the series is stationary.  

## Make a Time Series Stationary  

Though stationarity assumption is taken in many TS models, almost none of practical time series are stationary. So statisticians have figured out ways to make series stationary  

Lets understand what is making a TS non-stationary. There are 2 major reasons behind non-stationaruty of a TS:  

* **Trend** – varying mean over time. For eg, in this case we saw that on average, the number of passengers was growing over time.  

* **Seasonality** – variations at specific time-frames. eg people might have a tendency to buy cars in a particular month because of pay increment or festivals.  

The underlying principle is to model or estimate the trend and seasonality in the series and remove those from the series to get a stationary series. Then statistical forecasting techniques can be implemented on this series. The final step would be to convert the forecasted values into the original scale by applying trend and seasonality constraints back.  

## Libraries used  

In this repo I am exploring time series using different libraries.They are,  

1 - Time series fundamentals using statesmodels  
2 - Prophet  
3 - Dart  
4 - Sktime 

