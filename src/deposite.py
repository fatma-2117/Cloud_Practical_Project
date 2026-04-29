import tkinter as tk
from tkinter import messagebox
from models import Account

def setup_deposit_page(login_screen, update_screen, content_frame, is_logged_in, current_account, operation_screen):
    if not is_logged_in or not current_account:
        messagebox.showwarning("Access Denied", "You must log in first to perform this operation.")
        update_screen(login_screen)
        return

    # Clear previous content in the content frame
    for widget in content_frame.winfo_children():
        widget.destroy()

    # Customize content_frame size and styling
    content_frame.config(width=800, height=400, bg="white")
    content_frame.pack_propagate(False)  # Prevent resizing based on content
    content_frame.grid_propagate(False)  # Prevent resizing in grid layout

    # Add a title
    title_label = tk.Label(
        content_frame,
        text="Deposit Money",
        font=("Helvetica", 30, "bold"),
    )
    title_label.pack(pady=20)

    # Amount label and entry
    amount_label = tk.Label(
        content_frame,
        text="Amount",
        font=("Helvetica", 25),
        anchor="w"
    )
    amount_label.pack()

    amount_entry = tk.Entry(content_frame, font=("Helvetica", 15))
    amount_entry.pack(pady=5)

    # Perform deposit logic
    def perform_deposit():
        try:
            amount = float(amount_entry.get())
            result = Account.deposit(current_account[0], amount)  # Use the backend method
            if "Account not found" in result:
                messagebox.showerror("Deposit", result)
            else:
                messagebox.showinfo("Deposit", result)
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid amount.")

    # Deposit button
    deposit_button = tk.Button(
        content_frame,
        text="Deposit",
        width=15,
        font=("Helvetica", 14, "bold"),
        bg="green",
        fg="white",
        activebackground="darkgreen",
        activeforeground="white",
        command=perform_deposit
    )
    deposit_button.pack(pady=20)

    # Back button
    back_button = tk.Button(
        content_frame,
        text="Back",
        width=15,
        font=("Helvetica", 14, "bold"),
        bg="red",
        fg="white",
        activebackground="darkred",
        activeforeground="white",
        command=lambda: update_screen(operation_screen)
    )
    back_button.pack(pady=13)