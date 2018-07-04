'''
Created on Jun 27, 2018

@author: ftd
'''

class FileConstant(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.viewmetadata_path = '\\main\\resources\\com\\qad\\erp\\financials\\view\\'
        self.resourcemetadata_path = '\\main\\resources\\com\\qad\\erp\\financials\\data\\meta\\'
        self.javacontroller_path = '\\main\\java\\com\\qad\\erp\\financials\\'
        self.entitymap_path = '\\main\\resources\\com\\qad\\erp\\financials\\data\\doc\\'
        self.beanappcontext_path = '\\main\\resources\\WEB-INF\\qad\\erp\\financials\\'
        
        self.xml_suffix = ".xml"
        self.resourcemetadata_suffix = "-ViewResourceMeta.xml"