import zipfile
import time
import os
import shutil
import tkinter as tk
from tkinter import filedialog
def extractPackage():
    folder = 'temp'
    root = tk.Tk()
    root.withdraw() 
    file_path = filedialog.askopenfilename(
        title="Select a file",
        initialdir="./", # Optional: sets the initial directory
        filetypes=(("Hyperion Package Files", "*.hpkg"), ("All files", "*.*")) # Optional: filters file types
    )
    with zipfile.ZipFile(file_path, 'r') as archive:
        archive.extractall(path=folder)
        print("All files extracted.")

def cleanupPackage():
    time.sleep(3)
    shutil.rmtree('temp')

if __name__ == "__main__":
    print("This is not a direct python executable, this is a module. This is to be imported and used in other scripts")