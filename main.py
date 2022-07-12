import tkinter as tk
from tkinter import ttk
import asyncio
from tkinter import filedialog
import apikey # your own file with YOUR API KEY, you can get it on virustotal site
import vt
from tkinter import *
import threading

class App:
    async def exec(self):
        self.window = Window(asyncio.get_event_loop())
        await self.window.show()

class Window(Tk.tk):
    def __init__(self, loop):
        self.loop = loop
        self.root = tk.Tk()
        self.label = tk.Label(text="")
        self.label.grid(row=0, columnspan=2, padx=(8, 8), pady=(16, 0))
        self.progressbar = ttk.Progressbar(length=280)
        self.progressbar.grid(row=1, columnspan=2, padx=(8, 8), pady=(16, 0))
        button_block = tk.Button(text="Calculate Sync", width=10, command=self.calculate_sync)
        button_block.grid(row=2, column=0, sticky=tk.W, padx=8, pady=8)
        button_non_block = tk.Button(text="Calculate Async", width=10, command=lambda: self.loop.create_task(self.calculate_async()))
        button_non_block.grid(row=2, column=1, sticky=tk.W, padx=8, pady=8)

    async def show(self):
        while True:
            self.label["text"] = self.animation
            self.animation = self.animation[1:] + self.animation[0]
            self.root.update()
            await asyncio.sleep(.1)

    def calculate_sync(self):
        max = 3000000
        for i in range(1, max):
            self.progressbar["value"] = i / max * 100

    async def calculate_async(self):
        max = 3000000
        for i in range(1, max):
            self.progressbar["value"] = i / max * 100
            if i % 1000 == 0:
                await asyncio.sleep(0)

asyncio.run(App().exec())

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

def scan_link():
    client.scan_url(vir_url.get())
    analysis = vt.url_id(vir_url.get())
    url = client.get_object("/urls/{}".format(analysis))

    print(url.times_submitted)
    print(url.last_analysis_stats)

Button(root,text="Check url",command=threading.Thread(target=scan_link).start).place(x=190,y=70)
Button(root, text="Select File to check",command=threading.Thread(target=scan_file).start).place(x=20,y=200)
client=vt.Client(apikey.api_key)

root.mainloop()