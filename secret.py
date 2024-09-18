import ctypes
import os
import shutil
import time
import tkinter as tk
from tkinter import filedialog, messagebox

def secrets():
    def hide():
        def move_and_hide_windows(source_path, destination_path):
            try:
                shutil.move(source_path, destination_path)
                dis_file_path = os.path.join(destination_path, os.path.basename(source_path))
                set_file_attributes = ctypes.windll.kernel32.SetFileAttributesW
                set_file_attributes(dis_file_path, 2)
            except Exception as e:
                messagebox.showinfo("Information", "Error occured while hiding: May be the error will be the file is in the same dir.")

        destination_folder = r'E:\@_M I N\.hidden'
        def choose_file():
            path = filedialog.askopenfilename(initialdir="/", title="Select File")
            if path:
                source = path
                move_and_hide_windows(source, destination_folder)
                messagebox.showinfo("Information", "File hided successfully")
                exit()
        def choose_directory():
            path = filedialog.askdirectory(initialdir="/", title="Select Directory")
            if path:
                source = path
                move_and_hide_windows(source, destination_folder)
                messagebox.showinfo("Information", "folder hided successfully")
                exit()
        root1 = tk.Tk()
        root1.title("Hide files or folder")
        root1.geometry("160x130")
        dialog = root1
        file_button = tk.Button(dialog, text="Choose File", command=choose_file)
        file_button.pack(pady=20)
        directory_button = tk.Button(dialog, text="Choose Directory", command=choose_directory)
        directory_button.pack()
        window.withdraw()
        dialog.mainloop()

    def unhide():
        directory = r'E:\@_M I N\.hidden'
        def unhide_the_file():
            root3 = tk.Tk()
            root3.title("Unhide file")
            root3.geometry("200x200")
            dialog = root3
            hidden_files = []
            for file_name in os.listdir(directory):
                file_path = os.path.join(directory, file_name)
                if os.path.isfile(file_path) and (os.stat(file_path).st_file_attributes & 2):
                    hidden_files.append(file_path)
            if hidden_files:
                for file_path in hidden_files:
                    def on_button_click(name):
                        set_file_attributes = ctypes.windll.kernel32.SetFileAttributesW
                        result = set_file_attributes(name, 0)
                        if result == 1:
                            messagebox.showinfo("Information", "File Unhided successfully")
                        else:
                            messagebox.showinfo("Information", "File Unhided failed")
                    file_button = tk.Button(dialog, text=file_path[19:], command=lambda: on_button_click(file_path))
                    file_button.pack(pady=20)
            else:
                tk.Label(text="There is No Hided files")
            window.withdraw()
            dialog.mainloop()
        def unhide_the_folder():
            root4 = tk.Tk()
            root4.title("Unhide folder")
            root4.geometry("200x200")
            dialog = root4
            hidden_directories = []
            for dir_name in os.listdir(directory):
                dir_path = os.path.join(directory, dir_name)
                if os.path.isdir(dir_path) and (os.stat(dir_path).st_file_attributes & 2):
                    hidden_directories.append(dir_path)
            if hidden_directories:
                for dir_path in hidden_directories:
                    def on_button_click(name):
                        set_file_attributes = ctypes.windll.kernel32.SetFileAttributesW
                        result = set_file_attributes(name, 0)
                        if result == 1:
                            messagebox.showinfo("Information", "File Unhided successfully")
                            exit()
                        else:
                            messagebox.showinfo("Information", "File Unhided failed")
                            exit()
                    file_button = tk.Button(dialog, text=dir_path[19:], command=lambda: on_button_click(dir_path))
                    file_button.pack(pady=20)
            else:
                tk.Label(text="There is No Hided files")
            window.withdraw()
            dialog.mainloop()

        root2 = tk.Tk()
        root2.title("Unhide file of folder")
        root2.geometry("160x130")
        dialog = root2
        file_button = tk.Button(dialog, text="Unhide a File",command=unhide_the_file)
        file_button.pack(pady=20)
        directory_button = tk.Button(dialog, text="Unhide a folder",command=unhide_the_folder)
        directory_button.pack()
        window.withdraw()
        dialog.mainloop()


    window = tk.Tk()
    window.title("Secret")
    window_width = 160
    window_height = 130
    window.geometry(f"{window_width}x{window_height}")
    hide_btn = tk.Button(window, text="Hide a folder or file", command=hide)
    hide_btn.grid(row=0, column=0, padx=20, pady=20)
    un_hide_btn = tk.Button(window, text="Unhide a files or folder", command=unhide)
    un_hide_btn.grid(row=1, column=0, padx=0, pady=0)
    window.mainloop()
