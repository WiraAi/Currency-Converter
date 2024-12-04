# ui.py
import tkinter as tk
from tkinter import ttk, messagebox
from currency_converter import CurrencyConverter
from currencies import CURRENCY_CODES

class CurrencyConverterUI:
    def __init__(self, root, converter):
        self.converter = converter
        self.root = root
        self.root.title("Konverter Mata Uang")
        self.root.geometry("400x500")
        self.root.configure(bg="#f0f0f0")
        
        # Buat frame utama
        self.main_frame = tk.Frame(self.root, bg="#f0f0f0", padx=20, pady=20)
        self.main_frame.pack(expand=True, fill="both")
        
        self.create_widgets()
        
    def create_widgets(self):
        # Judul
        title_label = tk.Label(
            self.main_frame, 
            text="Konverter Mata Uang",
            font=("Helvetica", 16, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        title_label.pack(pady=(0, 20))

        # Frame untuk input
        input_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        input_frame.pack(fill="x", pady=5)

        # Amount input dengan styling
        amount_frame = tk.Frame(input_frame, bg="#f0f0f0")
        amount_frame.pack(fill="x", pady=5)
        
        tk.Label(
            amount_frame,
            text="Jumlah:",
            font=("Helvetica", 10),
            bg="#f0f0f0"
        ).pack(side="left")
        
        self.amount_entry = tk.Entry(
            amount_frame,
            font=("Helvetica", 12),
            width=20,
            relief="solid"
        )
        self.amount_entry.pack(side="right", ipady=3)

        # Currency selection frames
        currency_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        currency_frame.pack(fill="x", pady=10)

        # From currency
        from_frame = tk.Frame(currency_frame, bg="#f0f0f0")
        from_frame.pack(fill="x", pady=5)
        
        tk.Label(
            from_frame,
            text="Dari Mata Uang:",
            font=("Helvetica", 10),
            bg="#f0f0f0"
        ).pack(side="left")
        
        self.from_currency_combobox = ttk.Combobox(
            from_frame,
            values=[code.split(' - ')[0] for code in CURRENCY_CODES],
            width=15,
            font=("Helvetica", 10)
        )
        self.from_currency_combobox.pack(side="right")
        self.from_currency_combobox.set('USD')

        # To currency
        to_frame = tk.Frame(currency_frame, bg="#f0f0f0")
        to_frame.pack(fill="x", pady=5)
        
        tk.Label(
            to_frame,
            text="Ke Mata Uang:",
            font=("Helvetica", 10),
            bg="#f0f0f0"
        ).pack(side="left")
        
        self.to_currency_combobox = ttk.Combobox(
            to_frame,
            values=[code.split(' - ')[0] for code in CURRENCY_CODES],
            width=15,
            font=("Helvetica", 10)
        )
        self.to_currency_combobox.pack(side="right")
        self.to_currency_combobox.set('IDR')

        # Swap button
        self.swap_button = tk.Button(
            self.main_frame,
            text="⇅ Tukar",
            command=self.swap_currencies,
            bg="#4CAF50",
            fg="white",
            font=("Helvetica", 10),
            relief="flat",
            cursor="hand2"
        )
        self.swap_button.pack(pady=10)

        # Convert button
        self.convert_button = tk.Button(
            self.main_frame,
            text="Konversi",
            command=self.convert,
            bg="#2196F3",
            fg="white",
            font=("Helvetica", 12, "bold"),
            width=20,
            relief="flat",
            cursor="hand2"
        )
        self.convert_button.pack(pady=20)

        # Result frame
        result_frame = tk.Frame(self.main_frame, bg="#f0f0f0")
        result_frame.pack(fill="x", pady=10)
        
        tk.Label(
            result_frame,
            text="Hasil Konversi:",
            font=("Helvetica", 10),
            bg="#f0f0f0"
        ).pack()
        
        self.result_label = tk.Label(
            result_frame,
            text="0.00",
            font=("Helvetica", 24, "bold"),
            bg="#f0f0f0",
            fg="#333333"
        )
        self.result_label.pack(pady=10)

    def swap_currencies(self):
        from_currency = self.from_currency_combobox.get()
        to_currency = self.to_currency_combobox.get()
        self.from_currency_combobox.set(to_currency)
        self.to_currency_combobox.set(from_currency)
        if self.amount_entry.get():
            self.convert()

    def convert(self):
        try:
            amount = float(self.amount_entry.get())
            from_currency_code = self.from_currency_combobox.get()
            to_currency_code = self.to_currency_combobox.get()
            
            result = self.converter.convert(amount, from_currency_code, to_currency_code)
            
            # Format hasil dengan pemisah ribuan
            formatted_result = "{:,.2f}".format(result)
            self.result_label.config(
                text=f"{formatted_result} {to_currency_code}",
                fg="#333333"
            )
            
        except ValueError:
            messagebox.showerror("Error", "Mohon masukkan angka yang valid")
            self.result_label.config(text="0.00", fg="red")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.result_label.config(text="0.00", fg="red")

if __name__ == "__main__":
    root = tk.Tk()
    
    # api key dan inisialisasi api
    api_key = '5f294d649649042f56702e66'
    converter = CurrencyConverter(api_key)
    app = CurrencyConverterUI(root, converter)
    root.mainloop()
