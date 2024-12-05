# main.py
from ui import CurrencyConverterUI
from currency_converter import CurrencyConverter
import os
from dotenv import load_dotenv
import streamlit as st

def main():
    # Load environment variables
    load_dotenv()
    
    # Get API key from environment variable
    api_key = os.getenv('API_KEY')
    
    if not api_key:
        st.error("API key tidak ditemukan. Pastikan file .env berisi API_KEY yang valid.")
        return
        
    converter = CurrencyConverter(api_key)
    CurrencyConverterUI(converter)

if __name__ == "__main__":
    main()
