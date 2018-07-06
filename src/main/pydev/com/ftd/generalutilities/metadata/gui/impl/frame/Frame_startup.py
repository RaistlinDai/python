'''
Created on Jul 6, 2018

@author: ftd
'''
from tkinter import *
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_bottom import Frame_bottom
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.base.FormatableFrame import FormatableFrame
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.button.Button_openfile import Button_openfile

class Frame_startup(FormatableFrame):
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
        self.__label01 = Label(self.__frame1, text="Hello world, let's rock", width= 45)
        self.__label01.pack(side=TOP, fill=X, ipady=10)
        
        #---- panel 01 ----------
        canv1 = Canvas(self, height=100, width=550)
        #label
        label1 = Label(canv1, text='Please select a processing pattern:')
        label1.place(height=20, width=200, relx=0.01, rely=0.05)
        #radio box
        self.__vari1 = IntVar()
        self.__rad1 = Radiobutton(canv1, text='Select files from project', variable=self.__vari1, value=1)
        self.__rad1.place(height=20, width=150, relx= 0.1, rely=0.4)
        self.__rad1.select()
        self.__rad2 = Radiobutton(canv1, text='Select files from metadata', variable=self.__vari1, value=2)
        self.__rad2.place(height=20, width=160, relx= 0.39, rely=0.4)
        self.__rad2.deselect()
        self.__rad3 = Radiobutton(canv1, text='Customize process flow', variable=self.__vari1, value=3)
        self.__rad3.place(height=20, width=150, relx= 0.7, rely=0.4)
        self.__rad3.deselect()
        canv1.pack()
        
        #---- panel 02 ----------
        canv2 = Canvas(self, height=100, width=550)
        #label
        label2 = Label(canv2, text='Please select a workspace folder:')
        label2.place(height=20, width=200, relx=0.01, rely=0.05)
        #input
        feet = StringVar()
        self.__dicinput = Entry(canv2, textvariable=feet, borderwidth=3, bg='black', foreground='yellow', highlightcolor='red', insertbackground='red')
        self.__dicinput.place(height=20, width=430, relx=0.1, rely=0.4)
        #button
        self.__dicload = Button_openfile(canv2, self.reset_dicinput, height=1)
        self.__dicload.place(height=20, width=20, relx=0.9, rely=0.4)
        #label
        label3 = Label(canv2, text='(This folder will be used for storing the backup files)', bg='white')
        label3.place(height=20, width=300, relx=0.1, rely=0.6)
        
        canv2.pack()
        
    
    #overwrite before_next
    def add_bottom(self, parent):
        #bottom frame
        exFuncs = {'Next':{'process':self.get_nextframe(), 'before':self.before_next}}
        self.__buttom = Frame_bottom(parent, ['Next'], exFuncs)
        self.__buttom.pack(fill=X, ipady=10,side=BOTTOM)
        
    
    def before_next(self):
        '''
        overwrite the function in super class
        generating the next frames according to the selections
        '''
        self.get_trans().update_process_flow_by_start_selection(self.__vari1.get())
        
        return True
    
    
    def reset_dicinput(self, dicname):
        self.__dicinput.delete(0, END)
        self.__dicinput.insert(END, dicname)