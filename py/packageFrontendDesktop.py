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
    ## Launch packageInstaller.exe located in the same directory as this script
    installer_path = os.path.join(os.getcwd(), "packageInstaller.exe")
    if os.path.exists(installer_path):
        subprocess.Popen(installer_path)
    else:
        messagebox.showerror("Error", "packageInstaller.exe not found!")

def delete_package(pkg_id, app_name, root):
    if messagebox.askyesno("Confirm", f"Delete {app_name}?"):
        # 1. Remove folder
        folder_path = os.path.join(packageInstallPath, app_name)
        if os.path.exists(folder_path):
            shutil.rmtree(folder_path)
        
        # 2. Update JSON
        with open(f"{packageInstallPath}/packages.jsonl", 'r') as f:
            data = json.load(f)
        
        if pkg_id in data["packages"]:
            del data["packages"][pkg_id]
            
        with open(f"{packageInstallPath}/packages.jsonl", 'w') as f:
            json.dump(data, f, indent=4)
        
        # 3. Refresh UI (simplest way is to restart build_gui or clear frames)
        messagebox.showinfo("Success", "Package deleted. Please restart the launcher.")

def build_gui():
    root = tk.Tk()
    root.title("Hyperion Manager")
    root.geometry("500x600")

    # Install Button (Top)
    install_btn = tk.Button(root, text="+ Install New Package", bg="green", fg="white", 
                            command=install_package, height=2)
    install_btn.pack(fill="x", padx=10, pady=10)

    # Package List
    try:
        with open(f"{packageInstallPath}/packages.jsonl", 'r') as f:
            data = json.load(f)
            packages = data.get("packages", {})
    except FileNotFoundError:
        packages = {}

    for pkg_id, info in packages.items():
        frame = tk.Frame(root, pady=5)
        frame.pack(fill="x", padx=10)

        app_name = info.get("name", pkg_id)
        exe_path = os.path.join(packageInstallPath, app_name, info["executable"])

        # Launch Button
        tk.Button(frame, text=f"Launch {app_name}", width=30,
                  command=lambda p=exe_path: launch_app(p)).pack(side="left", padx=5)
        
        # Delete Button
        tk.Button(frame, text="Delete", bg="red", fg="white",
                  command=lambda i=pkg_id, n=app_name: delete_package(i, n, root)).pack(side="right", padx=5)

    root.mainloop()

if __name__ == "__main__":
    build_gui()
