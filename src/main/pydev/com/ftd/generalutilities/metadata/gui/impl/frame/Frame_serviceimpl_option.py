'''
Created on Jun 26, 2018

@author: ftd
'''
from tkinter import *
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_bottom import Frame_bottom
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.base.FormatableFrame import FormatableFrame
from src.main.pydev.com.ftd.generalutilities.metadata.service.base.File_constant import File_constant
from src.main.pydev.com.ftd.generalutilities.metadata.service.base.File_processor import File_processor
from tkinter.messagebox import showwarning
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
        #initialize
        self.__funclists = {}       #functins list backup
        self.__result = None
        self.__error = None
        self.__classlist = []       # 0:service interface, 1:factory interface, 2:qra service class, 3:qra factory class
                                    # 4:entity container interface, 5:entity container impl, 6:main table interface,
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
        
        #analysis the serviceImpl
        self.__result, self.__error, self.__classlist = self.__validate_javas()
        if not self.__result:
            #---- panel 02 ----------
            self.__pack_errorpanel()
            return
        
        # --------- analysis the api service
        self.__result, self.__error, serviceInterDTO = self.__analysis_service_interface()
        if not self.__result:
            #---- panel 02 ----------
            self.__pack_errorpanel()
            return
        else:
            self.get_dtos().set_serviceInterDTO(serviceInterDTO)
        
        self.__result, self.__error, serviceQraDTO = self.__analysis_service_qra()
        if not self.__result:
            #---- panel 02 ----------
            self.__pack_errorpanel()
            return
        else:
            self.get_dtos().set_serviceQraDTO(serviceQraDTO)
        
        
        # --------- analysis the factory
        self.__result, self.__error, factoryInterDTO = self.__analysis_factory_interface()
        if not self.__result:
            #---- panel 02 ----------
            self.__pack_errorpanel()
            return
        else:
            self.get_dtos().set_factoryInterDTO(factoryInterDTO)
        
        self.__result, self.__error, factoryQraDTO = self.__analysis_factory_qra()
        if not self.__result:
            #---- panel 02 ----------
            self.__pack_errorpanel()
            return
        else:
            self.get_dtos().set_factoryQraDTO(factoryQraDTO)

            
        # --------- analysis the container
        self.__result, self.__error, containerInterDTO = self.__analysis_container_interface()
        if not self.__result:
            #---- panel 02 ----------
            self.__pack_errorpanel()
            return
        else:
            self.get_dtos().set_entContInterDTO(containerInterDTO)
            
        self.__result, self.__error, containerQraDTO = self.__analysis_container_qra()
        if not self.__result:
            #---- panel 02 ----------
            self.__pack_errorpanel()
            return
        else:
            self.get_dtos().set_entContQraDTO(containerQraDTO)
            
        
        # --------- analysis the maintable interface
        self.__result, self.__error, maintableInterDTO = self.__analysis_maintable_interface()
        if not self.__result:
            #---- panel 02 ----------
            self.__pack_errorpanel()
            return
        else:
            self.get_dtos().set_maintableInterDTO(maintableInterDTO)

        
        #---- panel 02 ----------
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
        self.__button01 = Button(canv2, text='>>', relief=RAISED, cursor='hand2')
        self.__button01.bind('<Button-1>', self.__to_right_click_event) #bind button click event
        self.__button01.place(height=35, width=25, relx=0.465, rely=0.3)
        
        self.__button02 = Button(canv2, text='<<', relief=RAISED, cursor='hand2')
        self.__button02.bind('<Button-1>', self.__to_left_click_event) #bind button click event
        self.__button02.place(height=35, width=25, relx=0.465, rely=0.6)
        
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
        self.__rad2.place(height=20, width=200, relx= 0.1, rely=0.45)
        self.__rad2.deselect()
        self.__rad3 = Radiobutton(canv3, text='Save the previous file as backup', variable=self.__vari1, value=3)
        self.__rad3.place(height=20, width=200, relx= 0.1, rely=0.7)
        self.__rad3.deselect()
        canv3.pack()

        
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
        Java_processor.create_service_impl(self.__feet.get(), self.get_trans(), self.get_dtos(), self.__listboxright.get(0, END), self.__vari1.get())
        
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
        
        
    def __validate_javas(self):
        '''
        analysis the serviceImpl according to ResourceMetadataDTO in self.__resDto
        '''
        #get the entity info
        transDto = self.get_trans()
        entityDto = self.get_dtos()
        resDto = entityDto.get_resourceDTO()
        returnList = []
        
        #get the entity interface
        entityName = entityDto.get_entityname()
        prim_uri = resDto.get_primary_secure_uri()
        entity_interface = prim_uri[prim_uri.rindex(':')+1:]
        package_list = entity_interface.split('.')
        
        #verify if the java decompiled files existing
        fileconstant = File_constant()
        unzip_path = transDto.get_workspacepath() + fileconstant.UNZIP_JAR_FOLDER
        if not File_processor.verify_dir_existing(unzip_path):
            message = 'The decompile folder not existing, please re-generate!'
            return False, message, None
        
        api_unzip_path = unzip_path + fileconstant.API_FOLDER
        impl_unzip_path = unzip_path + fileconstant.IMPL_FOLDER
        idx = 0
        while idx < len(package_list):
            if idx != len(package_list) -1:
                api_unzip_path = api_unzip_path + package_list[idx] + '\\'
                impl_unzip_path = impl_unzip_path + package_list[idx] + '\\'
            else:
                impl_unzip_path = impl_unzip_path + fileconstant.IMPL_FOLDER
            idx = idx + 1
        
        
        
        # TODO: this is a hardcode style, should be enhancement later!!!
        business_entity_name = package_list[-1][1:]
        serviceImpl_name = business_entity_name + fileconstant.SERVICEIMPL_SUFFIX + fileconstant.JAVA_SUFFIX
        self.__feet.set(serviceImpl_name)
        
        # --------------------------------------------------------------------- #
        #                   The interface of service,factory                    #
        # --------------------------------------------------------------------- #
        # Validate the Api package
        decp_service_interface_name = business_entity_name + fileconstant.JAVA_SERVICE_SUFFIX + fileconstant.DEPOMPILE_JAVA_SUFFIX
        decp_factory_interface_name = business_entity_name + fileconstant.JAVA_FACTORY_SUFFIX + fileconstant.DEPOMPILE_JAVA_SUFFIX
        
        if not File_processor.verify_dir_existing(api_unzip_path):
            message = 'There is no api package for entity %s,\n please check your api jar!' % business_entity_name
            return False, message, None
        
        if not File_processor.verify_dir_existing(api_unzip_path + decp_service_interface_name):
            message = 'There is no service-interface for entity %s,\n please check your api jar!' % decp_service_interface_name
            return False, message, None
        
        if not File_processor.verify_dir_existing(api_unzip_path + decp_factory_interface_name):
            message = 'There is no factory-interface for entity %s,\n please check your api jar!' % decp_factory_interface_name
            return False, message, None
        
        # set the return list (idx = 0,1)
        returnList.append(api_unzip_path + decp_service_interface_name)
        returnList.append(api_unzip_path + decp_factory_interface_name)
        
        # --------------------------------------------------------------------- #
        #                   The impl of service,factory                         #
        # --------------------------------------------------------------------- #
        # Validate the Impl package
        decp_service_impl_name = fileconstant.JAVA_QRA_PREFIX + business_entity_name + fileconstant.JAVA_SERVICE_SUFFIX + fileconstant.DEPOMPILE_JAVA_SUFFIX
        decp_factory_impl_name = fileconstant.JAVA_QRA_PREFIX + business_entity_name + fileconstant.JAVA_FACTORY_SUFFIX + fileconstant.DEPOMPILE_JAVA_SUFFIX
        
        if not File_processor.verify_dir_existing(impl_unzip_path):
            message = 'There is no serviceImpl package for entity %s,\n please check your impl jar!' % business_entity_name
            return False, message, None
        
        if not File_processor.verify_dir_existing(impl_unzip_path + decp_service_impl_name):
            message = 'There is no service-class for entity %s,\n please check your impl jar!' % decp_service_impl_name
            return False, message, None
        
        if not File_processor.verify_dir_existing(impl_unzip_path + decp_factory_impl_name):
            message = 'There is no factory-class for entity %s,\n please check your impl jar!' % decp_factory_impl_name
            return False, message, None
        
        # set the return list (idx = 2,3)
        returnList.append(impl_unzip_path + decp_service_impl_name)
        returnList.append(impl_unzip_path + decp_factory_impl_name)
        
        
        # Validate the additional functionality
        
        
        #--- the entity name
        entityDSName = entityDto.get_resourceDTO().get_view_parameters().get_data_resource()
        mainTableName = entityDto.get_resourceDTO().get_view_parameters().get_table()
        # --------------------------------------------------------------------- #
        #                The interface & Impl of container                      #
        # --------------------------------------------------------------------- #
        # Validate the container interface
        entity_container_interface_name = entityDSName[:1].upper() + entityDSName[1:-1] + fileconstant.JAVA_CONTAINER_SUFFIX + fileconstant.DEPOMPILE_JAVA_SUFFIX
        entity_container_impl_name = fileconstant.JAVA_QRA_PREFIX + entityDSName[:1].upper() + entityDSName[1:-1] + fileconstant.JAVA_CONTAINER_SUFFIX + fileconstant.DEPOMPILE_JAVA_SUFFIX
        
        if not File_processor.verify_dir_existing(api_unzip_path + entity_container_interface_name):
            message = 'There is no interface for container %s,\n please check your api jar!' % entity_container_interface_name
            return False, message, None
        
        if not File_processor.verify_dir_existing(impl_unzip_path + entity_container_impl_name):
            message = 'There is no impl for container %s,\n please check your impl jar!' % entity_container_impl_name
            return False, message, None
        
        # set the return list (idx = 4,5)
        returnList.append(api_unzip_path + entity_container_interface_name)
        returnList.append(impl_unzip_path + entity_container_impl_name)
        
        # --------------------------------------------------------------------- #
        #                The interface of main table                            #
        # --------------------------------------------------------------------- #
        main_table_interface_name = mainTableName[:1].upper() + mainTableName[1:] + fileconstant.DEPOMPILE_JAVA_SUFFIX
        
        if not File_processor.verify_dir_existing(api_unzip_path + main_table_interface_name):
            message = 'There is no interface for main table %s,\n please check your api jar!' % main_table_interface_name
            return False, message, None
        
        # set the return list (idx = 6)
        returnList.append(api_unzip_path + main_table_interface_name)
        
        
        return True, None, returnList
        
        
    
    def __analysis_service_interface(self):
        '''
        analysis the entityService._java file and generate the function list
        '''
        # service interface
        decp_service_interface_name = self.__classlist[0]
        # call the java processor
        result, message, serviceInterDTO = Java_processor.read_java_interface(decp_service_interface_name)
        if not result:
            return False, message, None
        
        return True, None, serviceInterDTO
    
    
    def __analysis_service_qra(self):
        '''
        analysis the QraEntityService._java file
        '''
        # entity container interface
        entity_service_qra_name = self.__classlist[2]
        # call the java processor
        result, message, serviceQraDTO = Java_processor.read_java_class(entity_service_qra_name, self.get_dtos().get_serviceInterDTO())
        if not result:
            return False, message, None
        
        return True, None, serviceQraDTO
    
    
    def __analysis_factory_interface(self):
        '''
        analysis the entityfactory._java file
        '''
        # entity factory interface
        entity_factory_interface_name = self.__classlist[1]
        # call the java processor
        result, message, factoryInterDTO = Java_processor.read_java_interface(entity_factory_interface_name)
        if not result:
            return False, message, None
        
        return True, None, factoryInterDTO
    
    
    def __analysis_factory_qra(self):
        '''
        analysis the QraEntityfactory._java file
        '''
        # entity container interface
        entity_factory_qra_name = self.__classlist[3]
        # call the java processor
        result, message, factoryQraDTO = Java_processor.read_java_class(entity_factory_qra_name, self.get_dtos().get_factoryInterDTO())
        if not result:
            return False, message, None
        
        return True, None, factoryQraDTO
    
    
    def __analysis_container_interface(self):
        '''
        analysis the entitycontainer._java file
        '''
        # entity container interface
        entity_container_interface_name = self.__classlist[4]
        # call the java processor
        result, message, containerInterDTO = Java_processor.read_java_interface(entity_container_interface_name)
        if not result:
            return False, message, None
        
        return True, None, containerInterDTO
    
    
    def __analysis_container_qra(self):
        '''
        analysis the QraEntitycontainer._java file
        '''
        # entity container interface
        entity_container_qra_name = self.__classlist[5]
        # call the java processor
        result, message, containerQraDTO = Java_processor.read_java_class(entity_container_qra_name, self.get_dtos().get_entContInterDTO())
        if not result:
            return False, message, None
        
        return True, None, containerQraDTO
    
    
    def __analysis_maintable_interface(self):
        '''
        analysis the maintable._java file and generate the function list
        '''
        # service interface
        maintable_interface_name = self.__classlist[6]
        # call the java processor
        result, message, maintableInterDTO = Java_processor.read_java_interface(maintable_interface_name)
        if not result:
            return False, message, None
        
        return True, None, maintableInterDTO
    
    
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
            
    
    def __to_left_click_event(self, event):
        '''
        move the selection to the left list box
        '''
        javaconstant = Java_constant()
        if not self.__listboxright or self.__listboxright.size() == 0:
            return
        
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