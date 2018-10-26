'''
Created on Jun 27, 2018

@author: ftd
'''
from tkinter import *
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_bottom import Frame_bottom
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.base.FormatableFrame import FormatableFrame
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.base.Frame_constant import Frame_constant

class Frame_ts_handler_option(FormatableFrame):
    '''
    classdocs
    '''


    def __init__(self, parent=None, dtos=None, trans=None, **configs):
        '''
        Constructor
        '''
        self.__result = True
        self.__error = None
        
        FormatableFrame.__init__(self, parent.get_mainframe(), dtos, trans, **configs)
        
    
    #overwrite create_widges
    def create_widges(self):
        
        frame_constant = Frame_constant()
        
        #frame
        self.__frame1 = FormatableFrame(self)
        self.__frame1.pack(side=TOP)
        #Title
        self.__label01 = Label(self.__frame1, text="TS Handler generator options", width= 45)
        self.__label01.pack(side=TOP, fill=X, ipady=10)
        
        #---- panel 01 ----------
        canv1 = Canvas(self, height=30, width=550)
        Label(canv1, text = 'Please select the generated TS:', width=30).pack()
        self.__checkvalues01 = {frame_constant.TS_HANDLER_MAINT:IntVar(), 
                                frame_constant.TS_HANDLER_VIEWFORM:IntVar(), 
                                frame_constant.TS_HANDLER_GRID:IntVar(), 
                                frame_constant.TS_HANDLER_COMMON:IntVar() }
        for chkv in self.__checkvalues01.keys():
            chk1 = Checkbutton(canv1, text = chkv, variable = self.__checkvalues01[chkv], onvalue = 1, offvalue = 0)
            chk1.pack(side=LEFT)
        
        canv1.pack()
    
     
    #overwrite create_widges   
    def add_bottom(self, parent):
        #bottom frame
        exFuncs = {'Next':{'process':self.get_nextframe(), 'before':self.before_next},
                   'Prev':None}
        self.__buttom = Frame_bottom(parent, ['Next','Prev'], exFuncs)
        self.__buttom.pack(fill=X, ipady=10,side=BOTTOM)