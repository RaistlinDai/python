'''
Created on Jun 26, 2018

@author: ftd
'''
from tkinter import *
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_bottom import Frame_bottom
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.base.FormatableFrame import FormatableFrame
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.base.UnFormatableFrame import UnFormatableFrame
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.base.Frame_constant import Frame_constant
from tkinter.messagebox import showerror
from src.main.pydev.com.ftd.generalutilities.metadata.service.fileproc.Java_processor import Java_processor
from src.main.pydev.com.ftd.generalutilities.metadata.service.base.File_constant import File_constant

class Frame_gene_selection(FormatableFrame):
    '''
    classdocs
    '''


    def __init__(self, parent=None, dtos=None, trans=None, **configs):
        '''
        Constructor
        '''
        #initialize
        self.__result = None
        self.__error = None
        self.__classlist = []       # 0:service interface, 1:factory interface, 2:qra service class, 3:qra factory class
                                    # 4:entity container interface, 5:entity container impl, 6:main table interface,
        FormatableFrame.__init__(self, parent.get_mainframe(), dtos, trans, **configs)
        
        
    #overwrite create_widges
    def create_widges(self):
        #frame
        self.__frame1 = FormatableFrame(self)
        self.__frame1.pack(side=TOP)
        #Title
        self.__label01 = Label(self.__frame1, text="Select the generated file", width= 45)
        self.__label01.pack(side=TOP, fill=X, ipady=10)
        
        frame_constant = Frame_constant()
        
        # get the Generator Status from transDTO
        java_flag = True
        gene_status = self.get_trans().get_generatorstatus()
        for key, value in gene_status.items():
            # disable the java generator
            if key == 'ImplJAR' and value[1].get() == 0:
                java_flag = False
            elif key == 'ApiJAR' and value[1].get() == 0:
                java_flag = False
                
        # load the jar and java first
        if not self.__load_jar_and_java():
            return
                
        #check buttons
        checkbut_frame1 = UnFormatableFrame(self)
        checkbut_frame1.pack(fill=X)
        Label(checkbut_frame1, text = 'Xml:', width=10).pack(side=LEFT)
        self.__checkvalues01 = {frame_constant.ENTITY_MAP_AND_BEAN_APP:IntVar()}
        for chkv in self.__checkvalues01.keys():
            chk1 = Checkbutton(checkbut_frame1, text = chkv, variable = self.__checkvalues01[chkv], onvalue = 1, offvalue = 0)
            chk1.pack(side=LEFT)
        
        checkbut_frame2 = UnFormatableFrame(self)
        checkbut_frame2.pack(fill=X)
        Label(checkbut_frame2, text = 'Java:', width=10).pack(side=LEFT)
        self.__checkvalues02 = {frame_constant.SERVICE_IMPL:IntVar(),
                                frame_constant.DATA_CONTROLLER:IntVar()}
        for chkv in self.__checkvalues02.keys():
            if java_flag:
                chk1 = Checkbutton(checkbut_frame2, text = chkv, variable = self.__checkvalues02[chkv], onvalue = 1, offvalue = 0)
            else:
                chk1 = Checkbutton(checkbut_frame2, text = chkv, variable = self.__checkvalues02[chkv], onvalue = 1, offvalue = 0, state=DISABLED)
            chk1.pack(side=LEFT)
            
        checkbut_frame3 = UnFormatableFrame(self)
        checkbut_frame3.pack(fill=X)
        Label(checkbut_frame3, text = 'TsHandler:', width=10).pack(side=LEFT)
        self.__checkvalues03 = {frame_constant.TS_CONSTANTS:IntVar(), 
                                frame_constant.MOCK_DTO:IntVar(), 
                                frame_constant.OBSERVABLE_OBJ:IntVar(), 
                                frame_constant.TS_HANDLER:IntVar() }
        for chkv in self.__checkvalues03.keys():
            chk1 = Checkbutton(checkbut_frame3, text = chkv, variable = self.__checkvalues03[chkv], onvalue = 1, offvalue = 0)
            chk1.pack(side=LEFT)
    
    
    #overwrite before_next
    def add_bottom(self, parent):
        #bottom frame
        exFuncs = {'Next':{'process':self.get_nextframe(), 'before':self.before_next},
                   'Prev':{'process':self.get_prevframe(), 'before':self.before_prev}}
        self.__buttom = Frame_bottom(parent, ['Next','Prev'], exFuncs)
        self.__buttom.pack(fill=X, ipady=10,side=BOTTOM)
        
    
    def before_next(self):
        '''
        overwrite the function in super class
        generating the next frames according to the selections
        '''
        #check box flag
        checkFlag = False
        selections = dict(self.__checkvalues01, **self.__checkvalues02, **self.__checkvalues03)
        
        for val in selections.values():
            if val.get() == 1:
                checkFlag = True
                break
                
        if checkFlag:
            #merge the selections into process flow
            self.get_trans().update_process_flow_by_gene_selection(selections)
            self.get_trans().print_processflow()
            return True
        else:
            showerror('Error', 'You must select at least one generation file!')
            return False
        
    
    def __load_jar_and_java(self):
        '''
        this method will load the info from imp & api jar, and will also load the serviceImpl and dataController java files
        '''
        #analysis the serviceImpl
        self.__result, self.__error, business_entity_name, self.__classlist = Java_processor.validate_lib_javas(self.get_trans(), self.get_dtos())
        # ---- set serviceImpl name
        if business_entity_name:
            self.get_dtos().set_businessentityname(business_entity_name)
        if not self.__result:
            #---- panel 02 ----------
            self.__pack_errorpanel()
            return False
        
        # --------- analysis the api service
        if not self.get_dtos().get_serviceInterDTO().get_class_name():
            self.__result, self.__error, serviceInterDTO = Java_processor.read_java_interface(self.__classlist[0])
            if not self.__result:
                #---- panel 02 ----------
                self.__pack_errorpanel()
                return False
            else:
                self.get_dtos().set_serviceInterDTO(serviceInterDTO)
        
        if not self.get_dtos().get_serviceQraDTO().get_class_name():
            self.__result, self.__error, serviceQraDTO = Java_processor.read_java_class(self.__classlist[2])
            if not self.__result:
                #---- panel 02 ----------
                self.__pack_errorpanel()
                return False
            else:
                self.get_dtos().set_serviceQraDTO(serviceQraDTO)
        
        # --------- analysis the factory
        if not self.get_dtos().get_factoryInterDTO().get_class_name():
            self.__result, self.__error, factoryInterDTO = Java_processor.read_java_interface(self.__classlist[1])
            if not self.__result:
                #---- panel 02 ----------
                self.__pack_errorpanel()
                return False
            else:
                self.get_dtos().set_factoryInterDTO(factoryInterDTO)
        
        if not self.get_dtos().get_factoryQraDTO().get_class_name():
            self.__result, self.__error, factoryQraDTO = Java_processor.read_java_class(self.__classlist[3])
            if not self.__result:
                #---- panel 02 ----------
                self.__pack_errorpanel()
                return False
            else:
                self.get_dtos().set_factoryQraDTO(factoryQraDTO)
            
        # --------- analysis the container
        if not self.get_dtos().get_entContInterDTO().get_class_name():
            self.__result, self.__error, containerInterDTO = Java_processor.read_java_interface(self.__classlist[4])
            if not self.__result:
                #---- panel 02 ----------
                self.__pack_errorpanel()
                return False
            else:
                self.get_dtos().set_entContInterDTO(containerInterDTO)
        
        if not self.get_dtos().get_entContQraDTO().get_class_name():
            self.__result, self.__error, containerQraDTO = Java_processor.read_java_class(self.__classlist[5])
            if not self.__result:
                #---- panel 02 ----------
                self.__pack_errorpanel()
                return False
            else:
                self.get_dtos().set_entContQraDTO(containerQraDTO)
        
        # --------- analysis the main table interface
        if not self.get_dtos().get_maintableInterDTO().get_class_name():
            self.__result, self.__error, maintableInterDTO = Java_processor.read_java_interface(self.__classlist[6])
            if not self.__result:
                #---- panel 02 ----------
                self.__pack_errorpanel()
                return False
            else:
                self.get_dtos().set_maintableInterDTO(maintableInterDTO)
        
        
        # --------- analysis the serviceImpl class
        fileconstant = File_constant()
        tempstr01, tempstr02, parent_pack, tempstr03 = Java_processor.analysis_jar_package_name(self.get_dtos().get_serviceInterDTO().get_class_package())
        
        if not self.get_dtos().get_serviceImplPath():
            serviceImpl_path = self.get_trans().get_projectpath() + fileconstant.JAVA_SERVICEIMPL_PATH % (parent_pack, business_entity_name + fileconstant.SERVICEIMPL_SUFFIX + fileconstant.JAVA_SUFFIX)
            self.__result, self.__error, dcJavaDTO = Java_processor.analysis_serviceImpl(business_entity_name + fileconstant.SERVICEIMPL_SUFFIX, serviceImpl_path, self.get_dtos())
            if not self.__result:
                #---- panel 02 ----------
                self.__pack_errorpanel()
                return
            else:
                self.get_dtos().set_serviceImplInfo(business_entity_name + fileconstant.SERVICEIMPL_SUFFIX + fileconstant.JAVA_SUFFIX, serviceImpl_path, dcJavaDTO)
            
        if not self.get_dtos().get_dataControllerPath():
            dataController_path = self.get_trans().get_projectpath() + fileconstant.JAVA_DATACONTROLLER_PATH % (parent_pack, business_entity_name + fileconstant.DATACONTROLLER_SUFFIX + fileconstant.JAVA_SUFFIX)
            self.__result, self.__error, dcJavaDTO = Java_processor.analysis_dataController(business_entity_name + fileconstant.DATACONTROLLER_SUFFIX, dataController_path, self.get_dtos())
            if not self.__result:
                #---- panel 02 ----------
                self.__pack_errorpanel()
                return
            else:
                self.get_dtos().set_dataControllerInfo(business_entity_name + fileconstant.DATACONTROLLER_SUFFIX + fileconstant.JAVA_SUFFIX, dataController_path, dcJavaDTO)

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