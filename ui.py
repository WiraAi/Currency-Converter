# ui.py
import streamlit as st
from currency_converter import CurrencyConverter
from currencies import CURRENCY_CODES

class CurrencyConverterUI:
    def __init__(self, converter):
        self.converter = converter
        self.setup_page()
        self.create_ui()
    
    def setup_page(self):
        st.set_page_config(
            page_title="Konverter Mata Uang",
            page_icon="💱",
            layout="centered"
        )
        
        # Custom CSS
        st.markdown("""
        <style>
        .main {
            padding: 2rem;
        }
        .stButton>button {
            width: 100%;
            margin-top: 1rem;
        }
        .result-text {
            font-size: 2rem;
            font-weight: bold;
            text-align: center;
            padding: 1rem;
            color: #2196F3;
        }
        </style>
        """, unsafe_allow_html=True)
    
    def create_ui(self):
        # Header
        st.title("💱 Konverter Mata Uang")
        st.markdown("---")
        
        # Input jumlah
        amount = st.number_input(
            "Masukkan Jumlah",
            min_value=0.0,
            value=1.0,
            step=0.01
        )
        
        # Layout kolom untuk mata uang
        col1, col2 = st.columns(2)
        
        with col1:
            # Mata uang asal
            from_currency = st.selectbox(
                "Dari Mata Uang",
                options=[code.split(' - ')[0] for code in CURRENCY_CODES],
                index=CURRENCY_CODES.index('USD - United States Dollar')
            )
            
        with col2:
            # Mata uang tujuan
            to_currency = st.selectbox(
                "Ke Mata Uang",
                options=[code.split(' - ')[0] for code in CURRENCY_CODES],
                index=CURRENCY_CODES.index('IDR - Indonesian Rupiah')
            )
        
        # Tombol tukar
        if st.button("🔄 Tukar Mata Uang"):
            # Simpan nilai sementara
            temp_from = from_currency
            # Update selectbox (akan trigger rerun)
            st.session_state['from_currency'] = to_currency
            st.session_state['to_currency'] = temp_from
            st.experimental_rerun()
        
        # Tombol konversi
        if st.button("Konversi"):
            try:
                # Lakukan konversi
                result = self.converter.convert(amount, from_currency, to_currency)
                
                # Format hasil
                formatted_result = "{:,.2f}".format(result)
                
                # Tampilkan hasil
                st.markdown("---")
                st.markdown("### Hasil Konversi")
                st.markdown(
                    f"<div class='result-text'>{formatted_result} {to_currency}</div>",
                    unsafe_allow_html=True
                )
                
                # Tampilkan rate
                rate = self.converter.get_rate(from_currency, to_currency)
                st.info(f"Rate: 1 {from_currency} = {rate:.4f} {to_currency}")
                
            except Exception as e:
                st.error(f"Error: {str(e)}")
