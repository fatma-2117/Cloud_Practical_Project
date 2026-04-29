import tkinter as tk
from tkinter import messagebox
from models import Donation


def donations_screen(login_screen, update_screen, content_frame, is_logged_in, current_account, operation_screen):
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
        text="Make a Donation",
        font=("Helvetica", 30, "bold"),
        fg="black"
    )
    title_label.grid(row=0, column=0, columnspan=2, pady=20)

    # Organization label and dropdown
    org_label = tk.Label(
        content_frame,
        text="Select Organization:",
        font=("Helvetica", 20),
        anchor="w"
    )
    org_label.grid(row=1, column=0, sticky="e", padx=20, pady=10)

    organization_var = tk.StringVar()
    organization_dropdown = tk.OptionMenu(
        content_frame,
        organization_var,
        "Resala", "Baheya", "57357", "الهلال الاحمر المصري", "الاورمان", "مصر الخير", "مرسال"
    )
    organization_dropdown.config(font=("Helvetica", 18))
    organization_dropdown.grid(row=1, column=1, padx=20, pady=10)

    # Donation amount label and entry
    amount_label = tk.Label(
        content_frame,
        text="Donation Amount",
        font=("Helvetica", 20),
        anchor="w"
    )
    amount_label.grid(row=2, column=0, sticky="e", padx=20, pady=10)

    amount_entry = tk.Entry(content_frame, font=("Helvetica", 18), width=10)
    amount_entry.grid(row=2, column=1, padx=20, pady=10)

    # Perform donation logic
    def perform_donation():
        if not organization_var.get():
            messagebox.showerror("Input Error", "Organization is required.")
            return
        
        try:
            amount = float(amount_entry.get())
            if amount <= 0:
                messagebox.showerror("Input Error", "Donation amount must be greater than zero.")
                return
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid amount.")
            return

        success, message = Donation.add_donation(current_account[0], organization_var.get(), amount)
        if success:
            messagebox.showinfo("Donation Successful", message)
            update_screen(operation_screen)  # move to the operation screen
        else:
            messagebox.showerror("Donation Failed", message)

    # Donate button
    donate_button = tk.Button(
        content_frame,
        text="Donate",
        width=15,
        font=("Helvetica", 14, "bold"),
        bg="green",
        fg="white",
        activebackground="darkgreen",
        activeforeground="white",
        command=perform_donation
    )
    donate_button.grid(row=3, column=0, columnspan=2, pady=20)

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
    back_button.grid(row=4, column=0, columnspan=2, pady=10)

    # Add spacing for better layout
    content_frame.grid_rowconfigure(5, weight=1)
    content_frame.grid_columnconfigure(0, weight=1)
    content_frame.grid_columnconfigure(1, weight=1)
