# main.py
from ui import CurrencyConverterUI
from currency_converter import CurrencyConverter
import streamlit as st

def main():
    # Get API key from Streamlit secrets
    api_key = st.secrets["API_KEY"]
    
    if not api_key:
        st.error("API key tidak ditemukan dalam secrets.")
        return
        
    converter = CurrencyConverter(api_key)
    CurrencyConverterUI(converter)

if __name__ == "__main__":
    main()
