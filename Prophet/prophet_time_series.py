# -*- coding: utf-8 -*-
"""Prophet_time_series.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17eloBIg8GpYI-OHdptSb7mwxm5nAR7Ay
"""

# Import libraries
import pandas as pd
import numpy as np
from fbprophet import Prophet
from fbprophet.plot import plot_plotly
import plotly.offline as py
import io
import matplotlib.pyplot as plt
plt.style.use("fivethirtyeight")# for pretty graphs

#Upload training data
from google.colab import files
uploaded    = files.upload()
data        = pd.read_csv(io.BytesIO(uploaded['AirPassengers.csv']))

data.dtypes

plt.figure(figsize=(10,6))
plt.plot(data.set_index('Month'))
plt.legend(['#Passengers'])

data['#Passengers'] = np.log(data['#Passengers'])
plt.figure(figsize=(10,6))
plt.plot(data.set_index('Month'))
plt.legend(['#Passengers'])

data.columns = ['ds','y']
data.head()

m1 = Prophet(yearly_seasonality=True,weekly_seasonality=True,daily_seasonality=True)
m1.fit(data)

future1 = m1.make_future_dataframe(periods=60)
forecast1 = m1.predict(future1)
forecast1.head()

forecast1[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail()

np.exp(forecast1[['yhat', 'yhat_lower', 'yhat_upper']].tail())

m1.plot(forecast1);

m1.plot_components(forecast1);

m3 = Prophet(mcmc_samples=300,weekly_seasonality=True,daily_seasonality=True,yearly_seasonality=True).fit(data)
future3 = m3.make_future_dataframe(periods=60)
forecast3 = m3.predict(future3)
forecast3["Views"] = np.exp(forecast3.yhat).round()
forecast3["Views_lower"] = np.exp(forecast3.yhat_lower).round()
forecast3["Views_upper"] = np.exp(forecast3.yhat_upper).round()
forecast3[(forecast3.ds > "3-22-2019") &
          (forecast3.ds < "4-07-2019")][["ds","Views_lower",
                                        "Views", "Views_upper"]]

m1.plot(forecast3);

m1.plot_components(forecast3);