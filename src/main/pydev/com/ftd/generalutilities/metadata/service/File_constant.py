'''
Created on Jun 27, 2018

@author: ftd
'''

class File_constant(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.view_metadata_path = '\\main\\resources\\com\\qad\\erp\\financials\\view\\'
        self.resource_metadata_path = '\\main\\resources\\com\\qad\\erp\\financials\\data\\meta\\'
        self.java_controller_path = '\\main\\java\\com\\qad\\erp\\financials\\'
        self.entity_map_path = '\\main\\resources\\com\\qad\\erp\\financials\\data\\doc\\'
        self.bean_app_context_path = '\\main\\resources\\WEB-INF\\qad\\erp\\financials\\'
        
        self.xml_suffix = ".xml"
        self.resource_metadata_suffix = "-ViewResourceMeta.xml"