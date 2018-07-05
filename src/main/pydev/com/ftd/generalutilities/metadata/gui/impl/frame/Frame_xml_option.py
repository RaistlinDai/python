'''
Created on Jun 26, 2018

@author: ftd
'''
from tkinter import *
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_bottom import Frame_bottom
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.base.FormatableFrame import FormatableFrame
from src.main.pydev.com.ftd.generalutilities.metadata.service.File_reader import File_reader
from src.main.pydev.com.ftd.generalutilities.metadata.service.File_constant import File_constant


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
        
        #read the resource metadata and load the data into ResourceMetadataDTO
        resourcepath = curDtos.get_resourcefullpath()
        File_reader.read_resource_metadata(resourcepath, self.get_dtos())
        
        ''' test '''
        result, status = File_reader.read_bean_app_context(curTrans.get_projectpath() + fileconstant.BEAN_APP_CONTEXT_PATH)
        if status:
            #verify if the target entity uri is existing in the bean-app-context
            if curDtos.get_resourceDTO().get_primary_secure_uri() in result.get_entity_uri_mapstring():
                print(True)
            else:
                print(False)
            
        return True    