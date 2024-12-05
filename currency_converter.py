# currency_converter.py
import requests
from datetime import datetime, timedelta

class CurrencyConverter:
    def __init__(self, api_key):
        self.api_key = api_key
        self.rates = {}
        self.last_update = None
        self.update_interval = timedelta(hours=1)
        self.fetch_exchange_rates()

    def fetch_exchange_rates(self):
        current_time = datetime.now()
        
        if (self.last_update is None or 
            current_time - self.last_update > self.update_interval):
            
            url = f"https://v6.exchangerate-api.com/v6/{self.api_key}/latest/USD"
            response = requests.get(url)
            
            if response.status_code == 200:
                data = response.json()
                self.rates = data['conversion_rates']
                self.last_update = current_time
            else:
                raise Exception("Gagal mengambil data kurs mata uang")

    def get_rate(self, from_currency, to_currency):
        """Mendapatkan rate konversi antara dua mata uang"""
        self.fetch_exchange_rates()
        
        if from_currency not in self.rates or to_currency not in self.rates:
            raise Exception("Kode mata uang tidak valid")
            
        # Hitung rate melalui USD
        usd_to_from = self.rates[from_currency]
        usd_to_to = self.rates[to_currency]
        
        return usd_to_to / usd_to_from

    def convert(self, amount, from_currency, to_currency):
        if amount < 0:
            raise ValueError("Jumlah tidak boleh negatif")
            
        if from_currency == to_currency:
            return amount
            
        rate = self.get_rate(from_currency, to_currency)
        return amount * rate