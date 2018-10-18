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
        # imports
        import_list = []
        
        # temp lines
        temp_lines = []
        
        # ------------------------------------------------------- #
        # ----- preparation -----
        # TODO: grid obj
        # ------------------------------------------------------- #
        for ajaxMtd in controller_dto.get_class_methods():
            # skip the method without parameters
            if len(ajaxMtd.get_method_ajax_resp()) == 0:
                continue;
            
            # get the response parameters
            ajax_temp = ''
            for ajaxResp in ajaxMtd.get_method_ajax_resp():
                # convert the java type to TS type
                ajax_para_type_temp = TS_processor.convertJavaTypeToTSType(ajaxResp.get_parameter_type())
                # verify and convert container type
                if ajax_para_type_temp.endswith(fileconstant.JAVA_CONTAINER_SUFFIX):
                    # add import
                    import_name = ajax_para_type_temp[:-9]
                    import_prefix_part = ''
                    import_cells = ajaxResp.get_parameter_import().split(tsconstant.TS_DOT_MARK)
                    idx = 0
                    while idx < len(import_cells):
                        if idx != len(import_cells) -1:
                            import_prefix_part = import_prefix_part + import_cells[idx] + tsconstant.TS_DOT_MARK
                        idx = idx + 1
                        
                    import_temp = tsconstant.TS_OBSERVABLE_OBJ_NAMESPACE_TEMP % (import_name, import_prefix_part, business_entity_name, import_name+'s')
                    import_list.append(tsconstant.TS_TAB + import_temp)
                    
                    # add additional references
                    reference_temp = tsconstant.TS_OBSERVABLE_OBJ_REFERENCE_TEMP % ('bl', import_name)
                    additional_reference.append(reference_temp)
                    
                    # convert the Container type to import name
                    ajax_para_type_temp = import_name
                
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
        # ----- write the imports -----
        # ------------------------------------------------------- # 
        for temp_ref in import_list:
            file.write(temp_ref)
            file.write('\n')
        
        file.write('\n')
        
        # ------------------------------------------------------- #
        # ----- write the observable object content -----
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
    def createMockDTO(entityDto, transDto, filename, isCopy):
        '''
        create Observable Object
        @param copyFromBlDto: if the mock DTO is copied from the generated one
        '''
        #path constant
        fileconstant = File_constant()
        tsconstant = TS_constant()
        proj_path = transDto.get_projectpath()
        controller_dto = entityDto.get_dataControllerDTO()
        
        # get the main table interface name
        main_tb_name = entityDto.get_maintableInterDTO().get_class_name()
        # get the mock ds name
        mock_ds_name = fileconstant.TS_DATASET_PREFIX + main_tb_name + fileconstant.TS_MOCK_DS_SUFFIX + fileconstant.TS_SUFFIX
        
        # get the parent package name
        parent_pack = Java_processor.analysis_dataController_package_name(controller_dto.get_class_package())
        
        # copy from the generated ds
        if isCopy == 1:
            # get the generated ds name
            gene_ds_name = fileconstant.TS_DATASET_PREFIX + main_tb_name + fileconstant.TS_SUFFIX
            
            # get the generated ds full path
            gene_ds_filefullpath = proj_path + fileconstant.RESOURCE_TS_MAIN_PATH + fileconstant.RESOURCE_TS_DTO_BL_FOLDER + gene_ds_name
            # get the mock ds full path
            mock_ds_filefullpath = proj_path + fileconstant.RESOURCE_TS_MAIN_PATH + fileconstant.RESOURCE_TS_DTO_UI_FOLDER + mock_ds_name
            
            if not File_processor.verify_dir_existing(gene_ds_filefullpath):
                # throw error
                return False, 'The DTO %s does not generated in bl folder, please check.' % gene_ds_name
            
            # buffer the content of generated ds
            with open(gene_ds_filefullpath, 'r') as file:
                lines = file.readlines()
            
            # write the mock ds
            if not File_processor.verify_dir_existing(mock_ds_filefullpath):
                # create file
                Path(mock_ds_filefullpath).touch()
            
            # ------------------------------------------------------- #
            # ----- open the mock ds file -----
            # ------------------------------------------------------- #
            newfile = open(mock_ds_filefullpath, 'w')
            
            comment_flag = False
            for line in lines:
                if tsconstant.TS_LEFT_COMMENT in line:
                    comment_flag = True
                elif tsconstant.TS_RIGHT_COMMENT in line:
                    comment_flag = False
                    
                if not comment_flag and tsconstant.TS_COLON in line:
                    line = line.replace(tsconstant.TS_COLON, tsconstant.TS_QUESTION_MARK + tsconstant.TS_COLON)
                    newfile.write('\n')
                    
            newfile.close()
            
        return True, None
        