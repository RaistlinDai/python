'''
Created on Stp 06, 2018

@author: ftd
'''
from src.main.pydev.com.ftd.generalutilities.metadata.service.base.File_processor import File_processor
from src.main.pydev.com.ftd.generalutilities.metadata.service.base.File_constant import File_constant
from pathlib import Path
from src.main.pydev.com.ftd.generalutilities.metadata.service.base.TS_constant import TS_constant
from src.main.pydev.com.ftd.generalutilities.metadata.service.fileproc.Java_processor import Java_processor
from src.main.pydev.com.ftd.generalutilities.metadata.service.base.Java_constant import Java_constant

class TS_processor(File_processor):
    '''
    This class is used to process the Typescript files
    '''
    
    @staticmethod
    def create_TS_ObserObj(entityDto, transDto, filename):
        '''
        create Observable Object
        '''
        #path constant
        fileconstant = File_constant()
        tsconstant = TS_constant()
        business_entity_name = entityDto.get_businessentityname()
        proj_path = transDto.get_projectpath()
        controller_dto = entityDto.get_dataControllerDTO()
        
        # get the parent package name
        parent_pack = Java_processor.analysis_dataController_package_name(controller_dto.get_class_package())
        # get the file full path
        filefullpath = proj_path + fileconstant.RESOURCE_TS_MAIN_PATH + fileconstant.RESOURCE_TS_DTO_UI_FOLDER + filename
        # additional references
        additional_reference = []
        
        # temp lines
        temp_lines = []
        
        # ------------------------------------------------------- #
        # ----- preparation -----
        # ------------------------------------------------------- #
        for ajaxMtd in controller_dto.get_class_methods():
            # get the response parameters
            ajax_temp = ''
            for ajaxResp in ajaxMtd.get_method_ajax_resp():
                # convert the java type to TS type
                ajax_para_type_temp = TS_processor.convertJavaTypeToTSType(ajaxResp.get_parameter_type())
                # verify and convert container type
                if ajax_para_type_temp.startswith(File_constant.JAVA_QRA_PREFIX) and ajax_para_type_temp.endswith(File_constant.JAVA_CONTAINER_SUFFIX):
                    print(ajax_para_type_temp)
                
                ajax_temp = ajax_temp + '\n' + tsconstant.TS_TAB + tsconstant.TS_TAB + ajaxResp.get_parameter_name() + ': ' + ajax_para_type_temp + tsconstant.TS_END_MARK
            
            ajaxMtd_name = ajaxMtd.get_method_name()
            ajaxMtd_name = ajaxMtd_name[:1].upper() + ajaxMtd_name[1:]
            line = tsconstant.TS_TAB + tsconstant.TS_OBSERVABLE_OBJ_RESPONSE_TEMPLATE % (ajaxMtd_name,ajax_temp)
            
            temp_lines.append(line)
            temp_lines.append('\n')
        
        
        if not File_processor.verify_dir_existing(filefullpath):
            # create file
            Path(filefullpath).touch()
        
        # ------------------------------------------------------- #
        # ----- open the observable object file -----
        # ------------------------------------------------------- #
        file = open(filefullpath, 'w')
    
        # ------------------------------------------------------- #
        # ----- write the common references -----
        # ------------------------------------------------------- # 
        for temp_ref in tsconstant.TS_REFERENCE_COMMON_REFERENCES:
            file.write(temp_ref)
            file.write('\n')
        
        # ------------------------------------------------------- #
        # ----- write the common references -----
        # ------------------------------------------------------- # 
        for temp_ref in additional_reference:
            file.write(temp_ref)
            file.write('\n')
        
        file.write('\n')
        
        
        # ------------------------------------------------------- #
        # ----- write the observable object header -----
        # ------------------------------------------------------- # 
        temp_header = tsconstant.TS_OBSERVABLE_OBJ_HEADER % (parent_pack,business_entity_name.lower(), business_entity_name)
        file.write(temp_header)
        file.write('\n')
        
        # ------------------------------------------------------- #
        # ----- write the observable object header -----
        # ------------------------------------------------------- # 
        for sub_line in temp_lines:
            file.write(sub_line)
        
        file.write(tsconstant.TS_RIGHT_BRACE)
    
        file.close()
        
        return True, None
    
    
    @staticmethod
    def convertJavaTypeToTSType(javaType):
        '''
        convert the java type to TS type
        '''
        javaconstant = Java_constant()
        tsconstant = TS_constant()
        
        if not javaType:
            return None
        # string
        if javaType == javaconstant.JAVA_TYPE_STRING:
            return tsconstant.TS_TYPE_STRING
        # number
        elif javaType in [javaconstant.JAVA_TYPE_INTEGER,javaconstant.JAVA_TYPE_BIGDECIMAL,javaconstant.JAVA_TYPE_LONG]:
            return tsconstant.TS_TYPE_NUMBER
        # boolean
        elif javaType == javaconstant.JAVA_TYPE_BOOLEAN:
            return tsconstant.TS_TYPE_BOOLEAN
        # date
        elif javaType == javaconstant.JAVA_TYPE_GREGORIANCALENDAR:
            return tsconstant.TS_TYPE_BOOLEAN
        else:
            return javaType
    
    
    @staticmethod
    def convertContainerTypeToTSType(containerType):
        '''
        
        
        '''
        