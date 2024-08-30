#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk

# from six.moves import tkinter as tk

# root = tk.Tk()
# root.mainloop()
 1

class ClassName(object):
    def __init__(self,):
        super(ClassName, self).__init__()
        self.root = Tk()
        
    def quit(self):
        self.bsalir = ttk.Button
        (root, text='Salir',command=root.destroy)



def Aplicacion():
        c
        # self.root.geometry('600x400')
        # self.binfo.focus_set()
        root.title('Named Windows')
        bsalir = ttk.Button(root, text='Salir',command=root.destroy)
                         
        # Coloca el botón 'self.bsalir' a la derecha del 
        # objeto anterior.
                                 
        bsalir.pack(side=RIGHT)
        root.mainloop()

def main():
    app = Aplicacion()
    return 0
    # pass


if __name__ == '__main__':
   main()