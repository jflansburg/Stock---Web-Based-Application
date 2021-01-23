import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import yfinance as yf

st.title('S&P 500 App')

st.markdown("""
This app retrieves the list of the **S&P 500** (from Wikipedia) and its corresponding data while allowing the user to update the ticker, dates, and interval!
* **Python libraries:** pandas, streamlit, numpy, matplotlib, seaborn
* **Data source:** [Wikipedia](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies).
""")

st.sidebar.header('User Input Features')

# Web scraping of S&P 500 data
#

def load_data():
    url = 'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies'
    html = pd.read_html(url, header = 0)
    df = html[0]
    return df

df = load_data()
df.drop(['SEC filings','Headquarters Location','CIK'], axis=1, inplace=True)
df.rename(columns={'Symbol':'Ticker', 
                   'Security':'Company',
                   'GICS Sector':'Sector',
                  'GICS Sub-Industry':'Sub-Sector',
                  'Date first added':'Date Added to Index'}, inplace=True)

# Sidebar - Sector selection
select_ticker = st.sidebar.text_input("Insert the ticker here", 'MMM')
select_start = st.sidebar.date_input('Insert a start date')
select_end = st.sidebar.date_input('Insert an end date')
select_interval = st.sidebar.radio("Select the interval", options =('5m','30m','60m','1d','5d','1wk','1mo'))
# Filtering data

st.header('Display of Companies in S&P500')
pd.set_option("display.max_rows", None, "display.max_columns", None)
st.dataframe(df)

# Download S&P500 data
# https://discuss.streamlit.io/t/how-to-download-file-in-streamlit/1806
#def filedownload(df):
    #csv = df.to_csv(index=False)
    #b64 = base64.b64encode(csv.encode()).decode()  # strings <-> bytes conversions
    #href = f'<a href="data:file/csv;base64,{b64}" download="SP500.csv">Download CSV File</a>'
    #return href

#st.markdown(filedownload(sector), unsafe_allow_html=True)/#

# https://pypi.org/project/yfinance/

data = yf.download(
        tickers = (select_ticker),
        start = select_start,
        end = select_end,
        interval = select_interval,
        group_by = 'ticker',
        auto_adjust = True,
        prepost = True,
        threads = True,
        proxy = None
    )

# Plot Closing Price of Query Symbol
def close_plot():
  df = pd.DataFrame(data.Close)
  df['Date'] = df.index
  #plt.fill_between(df.Date, df.Close, color='skyblue', alpha=0.3)
  plt.plot(df.Date, df.Close, color='skyblue', alpha=0.8)
  plt.xticks(rotation=90)
  plt.title(select_ticker, fontweight='bold')
  plt.xlabel('Date', fontweight='bold')
  plt.ylabel('Closing Price', fontweight='bold')
  return st.pyplot()

def volume_plot():
  df1 = pd.DataFrame(data.Volume)
  df1['Date'] = df1.index
  plt.plot(df1.Date, df1.Volume, color = 'red')
  plt.xticks(rotation=90)
  plt.title(select_ticker, fontweight='bold')
  plt.xlabel('Date', fontweight='bold')
  plt.ylabel('Volume', fontweight='bold')
  return st.pyplot()


if st.button('Show Plots'):
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.header('Stock Closing Price')
    close_plot()
    st.header('Stock Volume')
    volume_plot()
