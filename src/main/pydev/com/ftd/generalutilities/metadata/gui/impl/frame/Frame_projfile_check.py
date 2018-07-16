'''
Created on Jul 16, 2018

@author: ftd
'''
from tkinter import *
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_bottom import Frame_bottom
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.base.FormatableFrame import FormatableFrame

class Frame_projfile_check(FormatableFrame):
    '''
    classdocs
    '''


    def __init__(self, parent=None, dtos=None, trans=None, **configs):
        '''
        Constructor
        '''
        FormatableFrame.__init__(self, parent.get_mainframe(), dtos, trans, **configs)
        
        
    #overwrite create_widges
    def create_widges(self):
        #frame
        self.__frame1 = FormatableFrame(self)
        self.__frame1.pack(side=TOP)
        #Title
        self.__label01 = Label(self.__frame1, text="Project file checking", width= 45)
        self.__label01.pack(side=TOP, fill=X, ipady=10)
        
        #---- panel 01 ----------
        canv1 = Canvas(self, height=80, width=550)
        #label
        self.__label02 = Label(canv1, text='Metadata xml checking:')
        self.__label02.place(height=20, width=200, relx=0.01, rely=0.05)
        #selected details
        self.__checkval01 = IntVar()
        self.__checkbox01 = Checkbutton(canv1, text = "View metadata", variable = self.__checkval01, onvalue = 1, offvalue = 0, state=DISABLED)
        self.__checkbox01.place(height=20, width=110, relx=0.1, rely=0.35)
        self.__label03 = Label(canv1, text='Status :')
        self.__label03.place(height=20, width=60, relx=0.4, rely=0.33)
        self.__label04 = Label(canv1, text='< No-need >')
        self.__label04.place(height=20, width=120, relx=0.5, rely=0.33)
        self.__button01 = Button(canv1, text="Detail")
        self.__button01.place(height=20, width=50, relx=0.8, rely=0.33)
        
        self.__checkval02 = IntVar()
        self.__checkbox02 = Checkbutton(canv1, text = "Resource metadata", variable = self.__checkval02, onvalue = 1, offvalue = 0, state=DISABLED)
        self.__checkbox02.place(height=20, width=130, relx=0.1, rely=0.65)
        self.__label05 = Label(canv1, text='Status :')
        self.__label05.place(height=20, width=60, relx=0.4, rely=0.65)
        self.__label06 = Label(canv1, text='< No-need >')
        self.__label06.place(height=20, width=120, relx=0.5, rely=0.65)
        self.__button02 = Button(canv1, text="Detail")
        self.__button02.place(height=20, width=50, relx=0.8, rely=0.63)
        
        canv1.pack()
        
        #---- panel 02 ----------
        canv2 = Canvas(self, height=80, width=550)
        #labe2
        label2 = Label(canv2, text='Jar checking:')
        label2.place(height=20, width=200, relx=0.01, rely=0.05)
        
        self.__checkval03 = IntVar()
        self.__checkbox03 = Checkbutton(canv2, text = "financials-impl", variable = self.__checkval03, onvalue = 1, offvalue = 0, state=DISABLED)
        self.__checkbox03.place(height=20, width=110, relx=0.1, rely=0.35)
        self.__label07 = Label(canv2, text='Status :')
        self.__label07.place(height=20, width=60, relx=0.4, rely=0.35)
        self.__label08 = Label(canv2, text='< No-need >')
        self.__label08.place(height=20, width=120, relx=0.5, rely=0.35)
        self.__button03 = Button(canv2, text="Detail")
        self.__button03.place(height=20, width=50, relx=0.8, rely=0.35)
        
        canv2.pack()
        
        #--- initialize
        self.initial_value()
    
    
    #overwrite create_widges
    def add_bottom(self, parent):
        #bottom frame
        exFuncs = {'Next':{'process':self.get_nextframe(), 'before':self.before_next},
                   'Prev':{'process':self.get_prevframe(), 'before':self.before_prev}}
        self.__buttom = Frame_bottom(parent, ['Next','Prev'], exFuncs)
        self.__buttom.pack(fill=X, ipady=10,side=BOTTOM)
        
        
    def initial_value(self):
        print(self.get_trans().get_prev_process())
        
