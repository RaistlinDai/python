'''
Created on Jun 21, 2018

@author: ftd
'''
import os
import xml.dom.minidom
from src.main.pydev.com.ftd.generalutilities.metadata.service.base.File_constant import File_constant
from src.main.pydev.com.ftd.generalutilities.metadata.dto.xmlFile.resourcemetadata.ResourceMetadataDTO import ResourceMetadataDTO,\
    ViewParametersDTO, KeyField
from src.main.pydev.com.ftd.generalutilities.metadata.dto.xmlFile.viewmetadata.ViewMetadataDTO import ViewMetadataDTO
from src.main.pydev.com.ftd.generalutilities.metadata.dto.xmlFile.viewmetadata.Datafield import Datafield
from src.main.pydev.com.ftd.generalutilities.metadata.dto.xmlFile.viewmetadata.Datalabel import Datalabel
from src.main.pydev.com.ftd.generalutilities.metadata.dto.xmlFile.viewmetadata.Datagrid import Datagrid
from src.main.pydev.com.ftd.generalutilities.metadata.dto.xmlFile.viewmetadata.Datagridtable import Datagridtable
from src.main.pydev.com.ftd.generalutilities.metadata.dto.xmlFile.viewmetadata.Datagridfield import Datagridfield
from src.main.pydev.com.ftd.generalutilities.metadata.dto.xmlFile.beanappcontext.BeansAppContextDTO import BeansAppContextDTO
from src.main.pydev.com.ftd.generalutilities.metadata.service.base.File_processor import File_processor
import xml.etree.ElementTree as ElementTree
from src.main.pydev.com.ftd.generalutilities.metadata.dto.xmlFile.entitymap.EntityMapDTO import EntityMaps,\
    EntityMap
from src.main.pydev.com.ftd.generalutilities.metadata.dto.xmlFile.pom.PomDTO import PomDTO
from pyexpat import ExpatError
from src.main.pydev.com.ftd.generalutilities.metadata.service.base.Xml_constant import Xml_constant

class Xmlfile_processor(File_processor):
    '''
    classdocs
    '''

    @staticmethod
    def verify_xml_type(dir_path):
        '''
        verify the jar file type
        @param dir_path: file directory
        @return: return status
        @return: message if validation failed
        '''
        if not File_processor.verify_dir_existing(dir_path):
            return False, "File not exist!"
        
        ftype = Xmlfile_processor.get_file_type(dir_path)
                
        if ftype == 'unknown':
            return False, 'The file type is unknown!'
        
        if ftype != 'xml':
            return False, 'The file type(%s) is not (xml) !' % ftype
        
        return True, None
    
    
#------------------ Reader project directory ------------------
    @staticmethod
    def read_proj_dir(dir_path):
        '''
        read the all view metadata xml files from the project directory
        @param dir_path: the full path of the project
        @return: return status
        @return: viewMetadataNames in list
        @return: message if validation failed
        '''
        # verify if file is existing
        if not File_processor.verify_dir_existing(dir_path):
            return False, None, "File not exist!"
        
        try:
            fileconstant = File_constant()
            #view metadata file list
            viewMetadataNames = {}
            
            #change the work path
            os.chdir(dir_path)
            #go through the inner files
            for fullname in File_processor.dir_iterbrowse(dir_path):
                #get the view metadata files
                if (fullname.startswith(dir_path + fileconstant.VIEW_METADATA_PATH)):
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
            print('Caught exception:', e.message())
            return False, None, e.message()
        except FileNotFoundError as e:
            print('Caught exception:', e.message())
            return False, None, e.message()
        finally:
            pass
        

