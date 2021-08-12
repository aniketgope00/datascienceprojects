#!/usr/bin/env python
# coding: utf-8

# In[1]:


import yfinance as yf
import streamlit as st
import pandas as pd


# In[2]:


st.write("""
# Stock Price App

Showing closing price and volume

""")


# In[3]:


tickersymbol = "AAPL"
tickerdata = yf.Ticker(tickersymbol)
tickerdf = tickerdata.history(period = "1d", start = "2015-1-1", end="2021-12-8")


# In[4]:


# Open High Low Close Volume Dividends Stock Splits


# In[5]:


st.line_chart(tickerdf.Close)
st.line_chart(tickerdf.Volume)


# In[ ]:




