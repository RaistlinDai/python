'''
Created on Jun 23, 2018

@author: ftd
'''
from tkinter import *
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.FtdFrame import FtdFrame
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.button.Button_openfile import Button_openfile
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_bottom import Frame_bottom

class Frame_loaddir(FtdFrame):
    '''
    classdocs
    '''


    def __init__(self, parent=None, nextframe=None, **configs):
        '''
        Constructor
        '''
        #analysis parent viewForm
        FtdFrame.__init__(self, parent, nextframe, **configs)
        self.__frame1 = FtdFrame(self)
        self.__frame1.pack(side=TOP)
        #label1
        self.__label01 = Label(self.__frame1, text="Select or Input the project src path:")
        self.__label01.pack(side=TOP, fill=X)
        #input
        feet = StringVar()
        self.__dicinput = Entry(self.__frame1, width=50, textvariable=feet)
        self.__dicinput.pack(side=LEFT, fill=Y)
        #button
        self.__dicload = Button_openfile(self.__frame1, self.reset_dicinput, height=1)
        self.__dicload.pack(side=LEFT)
        #focus
        self.__dicinput.focus()
        
        #select result
        self.__frame2 = FtdFrame(self)
        self.__frame2.pack(fill=X)
        self.__label02 = Label(self.__frame2, text="Selected metadata: ")
        self.__label02.pack(side=LEFT, fill=X)
        
        #bottom
        self.add_bottom(self)
        
    
    def add_bottom(self, parent):
        #bottom frame
        exFuncs = {'Load':{'loadFunc':self.get_dicinput, 'setFunc':self.refresh_resultlabel},
                   'Next':self.nextframe}
        self.__buttom = Frame_bottom(parent, ['Next','Load'], exFuncs)
        self.__buttom.pack(fill=X)
        
    
    def reset_dicinput(self, dicname):
        self.__dicinput.delete(0, END)
        self.__dicinput.insert(END, dicname)
        
        
    def get_dicinput(self):
        return self.__dicinput.get()
        
    
    def refresh_resultlabel(self, filename):
        newname = "Selected metadata: " + filename
        self.__label02.config(text=newname)
        
        