#---------------- view metadata.xml --------------------------
    @staticmethod
    def veriy_view_metadata(dir_path):
        '''
        read the target view metadata xml file by dom
        @param dir_path: the full path of view metadata
        @return: return status
        @return: message if validation failed
        '''
        # verify if file is existing
        if not File_processor.verify_dir_existing(dir_path):
            return False, "The view metadata is not exist, please check."
        
        #get the root of resource metadata
        try:
            dom = xml.dom.minidom.parse(dir_path)
            root = dom.documentElement
            if not root.nodeName == 'QADView':
                return False, 'This is not a valid view metadata, please check.'
        except ExpatError:
            return False, 'This is not a valid xml file, please check.'
            
        return True, None
        
        
    @staticmethod
    def read_view_metadata(file_dto):
        '''
        read the target view metadata xml file by dom, and load the details into ViewMetadataDTO
        @param dir_path: the full path of view metadata
        @return: return status
        @return: message if validation failed
        '''
        Xmlconstant = Xml_constant()
        
        # verify if file is existing
        if not File_processor.verify_dir_existing(file_dto.get_viewfullpath()):
            return False, "The view metadata is not exist, please check."
        
        #get the root of view metadata
        dom = xml.dom.minidom.parse(file_dto.get_viewfullpath())
        
        #create new resource dto
        viewDto = ViewMetadataDTO()
        
        # add field node into ViewMetadata DTO
        fields = dom.getElementsByTagName(Xmlconstant.XML_NODE_FIELD)
        for field in fields:
            dtField = Datafield()
            
            if field.getAttribute(Xmlconstant.XML_NODE_PROP_NAME):
                dtField.set_name(field.getAttribute(Xmlconstant.XML_NODE_PROP_NAME))
            
            if field.getAttribute(Xmlconstant.XML_NODE_PROP_TABLENAME):
                dtField.set_tablename(field.getAttribute(Xmlconstant.XML_NODE_PROP_TABLENAME))
            
            viewDto.push_datafields(dtField)
        
        # add label node into ViewMetadata DTO
        labels = dom.getElementsByTagName(Xmlconstant.XML_NODE_LABEL)
        for label in labels:
            dtLabel = Datalabel()
            
            if label.getAttribute(Xmlconstant.XML_NODE_PROP_NAME):
                dtLabel.set_name(label.getAttribute(Xmlconstant.XML_NODE_PROP_NAME))
            
            viewDto.push_datalabels(dtLabel)
        
        # add label node into ViewMetadata DTO
        datagrids = dom.getElementsByTagName(Xmlconstant.XML_NODE_DATAGRID)
        for datagrid in datagrids:
            dtGrid = Datagrid()
            
            if datagrid.getAttribute(Xmlconstant.XML_NODE_PROP_NAME):
                dtGrid.set_name(datagrid.getAttribute(Xmlconstant.XML_NODE_PROP_NAME))
            
            if datagrid.getAttribute(Xmlconstant.XML_NODE_PROP_TABLENAME):
                dtGrid.set_tablename(datagrid.getAttribute(Xmlconstant.XML_NODE_PROP_TABLENAME))
            
            # add DataGridTable into DataTable node
            datagridtables = datagrid.getElementsByTagName(Xmlconstant.XML_NODE_DATAGRIDTABLE)
            if len(datagridtables) == 0:
                return False, 'The DataGrid structure is incorrect without table!'
            
            dtGridTable = Datagridtable()
            
            if datagridtables[0].getAttribute(Xmlconstant.XML_NODE_PROP_NAME):
                dtGridTable.set_name(datagridtables[0].getAttribute(Xmlconstant.XML_NODE_PROP_NAME))
                    
            # add DataGridField into DataGridTable            
            datagridfields = datagridtables[0].getElementsByTagName(Xmlconstant.XML_NODE_DATAGRIDFIELD)
            for datagridfield in datagridfields:
                
                dtGridfield = Datagridfield()
                
                if datagridfield.getAttribute(Xmlconstant.XML_NODE_PROP_FIELDNAME):
                    dtGridfield.set_fieldname(datagridfield.getAttribute(Xmlconstant.XML_NODE_PROP_FIELDNAME)) 
                
                if datagridfield.getAttribute(Xmlconstant.XML_NODE_PROP_READONLY):
                    dtGridfield.set_readonly(datagridfield.getAttribute(Xmlconstant.XML_NODE_PROP_READONLY))
                    
                dtGridTable.push_datagridfield(dtGridfield)
            
            dtGrid.set_datagridtable(dtGridTable)    
            viewDto.push_datagrids(dtGrid)
        
        #update the ViewMetadataDTO in FileDTOSet
        if file_dto:
            file_dto.set_viewDTO(viewDto)
            
        return True, None
        

