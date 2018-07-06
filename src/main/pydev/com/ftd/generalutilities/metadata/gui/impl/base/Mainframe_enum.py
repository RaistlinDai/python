'''
Created on Jul 5, 2018

@author: ftd
'''
from enum import Enum, unique
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_load_dir import Frame_load_dir
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_gene_selection import Frame_gene_selection
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_xml_option import Frame_xml_option
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_controller_option import Frame_controller_option
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_serviceimpl_option import Frame_serviceimpl_option
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_startup import Frame_startup

@unique
class Mainframe_enum(Enum):
    '''
    classdocs
    @attention: the value structure: [frame class constructor, frame short name]
    '''

    START_UP = [Frame_startup, 'StartUp']
    LOAD_DIR = [Frame_load_dir, 'LoadFromDirectory']
    GENE_SELECTION = [Frame_gene_selection, 'GeneratorSelection']
    XML_OPTION = [Frame_xml_option, 'EntityMap & BeanAppContext']
    CONTROLLER_OPTION = [Frame_controller_option, 'DataController']
    SERVICEIMPL_OPTION = [Frame_serviceimpl_option, 'ServiceImpl']