'''
Created on Oct 22, 2018

@author: ftd
'''

class Xml_constant(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
        # TS end flag
        self.XML_NODE_FIELD = 'Field'
        self.XML_NODE_LABEL = 'Label'
        self.XML_NODE_DATAGRID = 'DataGrid'
        self.XML_NODE_DATAGRIDTABLE = 'DataGridTable'
        self.XML_NODE_DATAGRIDFIELD = 'DataGridField'
        
        self.XML_NODE_PROP_NAME = 'Name'
        self.XML_NODE_PROP_TABLENAME = 'TableName'
        self.XML_NODE_PROP_FIELDNAME = 'FieldName'
        self.XML_NODE_PROP_READONLY = 'ReadOnly'
        
        self.XML_COMMA = '\"'