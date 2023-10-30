import streamlit as st
import yfinance as yf

'''
# Financi App 
'''
# Get the list of the 10 most traded stocks in the world
most_traded_stocks = [
    {
        "ticker": "AAPL",
        "name": "Apple"
    },
    {
        "ticker": "MSFT",
        "name": "Microsoft"
    },
    {
        "ticker": "GOOGL",
        "name": "Alphabet"
    },
    {
        "ticker": "AMZN",
        "name": "Amazon"
    },
    {
        "ticker": "TSLA",
        "name": "Tesla"
    },
    {
        "ticker": "BAC",
        "name": "Bank of America"
    },
    {
        "ticker": "JNJ",
        "name": "Johnson & Johnson"
    },
    {
        "ticker": "WMT",
        "name": "Walmart"
    },
    {
        "ticker": "GOOG",
        "name": "Google"
    },
    {
        "ticker": "META",
        "name": "Facebook"
    }
]
applications = st.text_input("you want to see The 10 most traded stocks in the world type yes", key="app")
if applications=='yes':
    st.write(most_traded_stocks)
elif applications:
    st.write('Your lose 😉')
# Download the historical price data for the stock symbol 'AAPL'
ticker = st.text_input("Enter financial app you want:", key="symbol")
if ticker:
    st.title(ticker)
    ts = yf.Ticker(ticker.upper())
    tDf = ts.history(period='50y')
    # Get the historical price data for the past 10 years


    # Print the historical price data
    st.line_chart(tDf.Close)
    st.line_chart(tDf.Volume)
