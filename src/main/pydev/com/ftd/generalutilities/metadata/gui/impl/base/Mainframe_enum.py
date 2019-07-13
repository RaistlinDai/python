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
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_projfile_check import Frame_projfile_check
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_ts_handler_option import Frame_ts_handler_option
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_ts_constant_option import Frame_ts_constant_option
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_ts_mock_dto import Frame_ts_mock_dto
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_ts_observable_obj import Frame_ts_observable_obj
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_ts_handler_maint import Frame_ts_handler_maint
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_ts_handler_viewform import Frame_ts_handler_viewform
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_ts_handler_grid import Frame_ts_handler_grid
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_ts_handler_browse import Frame_ts_handler_browse
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.Frame_ts_handler_commonservice import Frame_ts_handler_commonservice

from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.cassandra.Frame_cassandra_startup import Frame_cassandra_startup
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.cassandra.Frame_cassandra_create_connection import Frame_cassandra_create_connection
from src.main.pydev.com.ftd.generalutilities.metadata.gui.impl.frame.cassandra.Frame_cassandra_load_connection import Frame_cassandra_load_connection

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
    PROJFILE_CHECK = [Frame_projfile_check, 'ProjFileCheck']
    TS_HANDLER_OPTION = [Frame_ts_handler_option, 'TSHandler']
    TS_CONSTANT = [Frame_ts_constant_option, 'TSConstants']
    TS_MOCK_DTO = [Frame_ts_mock_dto, 'MockDTO']
    TS_OBSERVABLE_OBJ = [Frame_ts_observable_obj, 'ObservableObj']
    TS_HANDLER_MAINT = [Frame_ts_handler_maint, 'TSMaint']
    TS_HANDLER_VIEWFORM = [Frame_ts_handler_viewform, 'TSViewForm']
    TS_HANDLER_GRID = [Frame_ts_handler_grid, 'TSGrid']
    TS_HANDLER_COMMON = [Frame_ts_handler_commonservice, 'TSCommonService']
    TS_HANDLER_BROWSE =[Frame_ts_handler_browse, 'TSBrowse']
    
    # ===== Cassandra =====
    CASSANDRA_STARTUP = [Frame_cassandra_startup, 'CassandraStartup']
    CASSANDRA_CREATE_CONNECTION = [Frame_cassandra_create_connection, 'CassandraCreateConnection']
    CASSANDRA_LOAD_CONNECTION = [Frame_cassandra_load_connection, 'CassandraLoadConnection']
    