#W14A1106AW
#Program to calculate a 5% raise on a salary three times

import tkinter as tk
from tkinter import ttk

class SalaryCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Salary Calculator")
        
        # Create and set up the main frame
        self.frame = ttk.Frame(root, padding="10")
        self.frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Create widgets
        ttk.Label(self.frame, text="Beginning salary:").grid(row=0, column=0, sticky=tk.W)
        self.salary_entry = ttk.Entry(self.frame)
        self.salary_entry.grid(row=0, column=1, padx=5, pady=5)
        
        ttk.Button(self.frame, text="Calculate New Salary", 
                  command=self.calculate_salary).grid(row=1, column=0, columnspan=2, pady=5)
        
        ttk.Label(self.frame, text="New salary:").grid(row=2, column=0, sticky=tk.W)
        self.new_salary_var = tk.StringVar()
        ttk.Label(self.frame, textvariable=self.new_salary_var).grid(row=2, column=1, sticky=tk.W)
        
        ttk.Label(self.frame, text="Change:").grid(row=3, column=0, sticky=tk.W)
        self.change_var = tk.StringVar()
        ttk.Label(self.frame, textvariable=self.change_var).grid(row=3, column=1, sticky=tk.W)

    def calculate_salary(self):
        try:
            initial_salary = float(self.salary_entry.get())
            # Calculate three successive 5% raises
            final_salary = initial_salary * (1.05 ** 3)
            percent_change = ((final_salary - initial_salary) / initial_salary) * 100
            
            # Update display
            self.new_salary_var.set(f"${final_salary:,.2f}")
            self.change_var.set(f"{percent_change:.2f}%")
        except ValueError:
            self.new_salary_var.set("Invalid input")
            self.change_var.set("Error")

def main():
    root = tk.Tk()
    app = SalaryCalculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()