'''
Created on Jun 23, 2018

@author: ftd
'''
from tkinter import *
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.button.Button_openfile import Button_openfile
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_bottom import Frame_bottom
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.base.FormatableFrame import FormatableFrame
from tkinter.messagebox import showerror
from src.main.pydev.com.ftd.generalutilities.metadata.service.FileConstant import FileConstant

class Frame_loaddir(FormatableFrame):
    '''
    classdocs
    '''


    def __init__(self, parent=None, nextframe=None, dtos=None, **configs):
        '''
        Constructor
        '''
        #analysis parent viewForm
        FormatableFrame.__init__(self, parent.get_mainframe(), nextframe, dtos, **configs)
                
    
    #overwrite create_widges
    def create_widges(self):
        #frame
        self.__frame1 = FormatableFrame(self)
        self.__frame1.pack(side=TOP)
        #title
        self.__label01 = Label(self.__frame1, text="Select or Input the project src path:", width= 45)
        self.__label01.pack(side=TOP, fill=X, ipady=10)
        #input
        feet = StringVar()
        self.__dicinput = Entry(self.__frame1, textvariable=feet)
        self.__dicinput.pack(side=LEFT, fill=BOTH, expand=1)
        #button
        self.__dicload = Button_openfile(self.__frame1, self.reset_dicinput, height=1)
        self.__dicload.pack(side=LEFT)
        #focus
        self.__dicinput.focus()
        
        #select result
        self.__frame2 = FormatableFrame(self)
        self.__frame2.pack(fill=X)
        self.__label02 = Label(self.__frame2, text="Selected metadata: ")
        self.__label02.pack(side=LEFT, fill=X)
        
    
    #overwrite create_widges
    def add_bottom(self, parent):
        #bottom frame
        exFuncs = {'Load':{'loadFunc':self.get_dicinput, 'setFunc':self.get_selection},
                   'Next':{'process':self.get_nextframe(), 'before':self.before_next}}
        self.__buttom = Frame_bottom(parent, ['Next','Load'], exFuncs)
        self.__buttom.pack(side=BOTTOM, fill=X, ipady=10)
        
    
    def reset_dicinput(self, dicname):
        self.__dicinput.delete(0, END)
        self.__dicinput.insert(END, dicname)
        
        
    def get_dicinput(self):
        return self.__dicinput.get()
        
    
    def get_selection(self, fileinfo):
        #path constant
        fileconstant = FileConstant(self)
        #update label
        if isinstance(fileinfo, tuple):
            filename = fileinfo[0]
            fullpath = fileinfo[1]
        else:
            filename = fileinfo
            fullpath = self.__dicinput.get() + fileconstant.viewmetadata_path + filename
        newname = "Selected metadata: " + filename
        self.__label02.config(text=newname)
        #set the entity name and full path in dto set
        self.get_dtos().set_entityname(filename)
        self.get_dtos().set_fullpath(fullpath)
    
    
    def before_next(self):
        if self.__dicinput.get():
            return True
        else:
            showerror('Error', 'You must select an existing metadata!')
            return False