import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def calculate_interest():
    principal = float(principal_entry.get())
    rate = float(rate_entry.get())
    time = float(time_entry.get())

    if interest_type.get() == "Simple":
        interest = principal * rate * time / 100
        total_amount = principal + interest
    elif interest_type.get() == "Compound":
        total_amount = principal * (1 + rate / 100) ** time
        interest = total_amount - principal
    else:
        messagebox.showerror("Error", "Invalid interest type")
        return

    result_label.config(text=f"Interest: Rs. {interest:.2f}\nTotal Amount: Rs. {total_amount:.2f} \nAmount payable per month: Rs. {total_amount/time:.2f}")

# Create the main window
root = tk.Tk()
root.title("Annual Loan Calculator")

#Entry
principal_label = ttk.Label(root, text="Principal Amount (in Rs.):")
principal_entry = ttk.Entry(root)

#Entry
rate_label = ttk.Label(root, text="Rate of Interest (%):")
rate_entry = ttk.Entry(root)

#Entry
time_label = ttk.Label(root, text="Duration (in years):")
time_entry = ttk.Entry(root)

#Drop down box
interest_type_label = ttk.Label(root, text="Interest Type:")
interest_type = ttk.Combobox(root, values=["Simple", "Compound"])
interest_type.set("Simple")

#Finalize Button
calculate_button = ttk.Button(root, text="Calculate", command=calculate_interest)
result_label = ttk.Label(root, text="Result will be displayed here.")

# Arrange the components in the grid
principal_label.grid(row=0, column=0, padx=10, pady=10, sticky="e")
principal_entry.grid(row=0, column=1, padx=10, pady=10)

rate_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
rate_entry.grid(row=1, column=1, padx=10, pady=10)

time_label.grid(row=2, column=0, padx=10, pady=10, sticky="e")
time_entry.grid(row=2, column=1, padx=10, pady=10)

interest_type_label.grid(row=3, column=0, padx=10, pady=10, sticky="e")
interest_type.grid(row=3, column=1, padx=10, pady=10)

calculate_button.grid(row=4, column=0, columnspan=2, pady=10)

result_label.grid(row=5, column=0, columnspan=2, pady=10)

if __name__ == "__main__":
    root.mainloop()