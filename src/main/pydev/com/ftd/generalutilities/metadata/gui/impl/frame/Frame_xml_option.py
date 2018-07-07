'''
Created on Jun 26, 2018

@author: ftd
'''
from tkinter import *
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_bottom import Frame_bottom
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.base.FormatableFrame import FormatableFrame
from src.main.pydev.com.ftd.generalutilities.metadata.service.File_processor import File_processor
from src.main.pydev.com.ftd.generalutilities.metadata.service.File_constant import File_constant
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.base.Frame_constant import Frame_constant
from tkinter.messagebox import showerror, showwarning
from pip._internal.utils.misc import file_contents


class Frame_xml_option(FormatableFrame):
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
        self.__label01 = Label(self.__frame1, text="Xml generator options", width= 45)
        self.__label01.pack(side=TOP, fill=X, ipady=10)
        
        canv1 = Canvas(self, height=70, width=550)
        #label
        label1 = Label(canv1, text='EntityMap:')
        label1.place(height=20, width=60, relx= 0, rely=0)
        #radio box
        self.__vari1 = IntVar()
        self.__rad1 = Radiobutton(canv1, text='Save the backup', variable=self.__vari1, value=1)
        self.__rad1.place(height=20, width=150, relx= 0.1, rely=0.3)
        self.__rad1.select()
        self.__rad2 = Radiobutton(canv1, text='Clean the backup', variable=self.__vari1, value=2)
        self.__rad2.place(height=20, width=150, relx= 0.4, rely=0.3)
        self.__rad2.deselect()
        canv1.pack()
        
        canv2 = Canvas(self, height=70, width=550)
        #label
        label2 = Label(canv2, text='BeanAppContext:')
        label2.place(height=20, width=100, relx= 0, rely=0)
        #radio box
        self.__vari2 = IntVar()
        self.__rad3 = Radiobutton(canv2, text='Save the backup', variable=self.__vari2, value=1)
        self.__rad3.place(height=20, width=150, relx= 0.1, rely=0.3)
        self.__rad3.select()
        self.__rad4 = Radiobutton(canv2, text='Clean the backup', variable=self.__vari2, value=2)
        self.__rad4.place(height=20, width=150, relx= 0.4, rely=0.3)
        self.__rad4.deselect()
        canv2.pack()
        
    
    #overwrite create_widges
    def add_bottom(self, parent):
        #bottom frame
        exFuncs = {'Next':{'process':self.get_nextframe(), 'before':self.before_next},
                   'Prev':{'process':self.get_prevframe(), 'before':self.before_prev}}
        self.__buttom = Frame_bottom(parent, ['Next','Prev'], exFuncs)
        self.__buttom.pack(fill=X, ipady=10,side=BOTTOM)
        
        
    #overwrite before_next
    def before_next(self):    
        fileconstant = File_constant()
        curDtos = self.get_dtos()
        curTrans = self.get_trans()
        const = Frame_constant()
        
        #--- update the process options in transaction dto ----
        result, message = curTrans.update_options(
            {'Xml':{'EntityMap':self.__vari1.get(), 'BeanAppContext':self.__vari2.get()}}, const.ACTION_UPDATE)
        
        if not result:
            print(message)
            return False
        
        #--- read the resource metadata and load the data into ResourceMetadataDTO ---
        resourcepath = curDtos.get_resourcefullpath()
        File_processor.read_resource_metadata(resourcepath, self.get_dtos())
        
        ''' process file '''
        beanpath = curTrans.get_projectpath() + fileconstant.BEAN_APP_CONTEXT_PATH
        status, beanDTO, message = File_processor.read_bean_app_context(beanpath)
        if status:
            #--- verify if the target entity uri is existing in the bean-app-context
            if curDtos.get_resourceDTO().get_primary_secure_uri() in beanDTO.get_entity_uri_mapstring():
                showwarning('Note', 'The entity uri has been added in the bean-app-context.xml.')
                return True
            else:
                #--- backup
                File_processor.copy_file(beanpath, curTrans.get_workspacepath() + beanDTO.get_filename() + fileconstant.BACKUP_SUFFIX)
                #--- update
                
                
                print(False)
        else:
            showerror('Error', message)
            return False
        
        return True    