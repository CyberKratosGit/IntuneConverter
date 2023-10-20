import tkinter as tk
from tkinter import filedialog, messagebox
import os
import subprocess


def select_source_folder():
    folder = filedialog.askdirectory()
    source_folder_var.set(folder)


def select_output_folder():
    folder = filedialog.askdirectory()
    output_folder_var.set(folder)


def convert_to_intunewin():
    source_folder = source_folder_var.get()
    output_folder = output_folder_var.get()

    # Assuming IntuneWinAppUtil.exe is in the same directory as this script
    tool_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), "IntuneWinAppUtil.exe")

    installer_file = filedialog.askopenfilename(initialdir=source_folder, title="Select installer file",
                                                filetypes=(("Executable files", "*.exe;*.msi"), ("All files", "*.*")))

    if not installer_file:
        return

    cmd = [tool_path, "-c", source_folder, "-s", installer_file, "-o", output_folder]

    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    if result.returncode == 0:
        messagebox.showinfo("Success", "Conversion completed successfully!")
    else:
        messagebox.showerror("Error", f"Conversion failed!\n\n{result.stderr}")


app = tk.Tk()
app.title("IntuneWin Converter")

source_folder_var = tk.StringVar()
output_folder_var = tk.StringVar()

tk.Label(app, text="Source Folder:").pack(pady=10)
tk.Entry(app, textvariable=source_folder_var, width=50).pack()
tk.Button(app, text="Select Source Folder", command=select_source_folder).pack(pady=10)

tk.Label(app, text="Output Folder:").pack(pady=10)
tk.Entry(app, textvariable=output_folder_var, width=50).pack()
tk.Button(app, text="Select Output Folder", command=select_output_folder).pack(pady=10)

tk.Button(app, text="Convert to IntuneWin", command=convert_to_intunewin).pack(pady=20)

app.mainloop()
