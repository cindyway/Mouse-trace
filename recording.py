# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 17:50:36 2020

@author: weixd5
"""
import pyautogui

from pynput import keyboard
from pynput import mouse

import time
from threading import Thread,Event
from subprocess import call

class Controller(object):
    def __init__(self):
        self.thread1 = None
#        self.thread2 = None
        self.stop_threads = Event()
    
    global is_start,fobj
    
    def start(self):
        global is_start,fobj
        self.stop_threads.clear()
        self.thread1 = Thread(target = self.listenall)
#        self.thread2 = Thread(target = self.loop2)
        self.thread1.start()
#        self.thread2.start()
#        is_start=True
#        listenall()
         
    def stop(self):
#        global is_start,fobj
        fobj.close() 
        self.stop_threads.set()
        self.thread1.join()
#        self.thread2.join()
        self.thread1 = None
#        self.thread2 = None
#        is_start=False
       
        
    #Monitor mouse action
    def on_move(self,x,y):
        global fobj
        fobj.writelines('move to  {0}'.format((x,y))+'\n')
    
    
    def on_click(self,x,y,button,pressed):
        global fobj
        if pressed:
            if button == mouse.Button.left:
                     fobj.writelines('{0} at  {1}'.format('left',(x,y))+'\n')
            elif button == mouse.Button.right:
                     fobj.writelines('{0} at  {1}'.format('right',(x,y))+'\n')
            elif button == mouse.Button.middle:
                     fobj.writelines('{0} at  {1}'.format('middle',(x,y))+'\n')
        else:
            fobj.writelines('{0} at  {1}'.format('release',(x,y))+'\n')
       # if not pressed:
       #     return False
    def on_scroll(self,x,y,dx,dy):
        global fobj
        fobj.writelines('scrolled {0} at  {1}'.format(
            'down' if dy <0 else 'up',
            (x,y))+'\n')
    
        
    def listenall(self):
        global is_start,fobj
        while not self.stop_threads.is_set():          
#           with open("log_.txt","w") as fobj:
            file_name = "log_.txt"
            fobj = open(file_name,  'w')
            with mouse.Listener(on_move=self.on_move,
                                    on_click=self.on_click,
                                    on_scroll=self.on_scroll) as listener:
                listener.join()

   





