import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import messagebox
from number_generator import generate_number
from call_handler import make_call

# Initialize main window
root = ttk.Window(themename="darkly")
root.geometry("300x550")
root.resizable(False, False)

# Store the dialed number
current_number = ttk.StringVar()

# === STYLE SECTION ===
style = ttk.Style()

# Display style (white background, black text)
style.configure(
    "WhiteEntry.TEntry",
    foreground="black",
    fieldbackground="white",
    borderwidth=2,
    font=("Courier", 18),
    relief="solid",
    padding=6
)

# Keypad + buttons style (white bg, black text)
style.configure(
    "Keypad.TButton",
    font=("Courier", 10),
    foreground="black",
    background="white",
    borderwidth=2,
    relief="solid",
    padding=10
)

# Call and end buttons (larger text for clarity)
style.configure(
    "Call.TButton",
    font=("Courier", 14), 
    padding=8
)

# === ENTRY DISPLAY FIELD ===
display = ttk.Entry(
    root,
    textvariable=current_number,
    style="WhiteEntry.TEntry",
    justify="center",
    font=("Courier", 18), # Increased font size for taller box
    width=18 # Wider display box
)
display.pack(pady=18) # Adds vertical padding inside

# === FUNCTION CALLBACKS ===
def press(num):
    current = current_number.get()
    current_number.set(current + str(num))

def clear():
    current_number.set("")

def call():
    number = current_number.get()
    if number:
        success = make_call(number)
        if success:
            messagebox.showinfo("Calling", f"Calling {number}...")
        else:
            messagebox.showerror("Error", "Call failed. Check number or internet.")
    else:
        messagebox.showwarning("Empty", "Please enter or generate a number.")

def end_call():
    messagebox.showinfo("Call Ended", "Call ended.")
    current_number.set("")

def generate_and_display():
    current_number.set(generate_number())
    
def backspace():
    current = current_number.get()
    current_number.set(current[:-1])

# === BUTTONS ===
buttons_frame = ttk.Frame(root)
buttons_frame.pack()

buttons = [
    [("1", ""), ("2", "ABC"), ("3", "DEF")],
    [("4", "GHI"), ("5", "JKL"), ("6", "MNO")],
    [("7", "PQRS"), ("8", "TUV"), ("9", "WXYZ")],
    [("*", ""), ("0", "+"), ("#", "")]
]

for row in buttons:
    row_frame = ttk.Frame(buttons_frame)
    row_frame.pack(pady=1)
    for digit, label in row:
        btn = ttk.Button(
            row_frame,
            text=f"{digit}\n{label}",
            width=6,
            style="Keypad.TButton",
            command=lambda c=digit: press(c)
        )
        btn.pack(side="left", padx=1)

# === CALL / END BUTTONS ===
control_frame = ttk.Frame(root)
control_frame.pack(pady=10)

call_btn = ttk.Button(
    control_frame,
    text="Call Number",
    width=8,
    style="Call.TButton",
    bootstyle="success",
    command=call
)
call_btn.pack(side="left", padx=10)

end_btn = ttk.Button(
    control_frame,
    text="End Call",
    width=8,
    style="Call.TButton",
    bootstyle="danger",
    command=end_call
)
end_btn.pack(side="left", padx=5)

# === CLEAR / GENERATE ===
clear_btn = ttk.Button(
    root,
    text="Clear",
    width=22,
    style="Keypad.TButton",
    command=clear
)
clear_btn.pack(pady=6)

generate_btn = ttk.Button(
    root,
    text="Generate Number",
    width=22,
    style="Keypad.TButton",
    command=generate_and_display
)
generate_btn.pack(pady=10)

backspace_btn = ttk.Button(
    root,
    text="⌫ Backspace",
    width=22,
    style="Keypad.TButton",
    command=backspace
)
backspace_btn.pack(pady=6)

def on_key(event):
    key = event.char
    if key.isalnum() or key in "*#+":  # Allow letters and symbols
        press(key.upper())
    elif key == "\x08":  # Backspace
        backspace()

root.bind("<Key>", on_key)

# === START THE APP ===
root.mainloop()
