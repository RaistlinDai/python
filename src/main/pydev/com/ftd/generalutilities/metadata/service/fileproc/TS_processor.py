'''
Created on Stp 06, 2018

@author: ftd
'''
from src.main.pydev.com.ftd.generalutilities.metadata.service.base.File_processor import File_processor
from src.main.pydev.com.ftd.generalutilities.metadata.service.base.File_constant import File_constant
from pathlib import Path
from src.main.pydev.com.ftd.generalutilities.metadata.service.base.TS_constant import TS_constant
from src.main.pydev.com.ftd.generalutilities.metadata.service.fileproc.Java_processor import Java_processor

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
        
        # get the parent package name
        parent_pack = Java_processor.analysis_dataController_package_name(entityDto.get_dataControllerDTO().get_class_package())
        # get the file full path
        filefullpath = proj_path + fileconstant.RESOURCE_TS_MAIN_PATH + fileconstant.RESOURCE_TS_DTO_UI_FOLDER + filename
        
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
        # ----- write the observable object header -----
        # ------------------------------------------------------- # 
        temp_header = tsconstant.TS_OBSERVABLE_OBJ_HEADER % (parent_pack,business_entity_name.lower(), business_entity_name)
        file.write(temp_header)
        file.write('\n')
        
        
        
        file.write(tsconstant.TS_RIGHT_BRACE)
    
        file.close()
        
        
        return True, None