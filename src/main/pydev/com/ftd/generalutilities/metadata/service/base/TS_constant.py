'''
Created on Sep 6, 2018

@author: ftd
'''

class TS_constant(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
        # TS end flag
        self.TS_END_MARK = ';'
        self.TS_SEPERATOR = ','
        self.TS_DOT_MARK = '.'
        self.TS_RIGHT_BRACKET = ')'
        self.TS_LEFT_BRACKET = '('
        self.TS_RIGHT_BRACE = '}'
        self.TS_LEFT_BRACE = '{'
        self.TS_LEFT_COMMENT = '/*'
        self.TS_RIGHT_COMMENT = '*/'
        self.TS_LEFT_DASH = '<'
        self.TS_RIGHT_DASH = '>'
        self.TS_TAB = '\t'
        
        # common references
        self.TS_REFERENCE_COMMON_ANGULAR = '/// <reference path="../../../../../../Lib/DefinitelyTyped/angular/angular.d.ts" />'
        self.TS_REFERENCE_COMMON_JQUERY = '/// <reference path="../../../../../../Lib/DefinitelyTyped/jquery/jquery.d.ts" />'
        self.TS_REFERENCE_COMMON_KENDO = '/// <reference path="../../../../../../Lib/kendo/kendo.all.d.ts" />'
        self.TS_REFERENCE_COMMON_UTILS = '/// <reference path="../../../../../../Lib/Qad/utils.d.ts" />'
        self.TS_REFERENCE_COMMON_QADTS = '/// <reference path="../../../../../../qad-ts.d.ts" />'
        
        self.TS_REFERENCE_COMMON_REFERENCES = [self.TS_REFERENCE_COMMON_ANGULAR,
                                               self.TS_REFERENCE_COMMON_JQUERY,
                                               self.TS_REFERENCE_COMMON_KENDO,
                                               self.TS_REFERENCE_COMMON_UTILS,
                                               self.TS_REFERENCE_COMMON_QADTS]
        
        # observable object header
        self.TS_OBSERVABLE_OBJ_HEADER = 'module com.qad.financials.%s.%s.TSHandler.%s.DTO.UI {\n\t\'use strict\';\n'
        
        