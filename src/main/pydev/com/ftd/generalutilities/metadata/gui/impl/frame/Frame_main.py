'''
Created on Jun 26, 2018

@author: ftd
'''
from tkinter import Frame
from tkinter.messagebox import askyesno

class Frame_main(Frame):
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
        self.master.geometry('600x300')
        self.master.resizable(width=False, height=False)
        #font
        self.labelfont = ('times', 15, 'bold')
        self.pack()
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        #closing event
        self.master.protocol("WM_DELETE_WINDOW", self.on_closing)
        
        
    def on_closing(self):
        if askyesno("Quit", 'Do you want to quit?'):
            self.quit()