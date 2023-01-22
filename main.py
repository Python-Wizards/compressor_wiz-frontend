import customtkinter

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.geometry("500x350")

def login():
    print("Test")

frame = customtkinter.CTkFrame(master=root)
frame.grid(row=0, column=0,pady=20, padx=60)

label = customtkinter.CTkLabel(master=frame, text="File Compressor")
label.grid(row=0, column=0,pady=20, padx=60)

label = customtkinter.CTkLabel(master=frame, text="Logs")
label.grid(row=0, column=2,pady=20, padx=60)

button = customtkinter.CTkButton(master=frame,
                text = "Select File")
button.grid(row=1, column=0, padx=10, pady=10)

button1 = customtkinter.CTkButton(master=frame,
                text = "Extract")
button1.grid(pady=10)

button2 = customtkinter.CTkButton(master=frame,
                text = "Explore")
button2.grid(pady=10)
root.mainloop()

#!/usr/bin/python
# basic file compression/decompression program using zipfile module
# please take note that the program uses comments for now to execute specific def.
# hello

# Declare important program variables
prog_nm="CompressorWiz"
prog_ver="0.1alpha"

# Import front-end framework
#import tkinter as gui

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

#window = gui.Tk()
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
