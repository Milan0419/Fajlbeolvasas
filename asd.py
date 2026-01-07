import tkinter as tk
import random
import time
import threading

# -----------------------------
# Main window
# -----------------------------
root = tk.Tk()
root.title("HAWKINS NATIONAL LAB — J-7 TERMINAL")
root.geometry("800x500")
root.configure(bg="black")
root.resizable(False, False)

# -----------------------------
# Frames
# -----------------------------
terminal_frame = tk.Frame(root, bg="black")
terminal_frame.pack(fill="both", expand=True)

logo_frame = tk.Frame(root, bg="black")

# -----------------------------
# Terminal
# -----------------------------
terminal = tk.Text(
    terminal_frame,
    bg="black",
    fg="#00ff66",
    insertbackground="#00ff66",
    font=("Courier New", 12),
    wrap="word",
    state="disabled"
)
terminal.pack(fill="both", expand=True, padx=10, pady=10)

# -----------------------------
# Input
# -----------------------------
input_frame = tk.Frame(terminal_frame, bg="black")
input_frame.pack(fill="x", padx=10, pady=(0, 10))

prompt = tk.Label(
    input_frame,
    text="J-7 >",
    fg="#00ff66",
    bg="black",
    font=("Courier New", 12)
)
prompt.pack(side="left")

command_entry = tk.Entry(
    input_frame,
    bg="black",
    fg="#00ff66",
    insertbackground="#00ff66",
    font=("Courier New", 12),
    relief="flat"
)
command_entry.pack(side="left", fill="x", expand=True)
command_entry.focus()

# -----------------------------
# Logo Mode
# -----------------------------
logo_image = tk.PhotoImage(file="j7.png")
logo_label = tk.Label(logo_frame, image=logo_image, bg="black")
logo_label.pack(expand=True)

def show_logo_mode():
    terminal_frame.pack_forget()
    logo_frame.pack(fill="both", expand=True)

def show_terminal_mode():
    logo_frame.pack_forget()
    terminal_frame.pack(fill="both", expand=True)
    command_entry.focus()

# -----------------------------
# Helper functions
# -----------------------------
def write_text(text, delay=0.03):
    terminal.configure(state="normal")
    for char in text:
        terminal.insert("end", char)
        terminal.see("end")
        terminal.update()
        time.sleep(delay)
    terminal.insert("end", "\n")
    terminal.configure(state="disabled")

def glitch_text(text):
    return "".join(
        random.choice("#$%&@!?") if random.random() < 0.1 else c
        for c in text
    )

# -----------------------------
# Boot
# -----------------------------
def boot_sequence():
    messages = [
        "INITIALIZING HAWKINS NATIONAL LAB SYSTEM...",
        "ACCESSING SECTOR J-7...",
        "WARNING: CLASSIFIED ENVIRONMENT",
        "SYSTEM ONLINE"
    ]
    for msg in messages:
        write_text(msg)
        time.sleep(0.4)

    write_text("\nTYPE 'HELP' FOR COMMANDS\n", 0.02)

# -----------------------------
# Commands
# -----------------------------
def handle_command(event=None):
    cmd = command_entry.get().strip().lower()
    command_entry.delete(0, "end")

    terminal.configure(state="normal")
    terminal.insert("end", f"\nJ-7 > {cmd}\n")
    terminal.configure(state="disabled")

    if cmd == "help":
        write_text("COMMANDS:")
        write_text("  status    - SYSTEM STATUS")
        write_text("  subject   - TEST SUBJECT")
        write_text("  j7        - J-7 LOCKDOWN MODE")
        write_text("  terminal  - RETURN TO TERMINAL")
        write_text("  clear     - CLEAR SCREEN")
        write_text("  exit      - SHUTDOWN")

    elif cmd == "status":
        write_text(glitch_text("GATE STATUS: CONTAINED"))
        write_text(glitch_text("POWER LEVEL: 99%"))

    elif cmd == "subject":
        write_text("SUBJECT: 011")
        write_text(glitch_text("STATUS: UNKNOWN"))

    elif cmd == "j7":
        write_text("ENTERING J-7 LOCKDOWN MODE...")
        root.after(500, show_logo_mode)

    elif cmd == "terminal":
        show_terminal_mode()

    elif cmd == "clear":
        terminal.configure(state="normal")
        terminal.delete("1.0", "end")
        terminal.configure(state="disabled")

    elif cmd == "exit":
        write_text("SYSTEM SHUTDOWN...")
        root.after(1000, root.destroy)

    else:
        write_text(glitch_text("UNKNOWN COMMAND"))

command_entry.bind("<Return>", handle_command)

# -----------------------------
# Start
# -----------------------------
threading.Thread(target=boot_sequence, daemon=True).start()
root.mainloop()
