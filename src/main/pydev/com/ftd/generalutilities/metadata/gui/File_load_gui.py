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
        self.pack()
        
        self.createWidgets()
            
    
    def createWidgets(self):
        #label
        self.label01 = Label(None, {'text':'Select the project path:'})
        self.label01.pack(side=TOP)
        
        self.nameInput = Entry(self)
        self.nameInput.pack(fill=BOTH)
        
        self.popupButton = Button(self, text='Hello', command=(lambda: self.hello()))
        self.popupButton.pack()
        
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack(side=LEFT, expand=YES, fill=X)
    
    
    def hello(self):
        name = self.nameInput.get()
        if name == "":
            name = 'world'
            
        messagebox.showinfo('Message', 'Hello, %s' % name)
        