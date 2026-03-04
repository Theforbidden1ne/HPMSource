import tkinter as tk
from tkinter import messagebox
import json
import subprocess
import os
import shutil

packageInstallPath = 'C:/HyperionPackages'

def launch_app(exe_path):
    try:
        subprocess.Popen(exe_path)
    except Exception as e:
        messagebox.showerror("Error", f"Could not launch: {e}")

def install_package():
    installer_path = os.path.join(os.getcwd(), "packageInstaller.exe")
    if os.path.exists(installer_path):
        subprocess.Popen(installer_path)
    else:
        messagebox.showerror("Error", "packageInstaller.exe not found!")

def delete_package(pkg_id, app_name, root):
    if messagebox.askyesno("Confirm", f"Permanently delete {app_name}?"):
        folder_path = os.path.join(packageInstallPath, app_name)
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)
        
        with open(f"{packageInstallPath}/packages.jsonl", 'r') as f:
            data = json.load(f)
        
        if pkg_id in data["packages"]:
            del data["packages"][pkg_id]
            
        with open(f"{packageInstallPath}/packages.jsonl", 'w') as f:
            json.dump(data, f, indent=4)
        
        messagebox.showinfo("Success", "Deleted. Please restart.")

def build_gui():
    root = tk.Tk()
    root.title("Hyperion Frontend")
    
    ## Fullscreen settings
    root.attributes('-fullscreen', True)
    root.configure(bg='#121212') # Dark background
    
    # Keybind to escape fullscreen (Escape key)
    root.bind("<Escape>", lambda e: root.attributes("-fullscreen", False))

    # Header
    header = tk.Label(root, text="HYPERION LIBRARY", font=("Arial", 32, "bold"), 
                      bg='#121212', fg='white', pady=40)
    header.pack()

    # Main Scrollable Area (or just a container)
    container = tk.Frame(root, bg='#121212')
    container.pack(expand=True, fill="both", padx=100)

    # Load Packages
    try:
        with open(f"{packageInstallPath}/packages.jsonl", 'r') as f:
            data = json.load(f)
            packages = data.get("packages", {})
    except FileNotFoundError:
        packages = {}

    for pkg_id, info in packages.items():
        app_name = info.get("name", pkg_id)
        exe_path = os.path.join(packageInstallPath, app_name, info["executable"])
        
        row = tk.Frame(container, bg='#1e1e1e', pady=10, padx=20)
        row.pack(fill="x", pady=5)

        tk.Label(row, text=app_name.upper(), font=("Arial", 18), 
                 bg='#1e1e1e', fg='white').pack(side="left")

        # Delete Button (Right)
        tk.Button(row, text="DELETE", bg="#cf6679", fg="black", font=("Arial", 12, "bold"),
                  command=lambda i=pkg_id, n=app_name: delete_package(i, n, root), 
                  width=10).pack(side="right", padx=10)

        # Launch Button (Right)
        tk.Button(row, text="PLAY", bg="#03dac6", fg="black", font=("Arial", 12, "bold"),
                  command=lambda p=exe_path: launch_app(p), 
                  width=15).pack(side="right", padx=10)

    # Bottom Toolbar
    toolbar = tk.Frame(root, bg='#121212', pady=20)
    toolbar.pack(side="bottom", fill="x")

    tk.Button(toolbar, text="INSTALL PACKAGE", bg="#bb86fc", font=("Arial", 14),
              command=install_package, width=20).pack(side="left", padx=50)

    tk.Button(toolbar, text="QUIT", bg="#333333", fg="white", font=("Arial", 14),
              command=root.destroy, width=10).pack(side="right", padx=50)

    root.mainloop()

if __name__ == "__main__":
    build_gui()
