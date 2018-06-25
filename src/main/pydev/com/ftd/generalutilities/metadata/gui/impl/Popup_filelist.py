'''
Created on Jun 23, 2018

@author: ftd
'''
from tkinter import *
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.Frame_selectbox import Frame_selectbox

class Popup_filelist(Toplevel):
    '''
    classdocs
    '''


    def __init__(self, filelists, parent=None, **configs):
        '''
        Constructor
        '''
        Toplevel.__init__(self, parent, **configs)
        
        self.title('File lsit')
        #self.geometry('300x500')
        self.resizable(width=False, height=False)
        
        row = Frame(self)
        lab = Label(row, width=15, text='Metadata list:')
        
        row.pack(side=TOP, fill=X)
        lab.pack(side=LEFT)
        
        #listbox and scrolbar
        body = Frame(self)
        body.pack(fill=BOTH)
        ls = Listbox(body)
        sb = Scrollbar(body)
        ls.config(yscrollcommand = sb.set)
        sb.pack(side=RIGHT, fill=Y)
        
        for name in filelists:
            ls.insert(0, name)
        
        sb.config(command = ls.yview)
        ls.pack(side=LEFT)
        
        #bottom frame
        bot = Frame(self)
        bot.pack(side=BOTTOM, fill=X)
        btn = Button(bot, text='OK', command=self.ok_callback)
        btn.pack(side=RIGHT)
        
    
    def show(self):
        self.destroy()
        
        
    def ok_callback(self):
        pass