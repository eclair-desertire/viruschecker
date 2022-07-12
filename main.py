
from tkinter import filedialog
import apikey # your own file with YOUR API KEY, you can get it on virustotal site
import vt
from tkinter import *
import threading



root=Tk()
root.geometry("500x300")
root.resizable(0,0)
root.title("Viruschecker")
root.configure(bg="white")

vir_url=StringVar()
Label(root,text="Paste the Link you want to check here:",font="arial 15 bold",
    bg="white").place(x=20,y=20)
link_enter=Entry(root, width=50, textvariable=vir_url).place(x=20,y=40)

#root.filename=filedialog.askopenfilename(initialdir="/",title="Select a file",filetypes=(("all files","*.*")))
def scan_file():
    file=filedialog.askopenfile()

def scan_url():
    pass

Button(root,text="Check url",command=threading.Thread(target=scan_url).start).place(x=190,y=70)
Button(root, text="Select File to check",command=threading.Thread(target=scan_file).start).place(x=20,y=200)
client=vt.Client(apikey.api_key)

root.mainloop()