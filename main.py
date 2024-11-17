import streamlit as st
import requests
from pandas.core.common import not_none

response=requests.get('https://api.coinlore.net/api/tickers/')
veri=response.json()
coinler=veri.get("data")
liste=[coin.get("name")for coin in  coinler]
selected = st.selectbox('Kripto para seçiniz', liste)

seleceted_coin=None
for coin in coinler:
        if coin.get("name")==selected:
                selected_coin=coin
                break
if selected_coin:
        fiyat=selected_coin.get("price_usd")
        st.write(fiyat)