#---------------- resource metadata.xml --------------------------
    @staticmethod
    def veriy_resource_metadata(dir_path):
        '''
        read the target resource metadata xml file by dom
        @param dir_path: the full path of resource metadata
        @return: return status
        @return: message if validation failed
        '''
        # verify if file is existing
        if not File_processor.verify_dir_existing(dir_path):
            return False, "The resource metadata is not exist, please check."
        
        #get the root of resource metadata
        try:
            dom = xml.dom.minidom.parse(dir_path)
            root = dom.documentElement
            if not root.nodeName == 'ViewResourceMetadata':
                return False, 'This is not a valid resource metadata, please check.'
        except ExpatError:
            return False, 'This is not a valid xml file, please check.'
        
        return True, None
        
    
    @staticmethod
    def read_resource_metadata(dir_path, file_dto):
        '''
        read the target resource metadata xml file by dom, and load the details into ResourceMetadataDTO
        @param dir_path: the full path of resource metadata
        @return: return status
        @return: message if validation failed
        '''
        # verify if file is existing
        if not File_processor.verify_dir_existing(dir_path):
            return False, "The resource metadata is not exist, please check."
        
        #get the root of resource metadata
        dom = xml.dom.minidom.parse(dir_path)
        root = dom.documentElement
        #elements=root.getElementsByTagName('element')
        
        #create new resource dto
        resDto = ResourceMetadataDTO()
        
        #root node information
        if root.nodeName == 'ViewResourceMetadata':
            prim_uri = root.getAttribute('PrimarySecureUri')
            if prim_uri.index(resDto.ENTITY_TYPE_BE) >= 0:
                entity_type = 'BE'
            elif prim_uri.index(resDto.ENTITY_TYPE_SERVICE) >= 0:
                entity_type = 'Service'
            else:
                entity_type = None
            
            resDto.update_header(root.getAttribute('MetaUri'), 
                                 root.getAttribute('ViewUri'), 
                                 root.getAttribute('NameStringCode'), 
                                 root.getAttribute('IsEligibleForMenu'), 
                                 root.getAttribute('IsSecure'), 
                                 prim_uri,
                                 entity_type)
            
            # --- HybridBrowseView ---
            
            
            # --- BrowseView ---
            
            
            # --- MaintView ---
            
            
            # --- ViewParameters ---
            tempViewDto = ViewParametersDTO()
            views = dom.getElementsByTagName("ViewParameters")
            for view in views:
                if len(view.getElementsByTagName("EntityModule")) > 0 and view.getElementsByTagName("EntityModule")[0].firstChild:
                    tempViewDto.set_entity_module(view.getElementsByTagName("EntityModule")[0].firstChild.data)
                if len(view.getElementsByTagName("StoredViewKey")) > 0 and view.getElementsByTagName("StoredViewKey")[0].firstChild:
                    tempViewDto.set_stored_view_key(view.getElementsByTagName("StoredViewKey")[0].firstChild.data)
                if len(view.getElementsByTagName("UsesDomain")) > 0 and view.getElementsByTagName("UsesDomain")[0].firstChild:
                    tempViewDto.set_uses_domain(view.getElementsByTagName("UsesDomain")[0].firstChild.data)
                if len(view.getElementsByTagName("ResourceUrlPrefix")) > 0 and view.getElementsByTagName("ResourceUrlPrefix")[0].firstChild:
                    tempViewDto.set_resource_url_prefix(view.getElementsByTagName("ResourceUrlPrefix")[0].firstChild.data)
                if len(view.getElementsByTagName("DataResource")) > 0 and view.getElementsByTagName("DataResource")[0].firstChild:
                    tempViewDto.set_data_resource(view.getElementsByTagName("DataResource")[0].firstChild.data)
                if len(view.getElementsByTagName("Table")) > 0 and view.getElementsByTagName("Table")[0].firstChild:
                    tempViewDto.set_table(view.getElementsByTagName("Table")[0].firstChild.data)
                    print(tempViewDto.get_table())
                if len(view.getElementsByTagName("KeyFields")) > 0:
                    firstkeys = view.getElementsByTagName("KeyFields")[0]
                    for subkey in firstkeys.getElementsByTagName("KeyField"):
                        keyDto = KeyField()
                        if len(subkey.getElementsByTagName("BrowseKeyField")) > 0 and subkey.getElementsByTagName("BrowseKeyField")[0].firstChild:
                            keyDto.set_browse_key_field(subkey.getElementsByTagName("BrowseKeyField")[0].firstChild.data)
                        if len(subkey.getElementsByTagName("EntityKeyField")) > 0 and subkey.getElementsByTagName("EntityKeyField")[0].firstChild:
                            keyDto.set_entity_key_field(subkey.getElementsByTagName("EntityKeyField")[0].firstChild.data)
                        if len(subkey.getElementsByTagName("IsParentForeignKey")) > 0 and subkey.getElementsByTagName("IsParentForeignKey")[0].firstChild:
                            keyDto.set_is_parent_foreign_key(subkey.getElementsByTagName("IsParentForeignKey")[0].firstChild.data)
                            
                        tempViewDto.push_key_field(keyDto)
            
            resDto.set_view_parameters(tempViewDto)
                    
        else:
            return False, 'This is not a valid resource metadata, please check.'
        
        #print(root.childNodes)
        
        #update the ResourceMetadataDTO in FileDTOSet
        if file_dto:
            file_dto.set_resourceDTO(resDto)
        
        return True, None
    

