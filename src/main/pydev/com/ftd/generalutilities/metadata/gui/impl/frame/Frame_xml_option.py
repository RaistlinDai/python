'''
Created on Jun 26, 2018

@author: ftd
'''
from tkinter import *
from tkinter import ttk
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_bottom import Frame_bottom
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.base.FormatableFrame import FormatableFrame
from src.main.pydev.com.ftd.generalutilities.metadata.service.fileproc.Xmlfile_processor import Xmlfile_processor
from src.main.pydev.com.ftd.generalutilities.metadata.service.base.File_constant import File_constant
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.base.Frame_constant import Frame_constant
from tkinter.messagebox import showerror, showwarning

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
        
        canv2 = Canvas(self, height=130, width=550)
        #label
        label2 = Label(canv2, text='BeanAppContext:')
        label2.place(height=20, width=100, relx= 0, rely=0)
        #radio box
        self.__vari2 = IntVar()
        self.__rad3 = Radiobutton(canv2, text='Save the backup', variable=self.__vari2, value=1)
        self.__rad3.place(height=20, width=150, relx= 0.1, rely=0.17)
        self.__rad3.select()
        self.__rad4 = Radiobutton(canv2, text='Clean the backup', variable=self.__vari2, value=2)
        self.__rad4.place(height=20, width=150, relx= 0.4, rely=0.17)
        self.__rad4.deselect()
        
        #label
        label3 = Label(canv2, text='Type:')
        label3.place(height=20, width=40, relx= 0.1, rely=0.45)
        #combo box
        self.__varc3 = StringVar()
        self.__cob1 = ttk.Combobox(canv2, textvariable=self.__varc3)
        self.__cob1["values"] = ('blf', 'mfg')
        self.__cob1["state"] = "readonly"
        self.__cob1.current(0)
        self.__cob1.place(height=20, width=110, relx= 0.17, rely=0.45)
        
        #label
        label4 = Label(canv2, text='panDomain:')
        label4.place(height=20, width=80, relx= 0.4, rely=0.45)
        #combo box
        self.__varc4 = StringVar()
        self.__cob2 = ttk.Combobox(canv2, textvariable=self.__varc4)
        self.__cob2["values"] = ('true', 'false')
        self.__cob2["state"] = "readonly"
        self.__cob2.current(0)
        self.__cob2.place(height=20, width=70, relx= 0.55, rely=0.45)
        
        #label
        label4 = Label(canv2, text='objectName:')
        label4.place(height=20, width=80, relx= 0.1, rely=0.65)
        #input
        self.__varc5 = StringVar()
        self.__varc5.set('xxx')
        self.__dicinput = Entry(canv2, textvariable=self.__varc5, borderwidth=3, bg='black', foreground='yellow', highlightcolor='red', insertbackground='red')
        self.__dicinput.place(height=20, width=120, relx= 0.25, rely=0.65)
        
        canv2.pack()
    
    
    def show_msg(self):
        print(self.__cob1.get())
    
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
        print(self.__varc3.get() + ',' + self.__varc4.get() + ',' + self.__varc5.get())
        #--- update the process options in transaction dto ----
        result, message = curTrans.update_options(
            {'Xml':{'EntityMap':self.__vari1.get(), 'BeanAppContext':self.__vari2.get()}}, const.ACTION_UPDATE)
        
        if not result:
            print(message)
            return False
        
        #--- read the resource metadata and load the data into ResourceMetadataDTO ---
        resourcepath = curDtos.get_resourcefullpath()
        Xmlfile_processor.read_resource_metadata(resourcepath, self.get_dtos())
        
        ''' process file '''
        beanpath = curTrans.get_projectpath() + fileconstant.BEAN_APP_CONTEXT_PATH
        status, beanDTO, message = Xmlfile_processor.read_bean_app_context(beanpath)
        if status:
            resDTO = curDtos.get_resourceDTO()
            #--- verify if the target entity uri is existing in the beans-app-context
            if resDTO.get_primary_secure_uri() in beanDTO.get_entity_uri_mapstring():
                showwarning('Note', 'The entity uri has been added in the beans-app-context.xml.')
            else:
                #--- backup beans-app-context
                Xmlfile_processor.copy_file(beanpath, curTrans.get_workspacepath() + beanDTO.get_filename() + fileconstant.BACKUP_SUFFIX)
                #--- format the new uri
                value = resDTO.get_primary_secure_uri() + ',' + resDTO.get_meta_uri()
                #--- update beans-app-context
                status, message = Xmlfile_processor.write_bean_app_context(beanpath, value)
                if not status:
                    showerror('Error', message)
                    return False
        else:
            showerror('Error', message)
            return False
        
        return True    