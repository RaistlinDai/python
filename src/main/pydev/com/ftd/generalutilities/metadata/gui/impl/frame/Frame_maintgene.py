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
        FormatableFrame.__init__(self, parent.get_mainframe(), nextframe)
        self.__frame1 = FormatableFrame(self)
        self.__frame1.pack(side=TOP)
        #Title
        self.__label01 = Label(self.__frame1, text="Select the generated file", width= 45)
        self.__label01.pack(side=TOP, fill=X, ipady=10)
        #check buttons
        checkbut_frame1 = Frame_checkbox(self)
        checkbut_frame1.pack(fill=X)
        self.__checkvalues = {"Constants":IntVar(), "TSHandler":IntVar(), "MockDTO":IntVar(), "ObservableObj":IntVar() }
        for chkv in self.__checkvalues.keys():
            chk1 = Checkbutton(checkbut_frame1, text = chkv, variable = self.__checkvalues[chkv], onvalue = 1, offvalue = 0)
            chk1.pack(side=LEFT)
        
        #bottom
        self.add_bottom(self)
    
        #format
        self.adjust_children(parent.get_mainframe())
        
    
    def add_bottom(self, parent):
        #bottom frame
        exFuncs = {'Next':self.get_checkbuttons,
                   'Prev':None}
        self.__buttom = Frame_bottom(self, ['Next','Prev'], exFuncs)
        self.__buttom.pack(fill=X, ipady=10)
    
    
    def get_checkbuttons(self):
        for ck in self.__checkvalues.keys():
            print(ck + ":" + str(self.__checkvalues[ck].get()))
        