#---------------- beans-app-context.xml --------------------------
    @staticmethod
    def verify_beans_app_context(dir_path):
        '''
        verify the beans-app-context.xml file by dom
        @param dir_path: the full path of beans-app-context.xml
        @return: return status
        @return: message if validation failed
        '''
        # verify if file is existing
        if not File_processor.verify_dir_existing(dir_path):
            return False, 'The beans-app-context is not exist, please check.'
        
        #get the root of resource metadata
        try:
            dom = xml.dom.minidom.parse(dir_path)
            if len(dom.getElementsByTagName('bean')) == 0:
                return False, 'This is not a valid beans-app-context.xml, please check.'
        except ExpatError:
            return False, 'This is not a valid xml file, please check.'
        
        return True, None
        

    @staticmethod
    def read_beans_app_context(path):
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
    def write_beans_app_context(dir_path, value):
        '''
        write the beans-app-context.xml file
        @param dir_path: the full path of beans-app-context.xml
        @param value: append value
        @return: return status
        @return: message if validation failed
        '''
        # verify if file is existing
        if not File_processor.verify_dir_existing(dir_path):
            return False, 'The beans-app-context is not exist, please check.'
        
        #get the root of resource metadata
        linecontents = []
        entityuri_start, entityuri_end, value_start = -1, -1, -1
        
        with open(dir_path, "r", encoding="utf-8") as f:
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
        f = open(dir_path, "w", encoding="utf-8")
        try:
            f.write(newfile)
            
        except PermissionError as e:
            return False, e
        finally:
            f.close()
        
        del linecontents[:] 
        return True, None

    
