# -*- coding: utf-8 -*-
"""
Created on Sat Jun 27 23:05:42 2020

@author: weixd5
"""
from tkinter import *
import tkinter.filedialog
from tkinter.filedialog import askopenfilename

import pyautogui

from pynput.mouse import Button,Controller
# =============================================================================
# def xz():
#     filename = tkinter.filedialog.askopenfilename()
#     if filename != '':
#         lb.config(text = "The files you choose is"+filename);
#         else:
#             lb.config(text = "You don't choose any file");
# =============================================================================

def play():  
#    mouse=Controller()  
    filename = askopenfilename()
    fo = open(filename, "r")
    for line in fo.readlines():                        
        line = line.strip().split('  ')
        a,b=map(float,line[1].strip('()').split(','))
        if line[0]=='move to':
            pyautogui.moveTo(a, b,duration=0.05)
        elif line[0]=='left at':
            pyautogui.moveTo(a, b,duration=0.05)
            pyautogui.click(a, b, 1, 0.25, button='left')
        elif line[0]=='right at':
            pyautogui.moveTo(a, b,duration=0.1)
            pyautogui.click(a, b, 1, 0.25, button='right')
    #    elif line[0]=='release at':
 #           mouse.move(x,y)
            #mouse.release(Button.left)
        elif line[0]=='scrolled up at':
            pyautogui.scroll(120, x=a, y=b)
        elif line[0]=='scrolled down at':
            pyautogui.scroll(-120, x=a, y=b)
     
    # 关闭文件
    fo.close()
      
