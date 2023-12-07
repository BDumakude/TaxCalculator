import tkinter as tk
from tkinter import messagebox
import locale
import ttkbootstrap

def calculate_tax():
    if "R" in income_entry.get():
        gross = income_entry.get()[1:] 
    else: 
        gross = income_entry.get()

    num_gross = gross.replace(" ", "")
    try:
        float(num_gross)
    except ValueError:
        messagebox.showerror("Error", "Please enter a number.")             # check in entry is convertible to float 
    num = float(num_gross)
    if num < 0:                                                             # calculate the tax for each tax bracket
        messagebox.showerror("Error", "You cannot make negative income.")   # account for entry of negative values
    elif num <= 273100:
        tax = 0.18*num
    elif num <= 370500:
        tax = 42678 + 0.26*(num - 273100)
    elif num <= 512800: 
        tax = 77362 + 0.31*(num - 370500)
    elif num <= 673000: 
        tax = 121475 + 0.36*(num - 512800)
    elif num <= 857900: 
        tax = 179147 + 0.39*(num - 673000)
    elif num <= 1817000: 
        tax = 251258 + 0.41*(num - 857900)
    else:
        tax = 644489 + 0.45*(num - 1817000)
    
    rounded_tax = round(tax, 2)   
    income = round(num - tax, 2)
    monthly_income = round(income/12, 2)

    lc_rounded_tax = locale.currency(rounded_tax, grouping=True)   # convert tax, income, monthly income to local currency formats
    lc_income = locale.currency(income, grouping=True)
    lc_monthly_income = locale.currency(monthly_income, grouping=True)

    tax_amount_label_output.configure(text=f"{lc_rounded_tax}")    # reconfigure output labels
    net_annual_income_output.configure(text=f"{lc_income}")
    net_monthly_income_output.configure(text=f"{lc_monthly_income}")

# initialise the window
root = ttkbootstrap.Window(themename="solar")
root.title("Tax Calculator - South Africa")
root.geometry("600x500")

# create entry widget
income_entry = ttkbootstrap.Entry(root, font="Helvetica, 18")
income_entry.insert(0, "R ")
income_entry.grid(row=0, column=1, pady=20)

# create income label
income_label = tk.Label(root, text="Income:", fg="white", font=("TkMenuFont", 14))
income_label.grid(row=0, column=0, padx=20)

# create calculate button
calculate_button = ttkbootstrap.Button(root, text="Calculate Tax", command=calculate_tax, bootstyle="warning")
calculate_button.grid(row=1, column=1, pady=10)

# create tax amount label 
tax_amount_label = tk.Label(root, text="Income Tax: ", fg="white", font=("TkMenyFont", 14))
tax_amount_label.grid(row=3, pady=10, padx=10)

# create annual income amount label
net_annual_income = tk.Label(root, text="Net Income \n (Annnual): ", fg="white", font=("TkMenyFont", 14))
net_annual_income.grid(row=4, pady=10, padx=10)

# create monthly income amount label
net_monthly_income = tk.Label(root, text="Net Income \n (Monthly): ", fg="white", font=("TkMenyFont", 14))
net_monthly_income.grid(row=5, pady=10, padx=10)

# create output label for tax amount
tax_amount_label_output = tk.Label(root, text="", fg="white", font=("TkMenuFont", 14))
tax_amount_label_output.grid(row=3, column=1, padx=10)

# create output label for net annual income
net_annual_income_output = tk.Label(root, text="", fg="white", font=("TkMenuFont", 14))
net_annual_income_output.grid(row=4, column=1, padx=10)

# create output label for net monthly income
net_monthly_income_output = tk.Label(root, text="", fg="white", font=("TkMenuFont", 14))
net_monthly_income_output.grid(row=5, column= 1, padx=10)

root.mainloop()