#---------------- entityMap.xml --------------------------
    @staticmethod
    def verify_entity_map(dir_path):
        '''
        verify the entityMap.xml file
        @param dir_path: the directory of entityMap.xml by dom
        @return: return status
        @return: message if validation failed
        '''
        # verify if file is existing
        if not File_processor.verify_dir_existing(dir_path):
            return False, 'The entityMap is not exist, please check.'
        
        try:
            dom = xml.dom.minidom.parse(dir_path)
            root = dom.documentElement
            if not root.nodeName == 'EntityMaps':
                return False, 'This is not a valid entityMap.xml, please check.'
        except ExpatError:
            return False, 'This is not a valid xml file, please check.'
        
        return True, None
    

    @staticmethod
    def read_entity_map(dir_path):
        '''
        read the entityMap.xml file, and load the details into entityMapDTO
        @param dir_path: the directory of entityMap.xml by ElementTree
        @return: return status
        @return: BeansAppContextDTO
        @return: message if validation failed
        '''
        # verify if file is existing
        if not File_processor.verify_dir_existing(dir_path):
            return False, None, 'The entityMap.xml is not exist, please check.'
        
        #get the root of entityMap.xml
        tree = ElementTree.parse(dir_path)
        root = tree.getroot()
        ent_maps = EntityMaps()
        
        for ent in root.findall('EntityMap'):
            for child in ent:
                if child.tag == 'urn':
                    urn = child.text
                elif child.tag == 'type':
                    urn_type = child.text
                elif child.tag == 'objectName':
                    obj_name = child.text
                elif child.tag == 'panDomain':
                    pan_domain = child.text
            
            if not urn or not urn_type or not obj_name or not pan_domain:
                return False, None, 'The file format of entityMap.xml is incorrect, please check.'
            
            ent = EntityMap(urn, urn_type, obj_name, pan_domain)
            ent_maps.add_entitymap(ent)
            
        return True, ent_maps, None
    
    
    @staticmethod
    def write_entity_map(dir_path, urn, urn_type, object_name, pan_domain):   
        '''
        write the entityMap.xml file
        @param dir_path: the full path of entityMap.xml
        @param urn: the new urn
        @param urn_type: the new urn_type
        @param object_name: the new object_name
        @param pan_domain: the new pan_domain
        @return: return status
        @return: message if validation failed
        '''
        # verify if file is existing
        if not File_processor.verify_dir_existing(dir_path):
            return False, None, 'The entityMap.xml is not exist, please check.'
        
        #get the root of entityMap
        linecontents = []
        entityuri_start, entityuri_end, file_end = -1, -1, -1
        
        with open(dir_path, "r", encoding="utf-8") as f:
            for cur_line_number, line in enumerate(f):
                linecontents.append(line)
                if '<EntityMap>' in line:
                    entityuri_start = cur_line_number
                if '</EntityMap>' in line and cur_line_number >= entityuri_start:
                    entityuri_end = cur_line_number
                if '</EntityMaps>' in line:
                    file_end = cur_line_number
        f.close()
        
        if entityuri_start == -1 or entityuri_end == -1:
            return False, 'The file format of entityMap.xml is incorrect, cannot find \'EntityMap\''
        
        try:
            # --- add a blank line
            linecontents.insert(file_end, '\n')
            # --- get the prefix from the last EntityMap node
            linepre = linecontents[entityuri_start][:linecontents[entityuri_start].index('<EntityMap>')]
            # --- add new EntityMap node
            linecontents.insert(file_end+1, linepre+'<EntityMap>\n')
            linecontents.insert(file_end+2, linepre+'\t<urn>'+urn+'</urn>\n')
            linecontents.insert(file_end+3, linepre+'\t<type>'+urn_type+'</type>\n')
            linecontents.insert(file_end+4, linepre+'\t<objectName>'+object_name+'</objectName>\n')
            linecontents.insert(file_end+5, linepre+'\t<panDomain>'+pan_domain+'</panDomain>\n')
            linecontents.insert(file_end+6, linepre+'</EntityMap>\n')
        except ValueError as e:
            return False, e
        
        newfile = ''.join(linecontents)
        f = open(dir_path, "w", encoding="utf-8")
        try:
            f.write(newfile)
            
        except PermissionError as e:
            return False, e
        finally:
            f.close()
        
        del linecontents[:] 
        return True, None
    
    
#---------------- pom.xml --------------------------
    @staticmethod
    def verify_pom(dir_path):
        '''
        verify the pom.xml file
        @param dir_path: the directory of pom.xml by dom
        @return: return status
        @return: message if validation failed
        '''
        # verify if file is existing
        if not File_processor.verify_dir_existing(dir_path):
            return False, 'The pom.xml is not exist, please check.'
        
        try:
            dom = xml.dom.minidom.parse(dir_path)
            root = dom.documentElement
            if not root.nodeName == 'project':
                return False, 'This is not a valid pom.xml, please check.'
        except ExpatError:
            return False, 'This is not a valid xml file, please check.'
        
        return True, None
    
        
    @staticmethod
    def read_pom(dir_path):
        '''
        read the pom.xml file, and load the details into PomDTO
        @param dir_path: the directory of pom.xml (web) by dom
        @return: return status
        @return: PomDTO
        @return: message if validation failed
        '''
        # verify if file is existing
        if not File_processor.verify_dir_existing(dir_path):
            return False, None, 'The pom.xml is not exist, please check.'
        
        #get the root of entityMap.xml
        dom = xml.dom.minidom.parse(dir_path)
        pomDto = PomDTO()
        for node in dom.getElementsByTagName('properties'):
            node_value = node.getElementsByTagName('financials-api-version')[0]
            pomDto.set_financials_api_version(node_value.childNodes[0].nodeValue)
            break
        
        return True, pomDto, None
    
    
    