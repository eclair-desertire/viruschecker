import tkinter as tk
from tkinter import ttk
import asyncio
from tkinter import filedialog
from tkinter import messagebox
import apikey # your own file with YOUR API KEY, you can get it on virustotal site
import vt
from tkinter import *

class App:
    async def exec(self):
        self.window = Window(asyncio.get_event_loop())
        await self.window.show()

class Window(tk.Tk):
    def __init__(self, loop):
        self.loop = loop
        self.client=vt.Client(apikey.api_key)
        self.root = tk.Tk()
        self.root.geometry("500x300")
        self.root.geometry("500x300")
        self.root.resizable(0,0)
        self.root.title("Viruschecker")
        self.root.configure(bg="white")
        self.vir_url=StringVar()
        Label(self.root,text="Paste the Link you want to check here:",font="arial 15 bold",
        bg="white").place(x=20,y=20)
        self.link_enter=Entry(self.root, width=50, textvariable=self.vir_url).place(x=20,y=40)
        Button(self.root,text="Check url",command=self.scan_link).place(x=190,y=70)
        Button(self.root, text="Select File to check",command=self.scan_file).place(x=20,y=200)

    async def show(self):
        while True:
            self.root.update()
            await asyncio.sleep(.1)

    async def scan_file(self):
        file=filedialog.askopenfile()
        await asyncio.sleep(0)

    async def scan_link(self):
        self.client.scan_url(self.vir_url.get())
        analysis = vt.url_id(self.vir_url.get())
        url = self.client.get_object("/urls/{}".format(analysis))

        print(url.times_submitted)
        messagebox.showinfo("Information about link",f"Times submitted:{url.times_submitted}")
        print(url.last_analysis_stats)
        await asyncio.sleep(0)

    async def calculate_async(self):
        max = 3000000
        for i in range(1, max):
            self.progressbar["value"] = i / max * 100
            if i % 1000 == 0:
                await asyncio.sleep(0)

asyncio.run(App().exec())











