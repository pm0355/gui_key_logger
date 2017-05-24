import Tkinter as tk
from Tkinter import *
import os
import time
from collections import Counter
import json

os.system('xset r off')

begin=0
end=0
key_arr ={}
flight=False
flight_time=0

fields = 'User Name', 'Password-0', 'Password-1', 'Password-2', 'Password-3', 'Password-4', 'Password-5','Password-6','Password-7','Password-8','Password-9'

def fetch(entries):
    for entry in entries:
        field =entry[0]
	text = entry[1].get()
	print('%s: "%s"' % (field, text))
def makeRegForm(root):
    b1=Button(root,text="Register",command='')
    b1.pack(side=RIGHT, padx=5, pady=5)
    b2=Button(root,text="Quit",command=root.quit)
    b2.pack(side=LEFT, padx=5, pady=5)
def makeform(root, fields):
    entries = []
    for field in fields:
        row = Frame(root)
        lab = Label(row, width=15, text=field, anchor='w')
        ent = Entry(row)
        ent.bind("<KeyPress>",keyPress)
        ent.bind("<KeyRelease>",keyRelease)
        row.pack(side=TOP, fill=X, padx=5, pady=5)
        lab.pack(side=LEFT)
        ent.pack(side=RIGHT, expand=YES,fill=X)
        ent.focus_set()
        entries.append((field,ent))
    return entries

def keyPress(e):
    t1 = time.time()
    global begin
    begin = t1
    global flight
    global flight_time
    global end
    if flight == True:
	flight_time=begin-end
    flight=False


def keyRelease(e):
    t0 = time.time()
    tup={}
    global end
    global begin
    end = t0
    dwell_time = end-begin
    global key_arr
    global flight_time
    tup[e.char]=[dwell_time,flight_time]
    key_arr.update(tup)
    global flight
    flight=True

class MainWindow(tk.Frame):
    counter = 0
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        label=tk.Label(self,text="Credentials keylogger app")
	label.pack(side='top',padx=5,pady=5)
	self.button = tk.Button(self, text="Register",
                                command=self.create_window)
        self.button.pack(side="left",padx=5,pady=5)
	self.button=tk.Button(self,text="Quit",command=self.destroy)
	self.button.pack(side='right',padx=5,pady=5)

    def create_window(self):
        self.counter += 1
        t = tk.Toplevel(self)
        t.wm_title("Register")
        label = tk.Label(t, text="Enter account credentials: ")
        label.pack(side="top", fill="both", expand=True, padx=5, pady=5)
        ents= makeform(t,fields)
        t.bind('<Return>',(lambda event, e=ents: fetch(e)))

     	t.button=tk.Button(t,text="Quit", command=self.destroy)
	t.button.pack(side='right',padx=5,pady=5)

def logStat(arr):
    table= dict(arr)
    total= sum(map(Counter,table),Counter())
    N=float(len(table))
    avg={k: v/N for k, v in total.items()}
    with open('file.txt', 'w') as file:
     file.write(json.dumps(arr))


if __name__ == "__main__":
    root = tk.Tk()
    main = MainWindow(root)
    main.pack(side="top", fill="both", expand=True)
    root.mainloop()
    logStat(key_arr)
    os.system('xset r on')
