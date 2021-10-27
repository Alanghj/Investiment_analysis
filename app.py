from alpha_vantage.timeseries import TimeSeries
import plotly.express as px
import pandas as pd
import json

with open('key/api_key.json') as f:
    data = json.load(f)
keys = data['key']

stocks_value = ['FB', 'AAPL', 'AMZN', 'NFLX', 'GOOGL'] #FAANG
app = TimeSeries(keys, output_format='pandas')

for stocks in stocks_value:
    data_value, information_value = app.get_daily_adjusted(symbol=stocks, outputsize='full')
    if stocks in stocks_value[0]:
        data_value.to_excel('data-base/values_fb.xlsx')
    elif stocks in stocks_value[1]:
        data_value.to_excel('data-base/values_aapl.xlsx')
    elif stocks in stocks_value[2]:
        data_value.to_excel('data-base/values_amzn.xlsx')
    elif stocks in stocks_value[3]:
        data_value.to_excel('data-base/values_nflx.xlsx')
    elif stocks in stocks_value[4]:
        data_value.to_excel('data-base/values_googl.xlsx')

df = pd.read_excel("data-base/values_fb.xlsx")
table_fb = df[['1. open', '2. high', '3. low', '4. close', '6. volume']]
fig_fb = px.line(table_fb)
fig_fb.update_layout(
    title="Stock FB(Facebook)",
    xaxis_title="Daily",
    yaxis_title="Values",
    legend_title="Variables",
    font=dict(
        family="Roboto, monospace",
        size=18,
        color="#000000"
    )
)
fig_fb.show()


df = pd.read_excel("data-base/values_aapl.xlsx")
table_aapl = df[['1. open', '2. high', '3. low', '4. close', '6. volume']]
fig_aapl = px.line(table_aapl)
fig_aapl.update_layout(
    title="Stock AAPL(Apple)",
    xaxis_title="Daily",
    yaxis_title="Values",
    legend_title="Variables",
    font=dict(
        family="Roboto, monospace",
        size=18,
        color="#000000"
    )
)
fig_aapl.show()

df = pd.read_excel("data-base/values_amzn.xlsx")
table_amzn = df[['1. open', '2. high', '3. low', '4. close', '6. volume']]
fig_amzn = px.line(table_amzn)
fig_amzn.update_layout(
    title="Stock AMZN(Amazon)",
    xaxis_title="Daily",
    yaxis_title="Values",
    legend_title="Variables",
    font=dict(
        family="Roboto, monospace",
        size=18,
        color="#000000"
    )
)
fig_amzn.show()

df = pd.read_excel("data-base/values_nflx.xlsx")
table_nflx = df[['1. open', '2. high', '3. low', '4. close', '6. volume']]
fig_nflx = px.line(table_nflx)
fig_nflx.update_layout(
    title="Stock NFLX(Netflix)",
    xaxis_title="Daily",
    yaxis_title="Values",
    legend_title="Variables",
    font=dict(
        family="Roboto, monospace",
        size=18,
        color="#000000"
    )
)
fig_nflx.show()

df = pd.read_excel("data-base/values_googl.xlsx")
table_googl = df[['1. open', '2. high', '3. low', '4. close', '6. volume']]
fig_googl = px.line(table_googl)
fig_googl.update_layout(
    title="Stock GOOGL(Google)",
    xaxis_title="Daily",
    yaxis_title="Values",
    legend_title="Variables",
    font=dict(
        family="Roboto, monospace",
        size=18,
        color="#000000"
    )
)
fig_googl.show()