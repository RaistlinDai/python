'''
Created on Jul 16, 2018

@author: ftd
'''
from tkinter import *
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_bottom import Frame_bottom
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.base.FormatableFrame import FormatableFrame
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.view.Popup_projfile_details import Popup_projfile_details
from src.main.pydev.com.ftd.generalutilities.metadata.service.fileproc.Xmlfile_processor import Xmlfile_processor
from src.main.pydev.com.ftd.generalutilities.metadata.service.base.File_constant import File_constant
from src.main.pydev.com.ftd.generalutilities.metadata.service.base.File_processor import File_processor
from src.main.pydev.com.ftd.generalutilities.metadata.service.fileproc.Java_processor import Java_processor
from tkinter.messagebox import showerror, showwarning
from src.main.pydev.com.ftd.generalutilities.metadata.service.multproc.Multiple_processor import Multiple_processor

class Frame_projfile_check(FormatableFrame):
    '''
    classdocs
    '''

    def __init__(self, parent=None, dtos=None, trans=None, **configs):
        '''
        Constructor
        '''
        self.__checkstatus = {}  # the generator status, the same structure as TransactionDTO.GeneratorStatus (e.g. {'Metadata':1})
        self.__message = None
        FormatableFrame.__init__(self, parent.get_mainframe(), dtos, trans, **configs)
        
        
    #overwrite create_widges
    def create_widges(self):
        #frame
        self.__frame1 = FormatableFrame(self)
        self.__frame1.pack(side=TOP)
        #Title
        self.__label01 = Label(self.__frame1, text="Important files checking", width= 45)
        self.__label01.pack(side=TOP, fill=X, ipady=10)
        
        #---- panel 01 ----------
        canv1 = Canvas(self, height=120, width=550)
        #label
        self.__label02 = Label(canv1, text='Project file checking:')
        self.__label02.place(height=20, width=150, relx=0.01, rely=0.02)
        #selected details        
        self.__checkval03 = IntVar()
        self.__checkbox03 = Checkbutton(canv1, text = "Pom", variable = self.__checkval03, onvalue = 1, offvalue = 0, state=DISABLED)
        self.__checkbox03.place(height=20, width=50, relx=0.1, rely=0.2)
        self.__label07 = Label(canv1, text='Status :')
        self.__label07.place(height=20, width=60, relx=0.4, rely=0.2)
        self.__label08 = Label(canv1, text='< no need >')
        self.__label08.place(height=20, width=120, relx=0.5, rely=0.2)
        self.__button03 = Button(canv1, text="Detail")
        self.__button03.place(height=20, width=50, relx=0.8, rely=0.2)
        
        self.__checkval04 = IntVar()
        self.__checkbox04 = Checkbutton(canv1, text = "beans-app-context", variable = self.__checkval04, onvalue = 1, offvalue = 0, state=DISABLED)
        self.__checkbox04.place(height=20, width=125, relx=0.1, rely=0.4)
        self.__label09 = Label(canv1, text='Status :')
        self.__label09.place(height=20, width=60, relx=0.4, rely=0.4)
        self.__label10 = Label(canv1, text='< no need >')
        self.__label10.place(height=20, width=120, relx=0.5, rely=0.4)
        self.__button04 = Button(canv1, text="Detail")
        self.__button04.place(height=20, width=50, relx=0.8, rely=0.4)
        
        self.__checkval05 = IntVar()
        self.__checkbox05 = Checkbutton(canv1, text = "entityMap", variable = self.__checkval05, onvalue = 1, offvalue = 0, state=DISABLED)
        self.__checkbox05.place(height=20, width=80, relx=0.1, rely=0.6)
        self.__label11 = Label(canv1, text='Status :')
        self.__label11.place(height=20, width=60, relx=0.4, rely=0.6)
        self.__label12 = Label(canv1, text='< no need >')
        self.__label12.place(height=20, width=120, relx=0.5, rely=0.6)
        self.__button05 = Button(canv1, text="Detail")
        self.__button05.place(height=20, width=50, relx=0.8, rely=0.6)
        
        #warning message in xml panel
        self.__label99 = Label(canv1, text='Warning : Please run svn revert/update if something in project is incorrect.', fg='red')
        self.__label99.place(height=20, width=400, relx=0.1, rely=0.8)
                
        canv1.pack()
        
        #---- panel 02 ----------
        canv2 = Canvas(self, height=80, width=550)
        #labe2
        label2 = Label(canv2, text='Metadata checking:')
        label2.place(height=20, width=120, relx=0.01, rely=0.05)
        
        self.__checkval01 = IntVar()
        self.__checkbox01 = Checkbutton(canv2, text = "View metadata", variable = self.__checkval01, onvalue = 1, offvalue = 0, state=DISABLED)
        self.__checkbox01.place(height=20, width=110, relx=0.1, rely=0.3)
        self.__label03 = Label(canv2, text='Status :')
        self.__label03.place(height=20, width=60, relx=0.4, rely=0.3)
        self.__label04 = Label(canv2, text='< no need >')
        self.__label04.place(height=20, width=120, relx=0.5, rely=0.3)
        self.__button01 = Button(canv2, text="Detail")
        self.__button01.place(height=20, width=50, relx=0.8, rely=0.3)
        
        self.__checkval02 = IntVar()
        self.__checkbox02 = Checkbutton(canv2, text = "Resource metadata", variable = self.__checkval02, onvalue = 1, offvalue = 0, state=DISABLED)
        self.__checkbox02.place(height=20, width=130, relx=0.1, rely=0.6)
        self.__label05 = Label(canv2, text='Status :')
        self.__label05.place(height=20, width=60, relx=0.4, rely=0.6)
        self.__label06 = Label(canv2, text='< no need >')
        self.__label06.place(height=20, width=120, relx=0.5, rely=0.6)
        self.__button02 = Button(canv2, text="Detail")
        self.__button02.place(height=20, width=50, relx=0.8, rely=0.6)
        
        canv2.pack()
        
        #---- panel 03 ----------
        canv3 = Canvas(self, height=60, width=550)
        #labe3
        label3 = Label(canv3, text='Jar checking:')
        label3.place(height=20, width=100, relx=0.01, rely=0.05)
        
        self.__chkint91 = IntVar()
        self.__checkval91 = self.__chkint91
        self.__checkbox91 = Checkbutton(canv3, text = "financials-impl", variable = self.__checkval91, onvalue = 1, offvalue = 0)
        self.__checkbox91.place(height=20, width=110, relx=0.1, rely=0.5)
        self.__label91 = Label(canv3, text='Status :')
        self.__label91.place(height=20, width=60, relx=0.4, rely=0.5)
        self.__label92 = Label(canv3, text='< no need >')
        self.__label92.place(height=20, width=120, relx=0.5, rely=0.5)
        self.__button91 = Button(canv3, text="Detail")
        self.__button91.place(height=20, width=50, relx=0.8, rely=0.5)
        
        canv3.pack()
        
        #--- initialize
        self.verify_proj_files()
    
    
    #overwrite create_widges
    def add_bottom(self, parent):
        #bottom frame
        exFuncs = {'Next':{'process':self.get_nextframe(), 'before':self.before_next},
                   'Prev':{'process':self.get_prevframe(), 'before':self.before_prev}}
        self.__buttom = Frame_bottom(parent, ['Next','Prev'], exFuncs)
        self.__buttom.pack(fill=X, ipady=10,side=BOTTOM)
        
        
    def verify_proj_files(self):
        '''
        verify the project fiels
        '''
        #path constant
        fileconstant = File_constant()
        entity_name = self.get_dtos().get_entityname()
        proj_path = self.get_trans().get_projectpath()
        
        #verify view metadata
        view_exist = False
        viewfullpath = self.get_dtos().get_viewfullpath()
        if not viewfullpath and entity_name:
            viewfullpath = proj_path + fileconstant.VIEW_METADATA_PATH + entity_name +fileconstant.XML_SUFFIX
            view_exist, self.__message = Xmlfile_processor.veriy_view_metadata(viewfullpath)
        elif viewfullpath:
            view_exist = True
        if view_exist:
            newlabel01 = "< passed >"
            self.__label04.config(text=newlabel01, fg='blue')
            self.get_dtos().set_viewfullpath(viewfullpath)
            self.__checkstatus['ViewMetadata'] = [True, self.__checkval01]
        else:
            newlabel01 = "< failed >"
            self.__label04.config(text=newlabel01, fg='red')
            btnlabel = 'Correct'
            self.__button01.config(text=btnlabel)
            self.__checkstatus['ViewMetadata'] = [False, self.__checkval01]
        self.__checkval01.set(1)
        #bind button click event
        self.__button01.bind('<Button-1>', self.event_adapter(self.detal_button_click,
                                                              iscorrect=self.__checkstatus['ViewMetadata'][0],
                                                              filename=entity_name +fileconstant.XML_SUFFIX,
                                                              filetype='ViewMetadata',
                                                              filepath=viewfullpath))
        
        #verify source metadata
        resource_exist = False
        resourcefullpath = self.get_dtos().get_resourcefullpath()
        if not resourcefullpath and entity_name:
            resourcefullpath = proj_path + fileconstant.RESOURCE_METADATA_PATH + entity_name +fileconstant.RESOURCE_METADATA_SUFFIX
            resource_exist, self.__message = Xmlfile_processor.veriy_resource_metadata(resourcefullpath)
        if resource_exist:
            newlabel = "< passed >"
            self.__label06.config(text=newlabel, fg='blue')
            self.get_dtos().set_resourcefullpath(resourcefullpath)
            self.__checkstatus['ResourceMetadata'] = [True, self.__checkval02]
        else:
            newlabel = "< failed >"
            self.__label06.config(text=newlabel, fg='red')
            btnlabel = 'Correct'
            self.__button02.config(text=btnlabel)
            self.__checkstatus['ResourceMetadata'] = [False, self.__checkval02]
        self.__checkval02.set(1)
        self.__button02.bind('<Button-1>', self.event_adapter(self.detal_button_click,
                                                              iscorrect=self.__checkstatus['ResourceMetadata'][0],
                                                              filename=entity_name +fileconstant.RESOURCE_METADATA_SUFFIX,
                                                              filetype='ResourceMetadata',
                                                              filepath=resourcefullpath))
        
        #verify pom 
        result, self.__message = Xmlfile_processor.verify_pom(proj_path + fileconstant.POM_PATH)
        if result:
            #read the pom
            result, pomDto, self.__message = Xmlfile_processor.read_pom(proj_path + fileconstant.POM_PATH)
            newlabel = "< passed >"
            self.__label08.config(text=newlabel, fg='blue')
            self.get_trans().set_pomDto(pomDto)
            self.__checkstatus['Pom'] = [True, self.__checkval03]
        else:
            newlabel = "< failed >"
            self.__label08.config(text=newlabel, fg='red')
            btnlabel = 'Correct'
            self.__button03.config(text=btnlabel)
            self.__checkstatus['Pom'] = [False, self.__checkval03]
        self.__checkval03.set(1)
        self.__button03.bind('<Button-1>', self.event_adapter(self.detal_button_click,
                                                              iscorrect=self.__checkstatus['Pom'][0],
                                                              filename='pom.xml',
                                                              filetype='POM',
                                                              filepath=proj_path + fileconstant.POM_PATH))
        
        #verify beans-app-context 
        result, self.__message = Xmlfile_processor.verify_beans_app_context(proj_path + fileconstant.BEAN_APP_CONTEXT_PATH)
        if result:
            newlabel = "< passed >"
            self.__label10.config(text=newlabel, fg='blue')
            self.get_trans().set_pomDto(pomDto)
            self.__checkstatus['beans-app-context'] = [True, self.__checkval04]
        else:
            newlabel = "< failed >"
            self.__label10.config(text=newlabel, fg='red')
            btnlabel = 'Correct'
            self.__button04.config(text=btnlabel)
            self.__checkstatus['beans-app-context'] = [False, self.__checkval04]
        self.__checkval04.set(1)
        self.__button04.bind('<Button-1>', self.event_adapter(self.detal_button_click,
                                                              iscorrect=self.__checkstatus['beans-app-context'][0],
                                                              filename='beans-app-server.xml',
                                                              filetype='beans',
                                                              filepath=proj_path + fileconstant.BEAN_APP_CONTEXT_PATH))
        
        #verify entityMap 
        result, self.__message = Xmlfile_processor.verify_entity_map(proj_path + fileconstant.ENTITY_MAP_PATH)
        if result:
            newlabel = "< passed >"
            self.__label12.config(text=newlabel, fg='blue')
            self.get_trans().set_pomDto(pomDto)
            self.__checkstatus['entityMap'] = [True, self.__checkval05]
        else:
            newlabel = "< failed >"
            self.__label12.config(text=newlabel, fg='red')
            btnlabel = 'Correct'
            self.__button05.config(text=btnlabel)
            self.__checkstatus['entityMap'] = [False, self.__checkval05]
        self.__checkval05.set(1)
        self.__button05.bind('<Button-1>', self.event_adapter(self.detal_button_click,
                                                              iscorrect=self.__checkstatus['entityMap'][0],
                                                              filename='entityMap.xml',
                                                              filetype='entityMap',
                                                              filepath=proj_path + fileconstant.ENTITY_MAP_PATH))
        
        #verify jar metadata
        result = False
        jarname = None
        jarfullpath = self.get_trans().get_finImplJarPath()
        #verify if jar is existing at the Maven's default repository
        if not jarfullpath:
            userhomepath = File_processor.get_user_home() + fileconstant.JAR_LIB_PATH
            #jar name and full path
            jarfullpath = userhomepath + pomDto.get_financials_api_version() + '\\' + fileconstant.FIN_IMPL_JAR_PREFIX + pomDto.get_financials_api_version() + fileconstant.JAR_SUFFIX
            jarname = fileconstant.FIN_IMPL_JAR_PREFIX + pomDto.get_financials_api_version() + fileconstant.JAR_SUFFIX
            
            result, self.__message  = Java_processor.verify_jar_type(jarfullpath)
            
            if result:
                newlabel = "< passed >"
                self.__label92.config(text=newlabel, fg='blue')
                self.get_trans().set_finImplJarPath(jarfullpath)
                self.__checkstatus['JAR'] = [True, self.__checkval91]
            else:
                newlabel = "< failed >"
                self.__label92.config(text=newlabel, fg='red')
                btnlabel = 'Correct'
                self.__button91.config(text=btnlabel)
                self.__checkstatus['JAR'] = [False, self.__checkval91]
        else:
            newlabel = "< passed >"
            self.__label92.config(text=newlabel, fg='blue')
            self.__checkstatus['JAR'] = [True, self.__checkval91]
            #jar name
            jarname = File_processor.get_file_name(self.get_trans().get_finImplJarPath())
                
        self.__checkval91.set(1)
        self.__button91.bind('<Button-1>', self.event_adapter(self.detal_button_click,
                                                              iscorrect=self.__checkstatus['JAR'][0],
                                                              filename=jarname,
                                                              filetype='JAR',
                                                              filepath=jarfullpath))
    
    
    def event_adapter(self, fun, **kwds):
        '''
        event adapter, to transfer the input parameters into event
        @param fun: the event function
        @param kwds: event input parameters
        '''
        return lambda event,fun=fun,kwds=kwds: fun(event, **kwds)
    
    
    def detal_button_click(self, event, iscorrect, filename, filetype, filepath):
        '''
        detail button click event
        '''
        fileinfo = {'filename':filename, 'filetype':filetype, 'filepath':filepath, 'iscorrect':iscorrect}
        popup = Popup_projfile_details(fileinfo)
        popup.grab_set()
        popup.focus_set()
        popup.wait_window()
        
        if not iscorrect:
            result_dto = popup.return_selection()
            if result_dto['iscorrect']:
                if result_dto['filetype'] == 'JAR':
                    #update the global parameters
                    self.__checkstatus['JAR'][0] = True
                    #set new jara path into transaction
                    self.get_trans().set_finImplJarPath(result_dto['filepath'])
                    #update labels
                    newlabel = "< passed >"
                    self.__label92.config(text=newlabel, fg='blue')
                    btnlabel = 'Detail'
                    self.__button91.config(text=btnlabel)
                    #update event parameters
                    self.__button91.bind('<Button-1>', self.event_adapter(self.detal_button_click,
                                                              iscorrect=self.__checkstatus['JAR'][0],
                                                              filename=result_dto['filename'],
                                                              filetype='JAR',
                                                              filepath=result_dto['filepath']))
    
    def before_next(self):
        '''
        overwrite the function in super class
        verify the input directory
        '''
        #--- read the resource metadata and load the data into ResourceMetadataDTO
        curDtos = self.get_dtos()
        resourcepath = curDtos.get_resourcefullpath()
        result, message = Xmlfile_processor.read_resource_metadata(resourcepath, self.get_dtos())
        if not result:
            showerror('Error', message)
            return False
        
        #--- verify generator options
        warning_flag = False
        for flag in self.__checkstatus.items():
            if not flag[1][0] and flag[1][1].get() == 1:
                showerror('Error', 'There are errors existing, please correct it!')
                return False
            elif flag[1][1].get() == 0:
                if not warning_flag:
                    showwarning('Warning', 'Some generators could not work because the related file validations are skipped.')
                    warning_flag = True
                    
        # save the generator status into TransDto
        self.get_trans().set_generatorstatus(self.__checkstatus)
        
        #jar processing
        if self.__chkint91.get() == 1:
            Multiple_processor.multiprocessing_service(self.get_trans())
        
        return True
        
            