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
    bg="white").place(x=40,y=40)
link_enter=Entry(root, width=50, textvariable=vir_url).place(x=32,y=90)

def scan_file():
    pass

def scan_url():
    pass

client=vt.Client(apikey.api_key)

root.mainloop()