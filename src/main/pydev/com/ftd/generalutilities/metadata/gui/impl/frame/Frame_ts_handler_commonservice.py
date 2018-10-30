'''
Created on Jun 27, 2018

@author: ftd
'''
from tkinter import *
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_bottom import Frame_bottom
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.base.FormatableFrame import FormatableFrame
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.base.Frame_constant import Frame_constant
from src.main.pydev.com.ftd.generalutilities.metadata.service.base.File_constant import File_constant
from tkinter.messagebox import showwarning, showerror
from src.main.pydev.com.ftd.generalutilities.metadata.service.fileproc.TS_processor import TS_processor
from src.main.pydev.com.ftd.generalutilities.metadata.service.base.File_processor import File_processor

class Frame_ts_handler_commonservice(FormatableFrame):
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
        fileconstant = File_constant()
        
        #frame
        self.__frame1 = FormatableFrame(self)
        self.__frame1.pack(side=TOP)
        #Title
        self.__label01 = Label(self.__frame1, text="TS CommonService generator options", width= 45)
        self.__label01.pack(side=TOP, fill=X, ipady=10)
        
        #---- panel 01 ----------
        canv1 = Canvas(self, height=30, width=550)
        #label
        self.__label01 = Label(canv1, text='CommonService name :')
        self.__label01.place(height=20, width=130, relx=0.03, rely=0.2)
        #input
        self.__feet = StringVar()
        self.__dicinput = Entry(canv1, textvariable=self.__feet, borderwidth=3, bg='black', foreground='yellow', highlightcolor='red', insertbackground='red')
        self.__dicinput.place(height=20, width=250, relx=0.3, rely=0.2)
        canv1.pack()
        
        #---- panel 02 ----------
        canv2 = Canvas(self, height=100, width=550)
        self.__label02 = Label(canv2, text = 'Please select the imports:', width=30)
        self.__label02.place(height=20, width=200, relx=0.05, rely=0.02)
        canv2.pack()
        
        # TODO: add import options: constant, MockDTO
        
        #---- panel 03 ----------
        canv3 = Canvas(self, height=150, width=550)
        self.__label03 = Label(canv3, text = 'Please select the contents:', width=30)
        self.__label03.place(height=20, width=200, relx=0.05, rely=0.02)
        
        canv3.pack()
        
        if self.get_dtos().get_businessentityname():
            # get the mock ds name
            mock_ds_name = self.get_dtos().get_businessentityname() + fileconstant.TS_COMMON_SERVICE_SUFFIX + fileconstant.TS_SUFFIX
            self.__feet.set(mock_ds_name)
        
     
    #overwrite create_widges   
    def add_bottom(self, parent):
        #bottom frame
        exFuncs = {'Next':{'process':self.get_nextframe(), 'before':self.before_next},
                   'Prev':None}
        self.__buttom = Frame_bottom(parent, ['Next','Prev'], exFuncs)
        self.__buttom.pack(fill=X, ipady=10,side=BOTTOM)
        
    
    def before_next(self):
        '''
        overwrite the function in super class
        verify the input directory
        '''
        if not self.__result:
            showwarning('Warning', 'There are error existing, the CommonService cannot be generated.')
            return
        
        # --------------------- analysis the DTO if needed --------------------- #
        if not self.get_dtos().get_tsdtos() or not self.get_dtos().get_tsdto_value('TSDtoDTO'):
            #path constant
            fileconstant = File_constant()
            proj_path = self.get_trans().get_projectpath()
            # get the main table interface name
            main_tb_name = self.get_dtos().get_maintableInterDTO().get_class_name()
            # get the generated ds name
            gene_ds_name = fileconstant.TS_DATASET_PREFIX + main_tb_name + fileconstant.TS_SUFFIX
            # get the generated ds full path
            gene_ds_filefullpath = proj_path + fileconstant.RESOURCE_TS_MAIN_PATH + fileconstant.RESOURCE_TS_DTO_BL_FOLDER + gene_ds_name
            # get the mock ds full path
            mock_ds_filefullpath = proj_path + fileconstant.RESOURCE_TS_MAIN_PATH + fileconstant.RESOURCE_TS_DTO_UI_FOLDER + gene_ds_name.replace(fileconstant.TS_SUFFIX, fileconstant.TS_MOCK_DS_SUFFIX + fileconstant.TS_SUFFIX)
            
            # use MockDTO if existing
            if File_processor.verify_dir_existing(mock_ds_filefullpath):
                TS_processor.analysis_DTO(self.get_dtos(), mock_ds_filefullpath)
            elif File_processor.verify_dir_existing(gene_ds_filefullpath):
                TS_processor.analysis_DTO(self.get_dtos(), gene_ds_filefullpath)
            else:
                showerror('Error', 'The DTO interface TS is not existing, please check.')
                return False
        
        # create the observable object
        self.__result, self.__message = TS_processor.create_TS_CommonService(self.get_dtos(), self.get_trans(), self.__feet.get())
        if not self.__result:
            showerror('Error', self.__message)
            return False
        
        return True