#!/usr/bin/python
# basic file compression/decompression program using zipfile module
# please take note that the program uses comments for now to execute specific def.

# Declare important program variables
prog_nm="CompressorWiz"
prog_ver="0.1alpha"

# Import front-end framework
import customtkinter
import tkinter as tk
from tkinter import ttk

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


# Import "zipfile" module from python
## import zipfile

# compress_file definition/function
##def compress_file(filenm):
    # Initialize the compression parameters
    ##with zipfile.ZipFile('test.zip', 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zip:
        # Compress based on the file name provided
        ##zip.write(filenm)
# decompress_file definition/function
##def decompress_file(compressed_filenm):
    
    # Initialize the decompression parameters
    ##with zipfile.ZipFile(compressed_filenm, 'r') as zip:
        # Decompress the file name provided to a folder named "extracted"
        ##zip.extractall(path="extracted")

window = customtkinter.CTk()
window.geometry("500x320")
window.title(prog_nm+"-("+prog_ver+")")


def compress():
        header_compress = customtkinter.CTkLabel(master=frame_Log, text="Correct")
        header_compress.grid(row=5, column = 0, padx=(0, 60), pady=(0, 30))

def option(value):
    print("segmented button clicked:", value)

def command_function(value):
        if value == "  Compression level":
          Compression_lvl()
        elif value == "  Help ":
          help()


    
def Compression_lvl():
    style = ttk.Style()
    style.theme_use("alt")
    compression_level_window = tk.Toplevel(master=window)
    compression_level_window.configure(bg = '#1a1a1a')
    compression_level_window.geometry("400x250+200+200")
    compression_level_window.transient(master=window)
    compression_level_window.grab_set()
    compression_level_window.title("Compression Level")
    # create a label
    label = tk.Label(master=compression_level_window, text="Enter the compression level (1-9):")
    label.grid(row=0, column=0, padx=20, pady=20)
    # create an entry widget
    entry = tk.Entry(master=compression_level_window)
    entry.grid(row=1, column=0, padx=0, pady=0)
    # create a submit button
    submit_button = tk.Button(master=compression_level_window, text="Submit", command=lambda: submit_compression_level(entry.get()))
    submit_button.grid(row=2, column=0, padx=15, pady=15)
    # add a close button
    close_button = tk.Button(master=compression_level_window, text="Close", command=compression_level_window.destroy)
    close_button.grid(row=3, column=0, padx=15, pady=15)
    compression_level_window.columnconfigure(0, weight=1)


def submit_compression_level(level):
    level = int(level)
    if level < 1 or level > 9:
        messagebox.showerror("Error", "Invalid compression level")
    else:
        # do something with the valid level
        print(f"The compression level is {level}")
        
        

def help():
    style = ttk.Style()
    style.theme_use("alt")
    compression_level_window = tk.Toplevel(master=window)
    compression_level_window.configure(bg = '#1a1a1a')
    compression_level_window.geometry("400x250+200+200")
    compression_level_window.transient(master=window)
    compression_level_window.grab_set()
    compression_level_window.title("Help")
   


#side bar button
frame = customtkinter.CTkFrame(master=window, width=160, corner_radius=0)
frame.grid(row=1, column = 0,padx=20, pady=10)

header = customtkinter.CTkLabel(master=frame, text=prog_nm+"-("+prog_ver+")")
header.grid(row=1, column = 0, padx=20, pady=10)

button_select = customtkinter.CTkButton(master = frame, text="Select File", command = compress)
button_select.grid(row=3, column=0, padx=25, pady=10)
button_compress = customtkinter.CTkButton(master = frame, text="Compress File", command = compress)
button_compress.grid(row=4, column=0, padx=25, pady=10)
button_extract = customtkinter.CTkButton(master = frame, text="Extract File", command = compress)
button_extract.grid(row=5, column=0,padx=25, pady =10)
button_explore = customtkinter.CTkButton(master = frame, text="Explore File", command = compress)
button_explore.grid(row=6, column=0, padx=25, pady=10)

#side bar log
frame_Log = customtkinter.CTkFrame(master=window, width=200, height= 200,corner_radius=0)
frame_Log.grid(row=1, column = 1,padx=10, pady=0)

header_Log = customtkinter.CTkLabel(master=frame_Log, text="Log")
header_Log.grid(row=1, column = 0, padx=0, pady=20)

button_exit= customtkinter.CTkButton(master=frame_Log, text = "Exit", command=exit)
button_exit.grid(row= 70, column=0,padx=50, pady=(100,40))

button_option = customtkinter.CTkSegmentedButton(master=window,values=["  Compression level", "  Help "],command=command_function)
button_option.grid(row=0, column = 0,padx=0, pady=10)# set initial value

window.resizable(False, False)
window.mainloop()


#window.title(prog_nm+"-("+prog_ver+")")
#header = gui.Label(window, text=prog_nm+"-"+prog_ver, height=5, font="Helvetica 20 bold")
#header.pack()
#button_extract = gui.Button(window, text = "Compress", command = lambda: compress_file("testfile.txt"))
#button_extract.pack()
#exit_button = gui.Button(window, text='Exit', command=window.destroy)
#exit_button.pack()
#window.mainloop()

#compress_file("testfile.txt")
#decompress_file("test.zip")
