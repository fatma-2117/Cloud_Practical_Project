import tkinter as tk
from tkinter import messagebox
from models import Account


def setup_withdraw_page(login_screen, update_screen, content_frame, is_logged_in, current_account, operation_screen):

    if not is_logged_in or not current_account:
        messagebox.showwarning("Access Denied", "You must log in first to perform this operation.")
        update_screen(login_screen)
        return
 
    for widget in content_frame.winfo_children():
        widget.destroy()
    
    content_frame.config(width=800, height=400, bg="white")
    content_frame.pack_propagate(False)  # Prevent resizing based on content
    content_frame.grid_propagate(False)  # Prevent resizing in grid layout

    # إعداد صفحة السحب
    tk.Label(content_frame, text="Withdraw Money", font=("Helvetica", 30 , "bold")).pack(pady=20)

    # إضافة باقي العناصر كما هو

    tk.Label(content_frame, text="Amount", font=("Helvetica", 25)).pack()
    amount_entry = tk.Entry(content_frame, font=("Helvetica", 15))
    amount_entry.pack(pady=5)

    def perform_withdraw():
        try:
            amount = float(amount_entry.get())
            result = Account.withdraw(current_account[0], amount)  # Use the backend method
            if "Account not found" in result:
                messagebox.showerror("Withdraw", result)
            elif "not available" in result:
                messagebox.showerror("Withdraw", result)
            else:
                messagebox.showinfo("Withdraw", result)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter valid account ID and amount.")


    tk.Button(content_frame,
        text="Withdraw",
        width=15,
        font=("Helvetica", 14, "bold"),
        bg="green",
        fg="white",
        activebackground="darkgreen",
        activeforeground="white",
        command=perform_withdraw
        ).pack(pady=20)
    
    tk.Button(content_frame, text="Back",
        width=15,
        font=("Helvetica", 14, "bold"),
        bg="red",
        fg="white",
        activebackground="darkred",
        activeforeground="white",
        command=lambda: update_screen(operation_screen)
        ).pack(pady=13)