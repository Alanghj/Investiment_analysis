from alpha_vantage.timeseries import TimeSeries
# import pandas as pd
import matplotlib.pyplot as plt

api_key = '4TIM3MR1B7Q7Z731'

app = TimeSeries(api_key, output_format='pandas')
data_value, information_value = app.get_daily_adjusted(symbol='MSFT', outputsize='compact')

print(data_value)

data_value.to_excel('data-base/values.xlsx')
print(data_value['6. volume'])

data_value['4. close'].plot(figsize = (20, 14))
plt.show()