import streamlit as st
import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
#Simple Stocl Price App

Shown are the stock closing price and volume of Google

""")

# https://towardsdatascience.com/hơ-to-get-stock-data-using-python-code1df17e75
#define the ticker symbol
tickerSymbol = "GOOGL"
#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)
#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-5-13', end='2020-5-31')
#open high low close volume dividends stock splits
st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)

