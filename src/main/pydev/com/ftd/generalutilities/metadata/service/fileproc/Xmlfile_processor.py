'''
Created on Jun 21, 2018

@author: ftd
'''
import os
import xml.dom.minidom
from src.main.pydev.com.ftd.generalutilities.metadata.service.base.File_constant import File_constant
from src.main.pydev.com.ftd.generalutilities.metadata.dto.xmlFile.resourcemetadata.ResourceMetadataDTO import ResourceMetadataDTO
from src.main.pydev.com.ftd.generalutilities.metadata.dto.xmlFile.beanappcontext.BeansAppContextDTO import BeansAppContextDTO
from src.main.pydev.com.ftd.generalutilities.metadata.service.base.File_processor import File_processor
import xml.etree.ElementTree as ElementTree
from src.main.pydev.com.ftd.generalutilities.metadata.dto.xmlFile.entitymap import EntityMapDTO

class Xmlfile_processor(File_processor):
    '''
    classdocs
    '''

#------------------------ Reader ------------------

    @staticmethod
    def read_proj_dir(dirpath):
        try:
            fileconstant = File_constant()
            #view metadata file list
            viewMetadataNames = {}
            
            #change the work path
            os.chdir(dirpath)
            #go through the inner files
            for fullname in Xmlfile_processor.iterbrowse(dirpath):
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
        if not File_processor.verify_dir_existing(path):
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
        '''
        read the beans-app-context.xml file by dom, and load the details into BeansAppContextDTO
        @param path: the full path of beans-app-context.xml
        @return: return status
        @return: BeansAppContextDTO
        @return: message if validation failed
        '''
        # verify if file is existing
        if not File_processor.verify_dir_existing(path):
            return False, None, 'The beans-app-context is not exist, please check.'
        
        #get the root of resource metadata
        bean_app = BeansAppContextDTO()
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
                
        return True, bean_app, None
        
    
    @staticmethod
    def write_bean_app_context(path, value):
        '''
        write the beans-app-context.xml file
        @param path: the full path of beans-app-context.xml
        @param propname: property node name
        @param propvalue: property node value
        @return: return status
        @return: message if validation failed
        '''
        # verify if file is existing
        if not File_processor.verify_dir_existing(path):
            return False, 'The beans-app-context is not exist, please check.'
        
        #get the root of resource metadata
        linecontents = []
        entityuri_start, entityuri_end, value_start = -1, -1, -1
        
        with open(path, "r", encoding="utf-8") as f:
            for cur_line_number, line in enumerate(f):
                linecontents.append(line)
                if 'name=\"entityUriMapString\"' in line:
                    entityuri_start = cur_line_number
                if 'value=' in line and entityuri_start > -1 and value_start == -1 and cur_line_number >= entityuri_start:
                    value_start = cur_line_number
                if '\"/>' in line and entityuri_start > -1 and entityuri_end == -1 and cur_line_number >= entityuri_start:
                    entityuri_end = cur_line_number
        f.close()
        
        if entityuri_start == -1 or entityuri_end == -1:
            return False, 'The file format of beans-app-context.xml is incorrect, cannot find \'entityUriMapString\''
        
        try:
            # --- the node in a single line
            if entityuri_start == entityuri_end or value_start == entityuri_end:
                idxarr = linecontents[entityuri_end].index('\"/>')
                linecontents[entityuri_end] = linecontents[entityuri_end][:idxarr].rstrip(' ') + ';'+value + linecontents[entityuri_end][idxarr:]            
            else:
                strtrim = linecontents[entityuri_end].replace('\"/>', '').replace('\t', '').replace('\n', '').strip(' ')
                # --- the end flag in a single line
                if strtrim == '':
                    # --- add ';' in previous line
                    idxarr = linecontents[entityuri_end-1].index('\n')
                    linecontents[entityuri_end-1] = linecontents[entityuri_end-1][:idxarr].rstrip(' ') + ';\n'
                    # --- clone the tab format in previous line
                    tabpre = ''
                    if (entityuri_end-1 != value_start):
                        tabpre = linecontents[entityuri_end-1][:linecontents[entityuri_end-1].index('urn')]
                    # --- insert new line
                    value = tabpre + value + '\n'
                    linecontents.insert(entityuri_end, value)
                else:
                    idxarr = linecontents[entityuri_end].index('\"/>')
                    linesuf = linecontents[entityuri_end][idxarr:]
                    # --- only one uri in the last line
                    if len(linecontents[entityuri_end].split(';')) == 1:
                        linecontents[entityuri_end] = linecontents[entityuri_end][:idxarr].rstrip(' ') + ';\n'
                        # --- clone the tab format in current line
                        tabpre = linecontents[entityuri_end][:linecontents[entityuri_end].index('urn')]
                        # --- insert new line
                        value = tabpre + value + linesuf
                        linecontents.insert(entityuri_end+1, value)
                    else:
                        # --- add the new uri at the end of this line
                        linecontents[entityuri_end] = linecontents[entityuri_end][:idxarr].rstrip(' ') + ';'+value+ linecontents[entityuri_end][idxarr:]
        except ValueError as e:
            return False, e
        
        newfile = ''.join(linecontents)
        f = open(path, "w", encoding="utf-8")
        try:
            f.write(newfile)
            
        except PermissionError as e:
            return False, e
        finally:
            f.close()
        
        del linecontents[:] 
        return True, None

    
    @staticmethod
    def read_entity_map(path):
        '''
        read the entityMap.xml file, and load the details into entityMap
        @param path: the directory of entityMap.xml
        @return: return status
        @return: BeansAppContextDTO
        @return: message if validation failed
        '''
        # verify if file is existing
        if not File_processor.verify_dir_existing(path):
            return False, None, 'The entityMap.xml is not exist, please check.'
        
        #get the root of entityMap.xml
        tree = ElementTree.parse('C:\\Ftd-work\\entityMap.xml')
        root = tree.getroot()
        
        ent_maps = EntityMapDTO()
        
        try:
            for ent in root.findall('EntityMap'):
                urn = ent.find('urn').text
                urn_type = ent.find('type').text
                obj_name = ent.find('objectName').text
                pan_domain = ent.find('panDomain').text
                
                ent_maps.add_entitymap(urn, urn_type, obj_name, pan_domain)
        
            return True, ent_maps, None
        except AttributeError:
            return False, None, 'The file format of entityMap.xml is incorrect, please check.'
        
        
        
        