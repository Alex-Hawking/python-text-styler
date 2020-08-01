#A Simple App That Styles Text
#By Alex Hawking

#Imports
import platform
import os
import tempfile
import textStuff as tx
from tkinter import *
from tkinter import messagebox
import tkinter.ttk as ttk


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
                messagebox.showwarning("Character Error", "Invalid Character: Please only use normal upper and lower case letters")
            else:
                #Output Text
                textArea.delete('1.0', END)
                output = []
                sep = ''
                for word in receivedData:
                    output.append(word)
                    output.append('\n\n')
                #Write To .txt File if User Wants
                if makeTxt.get() == 1:
                    print(desktop + "/style_out.txt")
                    dataToAddToTxt = inputArea.get() + ":\n\n" + sep.join(output) + "\n"
                    with open(desktop + "/style_out.txt", "a+", encoding="utf-8") as txtOut:
                        txtOut.write(dataToAddToTxt)
                    txtOut.close()
                textArea.insert(END, sep.join(output))

        #Create and Pack Widgets
        label_widget = Label(root, text="𝕋𝕖𝕩𝕥 𝕊𝕥𝕪𝕝𝕖𝕣", font=("Helvetica", 20), bg='#FFFFFF', fg="#0A0A0A")
        label_widget.pack(pady=5)
        inputArea = Entry(root, fg="#241909", bg="#EBEBEB")
        inputArea.pack()
        styleButton = Button(root, text ="Style Text", command = lambda: getText(tx.convertText(inputArea.get())))
        styleButton.pack(pady=8)
        textArea = Text(root, height=6, width=25,font=("Consolas", 15), wrap=WORD, fg="#241909", bg="#EBEBEB")     
        textArea.pack()
        makeTxt = IntVar()
        makeTxtCheckBox = Checkbutton(root, text='Add to style_out.txt file',variable=makeTxt, onvalue=1, offvalue=0, bg='#FFFFFF', fg="#0A0A0A").pack()

        self.pack(fill=BOTH, expand=1)

#Create Window
root = Tk()
app = Window(root)
root.resizable(0,0)
root.wm_title("𝕋𝕖𝕩𝕥 𝕊𝕥𝕪𝕝𝕖𝕣 ✎")
root.iconbitmap(default=ICON_PATH)
root.geometry("320x275")
root.configure(bg='#FFFFFF')
root.mainloop()