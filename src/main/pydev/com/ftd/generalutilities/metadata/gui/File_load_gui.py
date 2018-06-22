'''
Created on Jun 20, 2018

@author: ftd
'''
from tkinter import *
import tkinter.messagebox as messagebox

class File_load_gui(Frame):
    '''
    classdocs
    '''


    def __init__(self, master=None):
        '''
        Constructor
        '''
        Frame.__init__(self, master)
        
        #main window
        self.master.title('File loader')
        self.master.geometry('600x200')
        self.grid(column=0, row=0, sticky=(N,W,E,S))
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        #add children
        self.create_widgets()
        self.create_buttons()
        #layout maintain
        self.adjust_children()
        
        
    def create_widgets(self):
        
        feet = StringVar()

        #label1
        self.label01 = Label(self, text="Select or Input the project path:")
        self.label01.grid(column=0, row=1, sticky=(W,E))
        
        #input
        self.nameInput = Entry(self, width=40, textvariable=feet)
        self.nameInput.grid(column=1, row=1, sticky=(W,E))
        
        
    def create_buttons(self):
        #button
        self.popupButton = Button(self, text='Convert', command=(lambda: self.hello()))
        self.quitButton = Button(self, text='Quit', command=self.quit)
        
        self.popupButton.grid(column=3, row=3, sticky=(E,S))
        self.quitButton.grid(column=4, row=3, sticky=(E,S))
        
        
    def hello(self):
        name = self.nameInput.get()
        if name == "":
            name = 'world'
        
        messagebox.showinfo('Message', 'Hello, %s' % name)


    def adjust_children(self):
        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)
        self.nameInput.focus()
        