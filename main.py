#A Simple App That Styles Text
#By Alex Hawking

#Imports
import platform
import os
import tempfile
import textStuff as tx
import tkinter as tk
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from ttkthemes import ThemedTk

#Transparent Icon Courtesy Of https://stackoverflow.com/users/1546993/ubomb
ICON = (b'\x00\x00\x01\x00\x01\x00\x10\x10\x00\x00\x01\x00\x08\x00h\x05\x00\x00'
        b'\x16\x00\x00\x00(\x00\x00\x00\x10\x00\x00\x00 \x00\x00\x00\x01\x00'
        b'\x08\x00\x00\x00\x00\x00@\x05\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        b'\x00\x01\x00\x00\x00\x01') + b'\x00'*1282 + b'\xff'*64
_, ICON_PATH = tempfile.mkstemp()
with open(ICON_PATH, 'wb') as icon_file:
    icon_file.write(ICON)

#Get Path Of Desktop
desktop = os.path.expanduser("~/Desktop")


#Create Window
class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)        
        self.master = master

        #Receive Styled Text From GetText()
        def getText(receivedData):
            #Check If Character Err
            if receivedData == 'error':
                messagebox.showwarning("Character Error", "Invalid Character: Please only use supported characters")
            else:
                #Output Text
                textArea.delete('1.0', END)
                output = []
                sep = ''

                def addTextToTextArea(styledArray):
                    #Write To .txt File if User Wants
                    if makeTxt.get() == 1:
                        print(desktop + "/style_out.txt")
                        dataToAddToTxt = inputArea.get() + ":\n\n" + sep.join(styledArray) + "\n"
                        with open(desktop + "/style_out.txt", "a+", encoding="utf-8") as txtOut:
                            txtOut.write(dataToAddToTxt)
                        txtOut.close()
                    textArea.insert(END, sep.join(output))

                #Run if the user wants to have a border
                if addBorder.get() == 1:
                    #Send Styled and Bordered Text to addTextToTextArea function
                    def sendBorder():
                        try:
                            selectedBorder = borderSelect.get().split(' ')
                            for word in receivedData:
                                output.append(selectedBorder[0] + word + selectedBorder[2])
                                output.append('\n\n')
                            addTextToTextArea(output)
                            borderWindow.destroy()
                        except:
                            messagebox.showwarning("Border Error", "Selection Error: Please select a border from the dropdown")

                    #Create select border window
                    borderWindow = tk.Toplevel(root)
                    borderWindow.resizable(0,0)
                    borderWindow.wm_title("ミ★𝕊𝕖𝕝𝕖𝕔𝕥 𝔸 𝔹𝕠𝕣𝕕𝕖𝕣★彡")
                    borderWindow.iconbitmap(default=ICON_PATH)
                    borderWindow.geometry("320x150")
                    borderWindow.configure(bg="#424242")

                    comboboxFont = ("Helvetica", 10)
                    borderWindowTitle = ttk.Label(borderWindow, text = "𝕊𝕖𝕝𝕖𝕔𝕥 𝔸 𝔹𝕠𝕣𝕕𝕖𝕣", font=("Helvetica", 25))
                    borderSelect = ttk.Combobox(borderWindow, values=tx.borders, font = comboboxFont, width=35)
                    useBorderButton = ttk.Button(borderWindow, text ="Use this border", command=sendBorder)
                    borderWindowTitle.pack(pady=8)
                    borderSelect.pack(pady=2)
                    useBorderButton.pack(pady=5)

                elif addBorder.get() != 1:
                    for word in receivedData:
                        output.append(word)
                        output.append('\n\n')
                    addTextToTextArea(output)
                    
        makeTxt = IntVar()
        addBorder = IntVar()
        #Create and Pack Widgets
        label_widget = ttk.Label(root, text="𝕋𝕖𝕩𝕥 𝕊𝕥𝕪𝕝𝕖𝕣", font=("Helvetica", 20))
        label_widget.pack(pady=5)
        inputArea = ttk.Entry(root)
        inputArea.pack()
        styleButton = ttk.Button(root, text ="Style Text", command = lambda: getText(tx.convertText(inputArea.get())))
        styleButton.pack(pady=8)
        addBorderCheckBox = ttk.Checkbutton(root, text='Add border',variable=addBorder, onvalue=1, offvalue=0).pack(side=TOP, pady=5)
        textArea = Text(root, height=6, width=35,font=("Consolas", 15), wrap=WORD)  
        textArea.pack()
        makeTxtCheckBox = ttk.Checkbutton(root, text='Add to style_out.txt file',variable=makeTxt, onvalue=1, offvalue=0).pack(side=TOP, pady=5)      

        self.pack(fill=BOTH, expand=1)

#Create and Define 
root = ThemedTk(theme="black")
app = Window(root)
root.resizable(0,0)
root.configure(bg="#424242")
root.wm_title("𝕋𝕖𝕩𝕥 𝕊𝕥𝕪𝕝𝕖𝕣 ✎")
root.iconbitmap(default=ICON_PATH)
root.geometry("425x300")

root.mainloop()

