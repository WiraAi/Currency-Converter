# main.py
from ui import CurrencyConverterUI
from currency_converter import CurrencyConverter
import tkinter as tk
from config import API_KEY

def main():
    root = tk.Tk()
    converter = CurrencyConverter(API_KEY)
    app = CurrencyConverterUI(root, converter)
    root.mainloop()

if __name__ == "__main__":
    main()
