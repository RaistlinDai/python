'''
Created on Jul 5, 2018

@author: ftd
'''
from enum import Enum, unique
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_load_dir import Frame_load_dir
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_maint_gene import Frame_maint_gene
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_xml_option import Frame_xml_option

@unique
class FrameEnum(Enum):
    '''
    classdocs
    '''

    LOAD_DIR = Frame_load_dir
    MAINT_GENE = Frame_maint_gene
    XML_OPTION = Frame_xml_option
    
    
