'''
Created on Jun 21, 2018

@author: ftd
'''
import os
import xml.dom.minidom
from src.main.pydev.com.ftd.generalutilities.metadata.service.File_constant import File_constant
from src.main.pydev.com.ftd.generalutilities.metadata.dto.xmlFile.resourcemetadata.ResourceMetadataDTO import ResourceMetadataDTO
from src.main.pydev.com.ftd.generalutilities.metadata.dto.xmlFile.beanappcontext.BeanAppContext import BeanAppContext

class File_reader(object):
    '''
    classdocs
    '''
    
    @staticmethod
    def read_dir(dirpath):
        try:
            dir_existing = False
            fileconstant = File_constant()
            #view metadata file list
            viewMetadataNames = {}
            
            #change the work path
            os.chdir(dirpath)
            #go through the inner files
            for fullname in File_reader.iterbrowse(dirpath):
                #get the view metadata files
                if (fullname.startswith(dirpath + fileconstant.VIEW_METADATA_PATH)):
                    #trim the file name
                    filename=os.path.basename(fullname)
                    #remove the suffix
                    filename = filename[:-4]
                    #insert into file list
                    viewMetadataNames[filename] = fullname
            
            #no files
            if len(viewMetadataNames) == 0:
                return False, None, 'There is no correct view metadata.'
            
            return True, viewMetadataNames, None
        
        except OSError as e:
            print('expect:', e)
            return False, None, e
        except FileNotFoundError as e:
            print('expect:', e)
            return False, None, e
        finally:
            pass
        
    
    #get the inner files (full path)
    @staticmethod
    def iterbrowse(path):
        for home, dirs, files in os.walk(path):
            for filename in files:
                #generator
                yield os.path.join(home, filename)
                
    
    @staticmethod
    def read_resource_metadata(path, file_dto):
        # verify if file is existing
        if not File_reader.verify_file(path):
            return False
        
        #get the root of resource metadata
        dom = xml.dom.minidom.parse(path)
        root = dom.documentElement
        #elements=root.getElementsByTagName('element')
        
        #create new resource dto
        resDto = ResourceMetadataDTO()
        
        #root node information
        if root.nodeName == 'ViewResourceMetadata':
            resDto.update_header(root.getAttribute('MetaUri'), 
                                 root.getAttribute('ViewUri'), 
                                 root.getAttribute('NameStringCode'), 
                                 root.getAttribute('IsEligibleForMenu'), 
                                 root.getAttribute('IsSecure'), 
                                 root.getAttribute('PrimarySecureUri'))
            
        #print(root.childNodes)
        
        #update the ResourceMetadataDTO in FileDTOSet
        file_dto.set_resourceDTO(resDto)
    
    
    @staticmethod
    def read_bean_app_context(path):
        # verify if file is existing
        if not File_reader.verify_file(path):
            return None, False
        
        #get the root of resource metadata
        bean_app = BeanAppContext()
        dom = xml.dom.minidom.parse(path)
        for node in dom.getElementsByTagName('bean'):
            bean_app.set_bean_id(node.getAttribute('id'))
            bean_app.set_bean_class(node.getAttribute('class'))
            break
            
        for node in dom.getElementsByTagName('property'):
            node_name = node.getAttribute('name')
            if node_name == 'entityUriMapString':
                bean_app.set_entity_uri_mapstring(node.getAttribute('value'))
            elif node_name == 'labelService':
                bean_app.set_label_service(node.getAttribute('value'))
            elif node_name == 'entityMetadataService':
                bean_app.set_entity_metadata_service(node.getAttribute('value'))
            elif node_name == 'viewMetadataService':
                bean_app.set_view_metadata_service(node.getAttribute('value'))
                
        return bean_app, True
            
    
    @staticmethod
    def verify_file(path):
        return os.path.exists(path)
    
    
    