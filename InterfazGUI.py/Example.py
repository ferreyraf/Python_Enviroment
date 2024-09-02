#!/usr/bin/env python
# -*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk

# from six.moves import tkinter as tk

# class Aplicacion(object):
#     def __init__(self,):
#         super(Aplicacion, self).__init__()
#         self.root = Tk()
        
#     def quit(self):
#         self.bsalir = ttk.Button(root, text='Salir',command=root.destroy)



def Aplicacion():
        # self.root.geometry('600x400')
        # self.binfo.focus_set()
        root = Tk()
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