'''
Created on Jul 16, 2018

@author: ftd
'''
from tkinter import *
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_bottom import Frame_bottom
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.base.FormatableFrame import FormatableFrame
from src.main.pydev.com.ftd.generalutilities.metadata.service.fileproc.Xmlfile_processor import Xmlfile_processor
from src.main.pydev.com.ftd.generalutilities.metadata.service.base.File_constant import File_constant
from src.main.pydev.com.ftd.generalutilities.metadata.service.base.File_processor import File_processor
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.view.Popup_projfile_details import Popup_projfile_details
from tkinter.messagebox import showerror

class Frame_projfile_check(FormatableFrame):
    '''
    classdocs
    '''

    def __init__(self, parent=None, dtos=None, trans=None, **configs):
        '''
        Constructor
        '''
        self.__checkstatus = {}
        self.__message = None
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
        canv1 = Canvas(self, height=180, width=550)
        #label
        self.__label02 = Label(canv1, text='Metadata xml checking:')
        self.__label02.place(height=20, width=180, relx=0.01, rely=0.01)
        #selected details
        self.__checkval01 = IntVar()
        self.__checkbox01 = Checkbutton(canv1, text = "View metadata", variable = self.__checkval01, onvalue = 1, offvalue = 0, state=DISABLED)
        self.__checkbox01.place(height=20, width=110, relx=0.1, rely=0.15)
        self.__label03 = Label(canv1, text='Status :')
        self.__label03.place(height=20, width=60, relx=0.4, rely=0.15)
        self.__label04 = Label(canv1, text='< no need >')
        self.__label04.place(height=20, width=120, relx=0.5, rely=0.15)
        self.__button01 = Button(canv1, text="Detail")
        self.__button01.place(height=20, width=50, relx=0.8, rely=0.15)
        
        self.__checkval02 = IntVar()
        self.__checkbox02 = Checkbutton(canv1, text = "Resource metadata", variable = self.__checkval02, onvalue = 1, offvalue = 0, state=DISABLED)
        self.__checkbox02.place(height=20, width=130, relx=0.1, rely=0.3)
        self.__label05 = Label(canv1, text='Status :')
        self.__label05.place(height=20, width=60, relx=0.4, rely=0.3)
        self.__label06 = Label(canv1, text='< no need >')
        self.__label06.place(height=20, width=120, relx=0.5, rely=0.3)
        self.__button02 = Button(canv1, text="Detail")
        self.__button02.place(height=20, width=50, relx=0.8, rely=0.3)
        
        self.__checkval03 = IntVar()
        self.__checkbox03 = Checkbutton(canv1, text = "Pom", variable = self.__checkval03, onvalue = 1, offvalue = 0, state=DISABLED)
        self.__checkbox03.place(height=20, width=50, relx=0.1, rely=0.45)
        self.__label07 = Label(canv1, text='Status :')
        self.__label07.place(height=20, width=60, relx=0.4, rely=0.45)
        self.__label08 = Label(canv1, text='< no need >')
        self.__label08.place(height=20, width=120, relx=0.5, rely=0.45)
        self.__button03 = Button(canv1, text="Detail")
        self.__button03.place(height=20, width=50, relx=0.8, rely=0.45)
        
        self.__checkval04 = IntVar()
        self.__checkbox04 = Checkbutton(canv1, text = "beans-app-context", variable = self.__checkval04, onvalue = 1, offvalue = 0, state=DISABLED)
        self.__checkbox04.place(height=20, width=125, relx=0.1, rely=0.6)
        self.__label09 = Label(canv1, text='Status :')
        self.__label09.place(height=20, width=60, relx=0.4, rely=0.6)
        self.__label10 = Label(canv1, text='< no need >')
        self.__label10.place(height=20, width=120, relx=0.5, rely=0.6)
        self.__button04 = Button(canv1, text="Detail")
        self.__button04.place(height=20, width=50, relx=0.8, rely=0.6)
        
        self.__checkval05 = IntVar()
        self.__checkbox05 = Checkbutton(canv1, text = "entityMap", variable = self.__checkval05, onvalue = 1, offvalue = 0, state=DISABLED)
        self.__checkbox05.place(height=20, width=80, relx=0.1, rely=0.75)
        self.__label11 = Label(canv1, text='Status :')
        self.__label11.place(height=20, width=60, relx=0.4, rely=0.75)
        self.__label12 = Label(canv1, text='< no need >')
        self.__label12.place(height=20, width=120, relx=0.5, rely=0.75)
        self.__button05 = Button(canv1, text="Detail")
        self.__button05.place(height=20, width=50, relx=0.8, rely=0.75)
        
        canv1.pack()
        
        #---- panel 02 ----------
        canv2 = Canvas(self, height=80, width=550)
        #labe2
        label2 = Label(canv2, text='Jar checking:')
        label2.place(height=20, width=100, relx=0.01, rely=0.05)
        
        self.__checkval51 = IntVar()
        self.__checkbox51 = Checkbutton(canv2, text = "financials-impl", variable = self.__checkval51, onvalue = 1, offvalue = 0, state=DISABLED)
        self.__checkbox51.place(height=20, width=110, relx=0.1, rely=0.35)
        self.__label51 = Label(canv2, text='Status :')
        self.__label51.place(height=20, width=60, relx=0.4, rely=0.35)
        self.__label52 = Label(canv2, text='< no need >')
        self.__label52.place(height=20, width=120, relx=0.5, rely=0.35)
        self.__button51 = Button(canv2, text="Detail")
        self.__button51.place(height=20, width=50, relx=0.8, rely=0.35)
        
        canv2.pack()
        
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
            self.__checkstatus['ViewMetadata'] = True
        else:
            newlabel01 = "< failed >"
            self.__label04.config(text=newlabel01, fg='red')
            btnlabel = 'Correct'
            self.__button01.config(text=btnlabel)
            self.__checkstatus['ViewMetadata'] = False
        self.__checkval01.set(1)
        #bind button click event
        self.__button01.bind('<Button-1>', self.event_adapter(self.detal_button_click,
                                                              iscorrect=self.__checkstatus['ViewMetadata'],
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
            self.__checkstatus['ResourceMetadata'] = True
        else:
            newlabel = "< failed >"
            self.__label06.config(text=newlabel, fg='red')
            btnlabel = 'Correct'
            self.__button02.config(text=btnlabel)
            self.__checkstatus['ResourceMetadata'] = False
        self.__checkval02.set(1)
        self.__button02.bind('<Button-1>', self.event_adapter(self.detal_button_click,
                                                              iscorrect=self.__checkstatus['ResourceMetadata'],
                                                              filename=entity_name +fileconstant.RESOURCE_METADATA_SUFFIX,
                                                              filetype='ResourceMetadata',
                                                              filepath=resourcefullpath))
        
        #verify pom 
        result, self.__message = Xmlfile_processor.verify_pom(proj_path + fileconstant.POM_PATH)
        if result:
            result, pomDto, self.__message = Xmlfile_processor.read_pom(proj_path + fileconstant.POM_PATH)
            newlabel = "< passed >"
            self.__label08.config(text=newlabel, fg='blue')
            self.get_trans().set_pomDto(pomDto)
            self.__checkstatus['Pom'] = True
        else:
            newlabel = "< failed >"
            self.__label08.config(text=newlabel, fg='red')
            btnlabel = 'Correct'
            self.__button03.config(text=btnlabel)
            self.__checkstatus['Pom'] = False
        self.__checkval03.set(1)
        self.__button03.bind('<Button-1>', self.event_adapter(self.detal_button_click,
                                                              iscorrect=self.__checkstatus['Pom'],
                                                              filename='pom.xml',
                                                              filetype='POM',
                                                              filepath=proj_path + fileconstant.POM_PATH))
        
        #verify beans-app-context 
        result, self.__message = Xmlfile_processor.verify_beans_app_context(proj_path + fileconstant.BEAN_APP_CONTEXT_PATH)
        if result:
            newlabel = "< passed >"
            self.__label10.config(text=newlabel, fg='blue')
            self.get_trans().set_pomDto(pomDto)
            self.__checkstatus['beans-app-context'] = True
        else:
            newlabel = "< failed >"
            self.__label10.config(text=newlabel, fg='red')
            btnlabel = 'Correct'
            self.__button04.config(text=btnlabel)
            self.__checkstatus['beans-app-context'] = False
        self.__checkval04.set(1)
        self.__button04.bind('<Button-1>', self.event_adapter(self.detal_button_click,
                                                              iscorrect=self.__checkstatus['beans-app-context'],
                                                              filename='beans-app-server.xml',
                                                              filetype='beans',
                                                              filepath=proj_path + fileconstant.BEAN_APP_CONTEXT_PATH))
        
        #verify entityMap 
        result, self.__message = Xmlfile_processor.verify_entity_map(proj_path + fileconstant.ENTITY_MAP_PATH)
        if result:
            newlabel = "< passed >"
            self.__label12.config(text=newlabel, fg='blue')
            self.get_trans().set_pomDto(pomDto)
            self.__checkstatus['entityMap'] = True
        else:
            newlabel = "< failed >"
            self.__label12.config(text=newlabel, fg='red')
            btnlabel = 'Correct'
            self.__button05.config(text=btnlabel)
            self.__checkstatus['entityMap'] = False
        self.__checkval05.set(1)
        self.__button05.bind('<Button-1>', self.event_adapter(self.detal_button_click,
                                                              iscorrect=self.__checkstatus['entityMap'],
                                                              filename='entityMap.xml',
                                                              filetype='entityMap',
                                                              filepath=proj_path + fileconstant.ENTITY_MAP_PATH))
        
        
        #verify jar metadata
        jar_exist = False
        jarfullpath = self.get_trans().get_finImplJarPath()
        #verify if jar is existing at the Maven's default repository
        if not jarfullpath:
            userhomepath = File_processor.get_user_home() + fileconstant.JAR_LIB_PATH
            jarfullpath = userhomepath + pomDto.get_financials_api_version() + '\\' + fileconstant.FIN_IMPL_JAR_PREFIX + pomDto.get_financials_api_version() + fileconstant.JAR_SUFFIX
            jar_exist = Xmlfile_processor.verify_dir_existing(jarfullpath)
        if jar_exist:
            newlabel = "< passed >"
            self.__label52.config(text=newlabel, fg='blue')
            self.get_trans().set_finImplJarPath(jarfullpath)
            self.__checkstatus['JAR'] = True
        else:
            newlabel = "< failed >"
            self.__label52.config(text=newlabel, fg='red')
            btnlabel = 'Correct'
            self.__button51.config(text=btnlabel)
            self.__checkstatus['JAR'] = False
        self.__checkval51.set(1)
        self.__button51.bind('<Button-1>', self.event_adapter(self.detal_button_click,
                                                              iscorrect=self.__checkstatus['JAR'],
                                                              filename=fileconstant.FIN_IMPL_JAR_PREFIX + pomDto.get_financials_api_version() + fileconstant.JAR_SUFFIX,
                                                              filetype='JAR',
                                                              filepath=jarfullpath))
        
        #record the message
        print(self.__message)
    
    
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
        '''
        if self.__setfunc:
            self.__setfunc(popup.return_selection())'''
            
    
    def before_next(self):
        '''
        overwrite the function in super class
        verify the input directory
        '''
        for flag in self.__checkstatus.values():
            if not flag:
                showerror('Error', 'There are errors existing, please correct it!')
                return False
            
        return True
        
            