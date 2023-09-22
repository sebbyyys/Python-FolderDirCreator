import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import *
import os 
import sys

# root window
root = tk.Tk()
root.geometry("445x500")
root.title('Folder Creator')
# root.resizable(0, 0)

# configure the grid
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=10)
root.columnconfigure(2, weight=3)

def printOutput():
        current_directory = filedialog.askdirectory()
        file_name = ""
        file_path = os.path.join(current_directory, file_name)
        print(file_path)
        DirectoryOutput.delete(0,END)
        DirectoryOutput.insert(0,current_directory)
        return
        
        
def exit():
    sys.exit()


Title = ttk.Label(root, text = "Folder Manager")
Title.grid(column = 0, row = 0, sticky=tk.N, padx=5, pady = 5, columnspan=2)

# username
DirectoryText = ttk.Label(root, text="Browse for where you want the folders: ")
DirectoryText.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

DirectoryOutput = ttk.Entry(root)
DirectoryOutput.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

BrowseDirectory = ttk.Button(root, text = "Browse", command=printOutput)
BrowseDirectory.grid(column=2, row=1, sticky=tk.E, padx=5, pady=5)

# password
FolderText = ttk.Label(root, text="Enter folder names followed by colon: ")
FolderText.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

FolderEntry = ttk.Entry(root)
FolderEntry.grid(column=1, row=2, sticky=tk.E, padx=5, pady=5)

# login button
SubmitButton = ttk.Button(root, text="Exit", command=exit)
SubmitButton.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

root.mainloop()