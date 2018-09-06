'''
Created on Jun 26, 2018

@author: ftd
'''
from tkinter import *
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_bottom import Frame_bottom
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.base.FormatableFrame import FormatableFrame
from src.main.pydev.com.ftd.generalutilities.metadata.service.base.File_constant import File_constant
from tkinter.messagebox import showwarning, showerror
from src.main.pydev.com.ftd.generalutilities.metadata.service.fileproc.Java_processor import Java_processor
from src.main.pydev.com.ftd.generalutilities.metadata.service.base.Java_constant import Java_constant

class Frame_serviceimpl_option(FormatableFrame):
    '''
    classdocs
    '''


    def __init__(self, parent=None, dtos=None, trans=None, **configs):
        '''
        Constructor
        '''
        self.__result = None
        self.__error = None
        self.__funclists = {}       #functions list backup
        FormatableFrame.__init__(self, parent.get_mainframe(), dtos, trans, **configs)
        
        
    #overwrite create_widges
    def create_widges(self):
        javaconstant = Java_constant()
        #frame
        self.__frame1 = FormatableFrame(self)
        self.__frame1.pack(side=TOP)
        #Title
        self.__label01 = Label(self.__frame1, text="ServiceImpl generator options", width= 45)
        self.__label01.pack(side=TOP, fill=X, ipady=10)
        
        #---- java validation flag
        self.__error = None
        self.__result = True
        
        #---- panel 01 ----------
        canv1 = Canvas(self, height=30, width=550)
        #label
        self.__label01 = Label(canv1, text='ServiceImpl name :')
        self.__label01.place(height=20, width=130, relx=0.03, rely=0.2)
        #input
        self.__feet = StringVar()
        self.__dicinput = Entry(canv1, textvariable=self.__feet, borderwidth=3, bg='black', foreground='yellow', highlightcolor='red', insertbackground='red')
        self.__dicinput.place(height=20, width=250, relx=0.3, rely=0.2)
        
        canv1.pack()
        
        #---- panel 02 ----------
        serviceInterDTO = self.get_dtos().get_serviceInterDTO()
        if not serviceInterDTO:
            self.__pack_errorpanel()
            return
        
        canv2 = Canvas(self, height=150, width=550)
        #label01
        self.__label01 = Label(canv2, text='Select the functions :')
        self.__label01.place(height=20, width=150, relx=0.01, rely=0.05)
        #left listbox and scrollbar
        self.__listboxleft = Listbox(canv2, width=30)
        self.__scrollleft = Scrollbar(canv2)
        self.__listboxleft.config(yscrollcommand = self.__scrollleft.set)
        self.__listboxleft.place(height=120, width=220, relx=0.02, rely=0.18)
        self.__scrollleft.place(height=120, width=20, relx=0.42, rely=0.18)
        self.__scrollleft.config(command = self.__listboxleft.yview)
        
        #middle buttons
        self.__button01 = Button(canv2, text='>', relief=RAISED, cursor='hand2')
        self.__button01.bind('<Button-1>', self.__to_right_click_event) #bind button click event
        self.__button01.place(height=25, width=25, relx=0.465, rely=0.2)
        
        self.__button02 = Button(canv2, text='>>', relief=RAISED, cursor='hand2')
        self.__button02.bind('<Button-1>', self.__all_to_right_click_event) #bind button click event
        self.__button02.place(height=25, width=25, relx=0.465, rely=0.4)
        
        self.__button03 = Button(canv2, text='<', relief=RAISED, cursor='hand2')
        self.__button03.bind('<Button-1>', self.__to_left_click_event) #bind button click event
        self.__button03.place(height=25, width=25, relx=0.465, rely=0.6)
        
        self.__button04 = Button(canv2, text='<<', relief=RAISED, cursor='hand2')
        self.__button04.bind('<Button-1>', self.__all_to_left_click_event) #bind button click event
        self.__button04.place(height=25, width=25, relx=0.465, rely=0.8)
        
        #right listbox and scrollbar
        self.__listboxright = Listbox(canv2, width=30)
        self.__scrollright = Scrollbar(canv2)
        self.__listboxright.config(yscrollcommand = self.__scrollright.set)
        self.__listboxright.place(height=120, width=220, relx=0.52, rely=0.18)
        self.__scrollright.place(height=120, width=20, relx=0.92, rely=0.18)
        self.__scrollright.config(command = self.__listboxright.yview)
    
        canv2.pack()
        
        #---- panel 03 ----------
        canv3 = Canvas(self, height=100, width=550)
        #label
        label1 = Label(canv3, text='Options:')
        label1.place(height=20, width=60, relx= 0, rely=0)
        #radio box
        self.__vari1 = IntVar()
        self.__rad1 = Radiobutton(canv3, text='Re-write the previous file', variable=self.__vari1, value=1)
        self.__rad1.place(height=20, width=170, relx= 0.1, rely=0.2)
        self.__rad1.select()
        self.__rad2 = Radiobutton(canv3, text='Attach new functions to the file', variable=self.__vari1, value=2)
        self.__rad2.place(height=20, width=210, relx= 0.1, rely=0.45)
        self.__rad2.deselect()
        self.__rad3 = Radiobutton(canv3, text='Save the previous file as backup', variable=self.__vari1, value=3)
        self.__rad3.place(height=20, width=220, relx= 0.1, rely=0.7)
        self.__rad3.deselect()
        canv3.pack()

        # set the serviceImpl name
        fileconstant = File_constant()
        serviceImpl_name = self.get_dtos().get_businessentityname() + fileconstant.SERVICEIMPL_SUFFIX + fileconstant.JAVA_SUFFIX
        self.__feet.set(serviceImpl_name)

        #set the function list to the left box
        for javaMtd in serviceInterDTO.get_class_methods():
            self.__funclists[javaMtd.get_method_name()] = javaMtd
            
            # CRUD functions are mandatory
            if javaMtd.get_method_name() == javaconstant.JAVA_FUNCTION_CREATE or javaMtd.get_method_name() == javaconstant.JAVA_FUNCTION_UPDATE or javaMtd.get_method_name() == javaconstant.JAVA_FUNCTION_DELETE or javaMtd.get_method_name() == javaconstant.JAVA_FUNCTION_FETCH:
                self.__listboxright.insert(END, javaMtd.get_method_name())
                continue
                
            #add items into list box
            self.__listboxleft.insert(END, javaMtd.get_method_name())
        
    
    #overwrite create_widges
    def add_bottom(self, parent):
        #bottom frame
        exFuncs = {'Next':{'process':self.get_nextframe(), 'before':self.before_next},
                   'Prev':{'process':self.get_prevframe(), 'before':self.before_prev}}
        self.__buttom = Frame_bottom(parent, ['Next','Prev'], exFuncs)
        self.__buttom.pack(fill=X, ipady=10,side=BOTTOM)
        
    
    def before_next(self):
        '''
        overwrite the function in super class
        verify the input directory
        '''
        if not self.__result:
            showwarning('Warning', 'There are error existing, the ServiceImpl cannot be generated.')
            return
        
        # write serviceImpl
        result, message, filefullpath, javaDTO = Java_processor.create_serviceImpl(self.__feet.get(), self.get_trans(), self.get_dtos(), self.__listboxright.get(0, END), self.__vari1.get())
        if not result:
            showerror('Error', message)
            return False
        
        # store the serviceImpl full path
        self.get_dtos().set_serviceImplInfo(self.__feet.get(), filefullpath, javaDTO)
        return True
        
        
    def __pack_errorpanel(self):
        '''
        pack the error panel
        '''
        canv2 = Canvas(self, height=50, width=550)
        #label01
        self.__label01 = Label(canv2, text=self.__error, fg='red')
        self.__label01.place(height=40, width=500, relx=0.01, rely=0.05)     
        canv2.pack()
    
    
    def __to_right_click_event(self, event):
        '''
        move the selection to the right list box
        '''
        if not self.__listboxleft or self.__listboxleft.size() == 0:
            return
        
        select_item = None
        if len(self.__listboxleft.curselection()) > 0:
            selection = self.__listboxleft.selection_get()
            #the dict.items() will convert to tuple
            for tup in self.__funclists.items():
                if tup[0] == selection:
                    select_item = tup
                    break
        
        if select_item:
            #add into right
            self.__listboxright.insert(END, select_item[0])
            select_idx = self.__listboxleft.curselection()
            #remove from left
            self.__listboxleft.delete(select_idx[0])
            
    
    def __all_to_right_click_event(self, event):
        '''
        move all items to the right list box
        '''
        select_items = []
        if len(self.__listboxleft.get(0, END)) > 0:
            for select_item in self.__listboxleft.get(0, END):
                select_items.append(select_item)
            self.__listboxleft.delete(0, END)
            
            for select_item in select_items:
                #add into right
                self.__listboxright.insert(END, select_item)
        
    
    def __to_left_click_event(self, event):
        '''
        move the selection to the left list box
        '''
        javaconstant = Java_constant()
        if not self.__listboxright or self.__listboxright.size() == 0:
            return
        
        select_item = None
        if len(self.__listboxright.curselection()) > 0:
            selection = self.__listboxright.selection_get()
            #the dict.items() will convert to tuple
            idx = 0
            for tup in self.__funclists.items():
                if tup[0] == selection:
                    if selection == javaconstant.JAVA_FUNCTION_CREATE or selection == javaconstant.JAVA_FUNCTION_UPDATE or selection == javaconstant.JAVA_FUNCTION_DELETE or selection == javaconstant.JAVA_FUNCTION_FETCH:
                        return
                    select_item = tup
                    break
                idx = idx + 1
        
        if select_item:
            #add into left
            self.__listboxleft.insert(idx, select_item[0])
            select_idx = self.__listboxright.curselection()
            #remove from right
            self.__listboxright.delete(select_idx[0])
            
    
    def __all_to_left_click_event(self, event):
        '''
        move all items to the right list box
        '''
        javaconstant = Java_constant()
        select_items = []
        if len(self.__listboxright.get(0, END)) > 0:
            crud_nbr = 0
            for select_item in self.__listboxright.get(0, END):
                if select_item == javaconstant.JAVA_FUNCTION_CREATE or select_item == javaconstant.JAVA_FUNCTION_UPDATE or select_item == javaconstant.JAVA_FUNCTION_DELETE or select_item == javaconstant.JAVA_FUNCTION_FETCH:
                    crud_nbr = crud_nbr + 1
                    continue
                select_items.append(select_item)
            self.__listboxright.delete(crud_nbr, END)
            
            for select_item in select_items:
                #add into right
                self.__listboxleft.insert(END, select_item)