'''
Created on Jun 26, 2018

@author: ftd
'''
from tkinter import *
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_bottom import Frame_bottom
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_checkbox import Frame_checkbox
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.base.FormatableFrame import FormatableFrame

class Frame_maintgene(FormatableFrame):
    '''
    classdocs
    '''


    def __init__(self, parent=None, nextframe=None, **configs):
        '''
        Constructor
        '''
        FormatableFrame.__init__(self, parent, nextframe)
        self.__frame1 = FormatableFrame(self)
        self.__frame1.pack(side=TOP)
        #Title
        self.__label01 = Label(self.__frame1, text="Select the generated file", width= 45)
        self.__label01.pack(side=TOP, fill=X, ipady=10)
        #check buttons
        checkbut_frame1 = Frame_checkbox(self)
        checkbut_frame1.pack(fill=X)
        CheckVar1 = IntVar()
        CheckVar2 = IntVar()
        CheckVar3 = IntVar()
        CheckVar4 = IntVar()
        chk1 = Checkbutton(checkbut_frame1, text = "Constants", variable = CheckVar1, onvalue = 1, offvalue = 0)
        chk1.pack(side=LEFT)
        chk2 = Checkbutton(checkbut_frame1, text = "TSHandler", variable = CheckVar2, onvalue = 2, offvalue = 0)
        chk2.pack(side=LEFT)
        chk3 = Checkbutton(checkbut_frame1, text = "MockDTO", variable = CheckVar3, onvalue = 3, offvalue = 0)
        chk3.pack(side=LEFT)
        chk4 = Checkbutton(checkbut_frame1, text = "ObservableObj", variable = CheckVar4, onvalue = 4, offvalue = 0)
        chk4.pack(side=LEFT)
        
        #bottom
        self.add_bottom(self)
    
        #format
        self.adjust_children(parent)
        
    
    def add_bottom(self, parent):
        #bottom frame
        exFuncs = {'Next':None,
                   'Prev':None}
        self.__buttom = Frame_bottom(self, ['Next','Prev'], exFuncs)
        self.__buttom.pack(fill=X, ipady=10)
        
        