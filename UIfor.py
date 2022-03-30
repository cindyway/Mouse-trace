# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 20:30:57 2020

@author: weixd5
"""
import recording
import playing

import pynput
from tkinter import *
import threading
import time

def thread_it(func,*args):
    t=threading.Thread(target=func,args=args)
    t.setDaemon(True)
    t.start()
    
    
root=Tk()
root.title("Monitor v1")
root.geometry("68x480")
control = recording.Controller()
#th = threading.Thread(target=control.start, args=(10,))
b1=Button(root,text="Record",bd=1,width=10,
           command=control.start).pack()
b2=Button(root,text="Play",bd=2,
          command=lambda:thread_it(playing.play),width=10).pack()
b3=Button(root,text="Stop Record",bd=3,width=10,
           command=lambda:thread_it(control.stop)).pack()
root.mainloop()

#command=lambda :thread_it(recording.start)).pack()