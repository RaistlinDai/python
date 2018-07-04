'''
Created on Jun 23, 2018

@author: ftd
'''
from tkinter import *
from tkinter.messagebox import showwarning

class Popup_filelist(Toplevel):
    '''
    classdocs
    '''


    def __init__(self, filelists, parent=None, **configs):
        '''
        Constructor
        '''
        Toplevel.__init__(self, parent, **configs)
        self.title('File list')
        
        #default parameters
        self.__curselection = None
        
        #forbidden resize
        self.resizable(width=False, height=False)
        
        #top label
        self.__top = Frame(self)
        self.__label = Label(self.__top, width=15, text='Metadata list:')
        self.__top.pack(side=TOP, fill=X)
        self.__label.pack(side=LEFT)
        
        #listbox and scrollbar
        body = Frame(self)
        body.pack(fill=BOTH)
        self.__listbox = Listbox(body, width=30)
        self.__scroll = Scrollbar(body)
        self.__listbox.config(yscrollcommand = self.__scroll.set)
        self.__scroll.pack(side=RIGHT, fill=Y)
        self.__scroll.config(command = self.__listbox.yview)
        self.__listbox.pack(side=LEFT)
        self.__filelists = filelists
        for name in filelists.keys():
            self.__listbox.insert(0, name)
            
        #bottom frame
        self.__bottom = Frame(self)
        self.__bottom.pack(side=BOTTOM, fill=X)
        self.__button = Button(self.__bottom, text='OK', command=self.ok_callback)
        self.__button.pack(side=RIGHT)
        
    
    def show(self):
        self.destroy()
        
        
    def ok_callback(self):
        if self.__listbox.curselection():
            selection = self.__listbox.selection_get()
            #the dict.items() will convert to tuple
            for tup in self.__filelists.items():
                if tup[0] == selection:
                    self.__curselection = tup
            self.destroy()
        else:
            showwarning('Warning', 'Please select a metadata file.')
    
    
    def return_selection(self):
        if self.__curselection:
            return self.__curselection
        else:
            return None
    
    