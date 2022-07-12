import pdb
import apikey # your own file with YOUR API KEY, you can get it on virustotal site
import vt
from tkinter import *
import threading


pdb.set_trace()

root=Tk()
root.geometry("500x300")
root.resizable(0,0)
root.title("Viruschecker")
root.configure(bg="black")

def scan_file():
    pass

def scan_url():
    pass

client=vt.Client(apikey.api_key)

root.mainloop()