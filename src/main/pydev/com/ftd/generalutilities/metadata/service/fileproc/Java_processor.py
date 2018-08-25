'''
Created on Jul 11, 2018

@author: ftd
'''
import jpype
import os
import zipfile
from jpype._jexception import JavaException
from src.main.pydev.com.ftd.generalutilities.metadata.service.base.File_constant import File_constant
from src.main.pydev.com.ftd.generalutilities.metadata.service.base.File_processor import File_processor
from src.main.pydev.com.ftd.generalutilities.metadata.service.base.Java_constant import Java_constant
from src.main.pydev.com.ftd.generalutilities.metadata.dto.javaFile.JavaDTO import JavaDTO,\
    JavaMethodDTO, JavaParameterDTO
from pathlib import Path

class Java_processor(File_processor):
    '''
    This class is used to process the Java and Jar files
    Note: before compiling this class, you have to install jpype and numpy in Python
    '''
    
    @staticmethod
    def verify_jar_type(dir_path):
        '''
        verify the jar file type
        @param dir_path: file directory
        @return: return status
        @return: message if validation failed
        '''
        if not File_processor.verify_file(dir_path):
            return False, "The jar file is not exist, please check."
        
        ftype = Java_processor.get_file_type(dir_path)
                
        if ftype == 'unknown':
            return False, 'The file type is unknown!'
        
        if ftype != 'jar':
            return False, 'The file type(%s) is not (jar) !' % ftype
        
        return True, None
        

    @staticmethod
    def java__tester():
        '''
        tester function for reading java
        '''
        jvmPath = jpype.getDefaultJVMPath() 
        jpype.startJVM(jvmPath) 
        jpype.java.lang.System.out.println('hello world!')
        jpype.shutdownJVM()
        
    
    @staticmethod
    def java_decomp_ftdJD(srcfile, dcpfile):
        '''
        decompile the jar to the target directory
        @param srcfile: the jar file
        @param dcpfile: the decompiled directory
        @return: return status
        @return: message if validation failed
        '''
        if not File_processor.verify_dir_existing(srcfile):
            return False, "File not exist!"
        
        fileconstant = File_constant()
        #--- get the 3rd lib jar path
        root_path = os.path.dirname(os.path.abspath(__file__))
        proj_path = root_path[:root_path.index(fileconstant.MY_PROJECT_PACKAGE)]
        #--- java class path
        jarpath = proj_path + fileconstant.FTD_JD_JAR + ';' + proj_path + fileconstant.THIRD_JDCORE_JAR
        
        #--- start JVM and point out the jar path
        if not jpype.isJVMStarted():  
            jpype.startJVM(jpype.getDefaultJVMPath(), "-Djava.class.path=%s" % jarpath)
            
        try:
            #--- import the jar class
            javaclass = jpype.JClass('main.java.com.jd.FtdDecompiler')
            #--- run java method
            javaclass.jarDecompiler(srcfile, dcpfile)
            
            return True, None
        except JavaException as ex: 
            print("Caught exception : ", ex.message())
            return False, ex.message()
        finally:
            #--- close JVM
            jpype.shutdownJVM()
            
    
    @staticmethod
    def unzip_jar(srcfile, outdir, deep_unzip=False):
        '''
        unzip the jar to the target directory
        @param srcfile: the jar file
        @param outdir: the output directory
        @param deep_unzip: if unzip the inner jar also
        @return: return status
        @return: message if validation failed
        '''
        if not File_processor.verify_dir_existing(srcfile):
            return False, "File not exist!"
        
        if not File_processor.verify_dir_existing(outdir):
            os.makedirs(outdir)
        
        fileconstant = File_constant()
        
        if fileconstant.JAR_SUFFIX in srcfile:
            zfile = zipfile.ZipFile(srcfile, 'r')  
            zfile.extractall(outdir)  
            zfile.close
        else:
            return False, "The source file is not jar!"
        
        #--- unzip all inner jars
        if deep_unzip:
            for fullname in File_processor.dir_iterbrowse(outdir):
                #get the inner jar files
                if (fileconstant.JAR_SUFFIX in fullname):
                    inner_jar_outdir = fullname[:fullname.index(fileconstant.JAR_SUFFIX)]
                    result, message = Java_processor.unzip_jar(fullname, inner_jar_outdir, deep_unzip)
                    if not result:
                        return False, "Deep unzip failed!"

        return True, None
    
    
    @staticmethod
    def read_java_interface(srcfile):
        '''
        read and analysis the java interface, output the information in JavaDTO
        NOTE: this is a light weight reader for java file. Generally we should use java reflection
        @param srcfile: the java file
        '''
        if not File_processor.verify_dir_existing(srcfile):
            return False, "File not exist!", None
        
        javaconstant = Java_constant()
        javaDTO = JavaDTO()
        
        # marks
        class_line_nbr = 0
        class_start_mark = False
        class_block_startln = -1
        class_end_mark = False
        method_param_startIdx = -1
        method_param_endIdx = -1
        
        file = open(srcfile, 'r')
        # read java file line by line
        for eachline in file.readlines():
            # line count
            class_line_nbr = class_line_nbr + 1
            
            # trim the line
            eachline = eachline.replace('\n', '')
            
            # split the line by blank
            cells = eachline.lstrip().split(' ')
            
            # package
            if javaconstant.JAVA_KEY_PACKAGE in cells:
                javaDTO.set_class_package(cells[cells.index(javaconstant.JAVA_KEY_PACKAGE)+1])
                
            # imports
            if javaconstant.JAVA_KEY_IMPORT in cells:
                value = cells[cells.index(javaconstant.JAVA_KEY_IMPORT)+1].replace(javaconstant.JAVA_END_MARK, '')
                javaDTO.push_class_imports(value)
                
            # class name
            if javaconstant.JAVA_KEY_CLASS in cells:
                #marks
                pass
            
            # interface name
            if javaconstant.JAVA_KEY_INTERFACE in cells:
                #marks
                class_start_mark = True
                
                value = cells[cells.index(javaconstant.JAVA_KEY_INTERFACE)+1]
                if javaconstant.JAVA_LEFT_BRACE in value:
                    subcells = value.split(javaconstant.JAVA_LEFT_BRACE)
                    javaDTO.set_class_name(subcells[0])
                    
                    # class start line
                    class_block_startln = class_line_nbr
                else:
                    javaDTO.set_class_name(value)
                    
                javaDTO.set_class_type(javaconstant.JAVA_KEY_INTERFACE)
            
            # extends
            if javaconstant.JAVA_KEY_EXTENDS in cells:
                value = cells[cells.index(javaconstant.JAVA_KEY_EXTENDS)+1]
                javaDTO.set_class_extends(value)
                
            # implements
            if javaconstant.JAVA_KEY_IMPLEMENTS in cells:
                value = cells[cells.index(javaconstant.JAVA_KEY_IMPLEMENTS)+1]
                
                if (javaconstant.JAVA_SEPERATOR in value):
                    # TODO: multiple interfaces
                    if (value.index(javaconstant.JAVA_SEPERATOR) == len(value) - 1):
                        javaDTO.push_class_implements(value[0:-1])
                    else:
                        subvalue = value.split(javaconstant.JAVA_SEPERATOR)
                        for imps in subvalue:
                            javaDTO.push_class_implements(imps)
                else:
                    javaDTO.push_class_implements(value)
            
            # class start line
            if class_start_mark and class_block_startln == -1 and javaconstant.JAVA_LEFT_BRACE in cells:
                # class start line
                class_block_startln = class_line_nbr
                
            # --------- methods & properties ------------
            # class inside
            if class_start_mark and class_block_startln > 0 and not class_end_mark:
                # find the method start point
                if javaconstant.JAVA_KEY_PUBLIC in cells or javaconstant.JAVA_KEY_PROTECTED in cells or javaconstant.JAVA_KEY_PRIVATE in cells:
                    # distingush method and property
                    
                    # constructor
                    if javaDTO.get_class_name() in cells:
                        continue;
                    
                    # method
                    if javaconstant.JAVA_LEFT_BRACKET in eachline:
                        
                        # method mark
                        method_param_startIdx = eachline.index(javaconstant.JAVA_LEFT_BRACKET)
                        new_method = JavaMethodDTO()
                        
                        # TODO: currently only parameters in one line could be processed
                        if javaconstant.JAVA_RIGHT_BRACKET in eachline:
                            # method mark
                            method_param_endIdx = eachline.index(javaconstant.JAVA_RIGHT_BRACKET)
                        
                        # --- method name & return
                        if method_param_startIdx > 0:
                            method_name_header = eachline[0:method_param_startIdx].strip(' ')
                            subcells = method_name_header.split(' ')
                            
                            method_name = subcells[-1]
                            new_method.set_method_name(method_name)
                            
                            return_type = subcells[-2]
                            new_method.set_method_output(return_type)
                        
                        # -- parameters
                        if method_param_startIdx > 0 and method_param_endIdx > 0:
                            method_param_block = eachline[method_param_startIdx+1:method_param_endIdx]
                            subcells = method_param_block.split(javaconstant.JAVA_SEPERATOR)
                            
                            for subparam in subcells:
                                internalcells = subparam.lstrip().split(' ')
                                if len(internalcells) <= 1:
                                    continue
                                params = JavaParameterDTO()
                                params.set_parameter_name(internalcells[1])
                                params.set_parameter_type(internalcells[0])
                                
                                new_method.push_method_inputs(params)
                        
                        # add method into DTO
                        javaDTO.push_class_methods(new_method)
                            
        file.close()
        return True, None, javaDTO
     
     
    @staticmethod
    def read_java_class(srcfile, interDTO): 
        '''
        read and analysis the java class, get the functions' parameters and set them in JavaDTO
        NOTE: this is a light weight reader for java file. Generally we should use java reflection
              it only process the functions' parameters
        @param srcfile: the java file
        @param javaDTO: the java DTO generated from interface reader
        '''
        if not File_processor.verify_dir_existing(srcfile):
            return False, "File not exist!", None
        
        javaconstant = Java_constant()
        javaDTO = JavaDTO()
        
        class_line_nbr = 0
        
        file = open(srcfile, 'r')
        # read java file line by line
        for eachline in file.readlines():
            # line count
            class_line_nbr = class_line_nbr + 1
            
            # trim the line
            eachline = eachline.replace('\n', '')
            
            # trim the line
            if javaconstant.JAVA_LEFT_COMMENT in eachline and javaconstant.JAVA_RIGHT_COMMENT in eachline:
                right_idx = eachline.index(javaconstant.JAVA_RIGHT_COMMENT) + 2
                eachline = eachline[right_idx:].lstrip()
            eachline = eachline.replace('\n', '')
            
            # split the line by blank
            cells = eachline.lstrip().split(' ')
            
            # package
            if javaconstant.JAVA_KEY_PACKAGE in cells:
                javaDTO.set_class_package(cells[cells.index(javaconstant.JAVA_KEY_PACKAGE)+1])
                
            # imports
            if javaconstant.JAVA_KEY_IMPORT in cells:
                value = cells[cells.index(javaconstant.JAVA_KEY_IMPORT)+1].replace(javaconstant.JAVA_END_MARK, '')
                javaDTO.push_class_imports(value)
                
            # class name
            if javaconstant.JAVA_KEY_CLASS in cells:
                #marks
                value = cells[cells.index(javaconstant.JAVA_KEY_CLASS)+1]
                if javaconstant.JAVA_LEFT_BRACE in value:
                    subcells = value.split(javaconstant.JAVA_LEFT_BRACE)
                    javaDTO.set_class_name(subcells[0])
                else:
                    javaDTO.set_class_name(value)
                    
                javaDTO.set_class_type(javaconstant.JAVA_KEY_CLASS)
            
            # method info
            if javaconstant.JAVA_KEY_CLASS not in cells:
                # public method
                methodDTO = JavaMethodDTO()
                if javaconstant.JAVA_KEY_PUBLIC in cells:
                    # all parameters are in a single line
                    if javaconstant.JAVA_LEFT_BRACKET in eachline and javaconstant.JAVA_RIGHT_BRACKET in eachline:
                        mtd_headers_and_param = eachline.split(javaconstant.JAVA_LEFT_BRACKET)
                        mtd_headers = mtd_headers_and_param[0].split(' ')
                        # method name
                        methodDTO.set_method_name(mtd_headers[-1])
                        # method return
                        methodDTO.set_method_output(mtd_headers[-2])
                        # method range
                        methodDTO.set_method_output(javaconstant.JAVA_KEY_PUBLIC)
                        
                        # method inputs
                        method_param = mtd_headers_and_param[1]
                        method_param = method_param[:method_param.index(javaconstant.JAVA_RIGHT_BRACKET)]
                        if method_param == '':
                            methodDTO.set_method_inputs(None)
                        else:
                            params = method_param.split(javaconstant.JAVA_SEPERATOR)
                            paramDTO = JavaParameterDTO()
                            for param in params:
                                paramcells = param.lstrip().split(' ')
                                paramDTO.set_parameter_name(paramcells[-1])
                                paramDTO.set_parameter_type(paramcells[-2])
                            
                                # verify the imports for parameter
                                for imp in javaDTO.get_class_imports():
                                    impcells = imp.split(javaconstant.JAVA_DOT_MARK)
                                    if impcells[-1] == paramDTO.get_parameter_type():
                                        methodDTO.push_method_related_imports(imp)
                                    
                                # add input parameter
                                methodDTO.push_method_inputs(paramDTO)
                    
                javaDTO.push_class_methods(methodDTO)   
            
        return True, None, javaDTO     
        
        
    @staticmethod
    def create_service_impl(filefullpath, filename, entityDTO):
        '''
        create the serviceImpl file
        @param filefullpath: the serviceImpl file full path
        '''
        javaconstant = Java_constant()
        fileconstant = File_constant()
        
        factory_mtd_list = entityDTO.get_factoryInterDTO().get_class_methods()
        service_mtd_list = entityDTO.get_serviceInterDTO().get_class_methods()
        container_mtd_list = entityDTO.get_entContInterDTO().get_class_methods()
        maintable_mtd_list = entityDTO.get_maintableInterDTO().get_class_methods()
        # ------------------------------------------------------- #
        #                       Preparation                       #
        # ------------------------------------------------------- #
        # get the package name
        pack_name = Java_processor.analysis_package_name(entityDTO.get_serviceInterDTO().get_class_package())
        # get the serviceImpl name
        serviceimpl_name = filename.replace(fileconstant.JAVA_SUFFIX, '')
        # get the container interface name
        container_inter_name = entityDTO.get_entContInterDTO().get_class_name()
        # get the service interface name
        service_inter_name = entityDTO.get_serviceInterDTO().get_class_name()
        # get the factory interface name
        factory_inter_name = entityDTO.get_factoryInterDTO().get_class_name()
        # get the container qra name
        container_qra_name = entityDTO.get_entContQraDTO().get_class_name()
        # get the service qra name
        service_qra_name = entityDTO.get_serviceQraDTO().get_class_name()
        # get the factory interface name
        factory_qra_name = entityDTO.get_factoryQraDTO().get_class_name()
        # get the main table interface name
        main_table_inter_name = entityDTO.get_maintableInterDTO().get_class_name()
        # entity holder
        entity_holder = container_inter_name.replace(fileconstant.JAVA_CONTAINER_SUFFIX, '') + fileconstant.JAVA_HOLDER_SUFFIX
        # retrieve the imports in api package
        imports = entityDTO.get_serviceInterDTO().get_class_imports()
        # additional imports for method parameters/result
        additional_imports = []
                        
        # createEntityContainer()
        mtd_create_entity_container = javaconstant.JAVA_FUNCTION_CREATE + container_inter_name
        valid_flag = False
        for mtd in factory_mtd_list:
            if mtd_create_entity_container == mtd.get_method_name() and container_inter_name == mtd.get_method_output():
                valid_flag = True
        if not valid_flag:
            return False
        
        # getEntityService()
        mtd_get_entity_service = javaconstant.JAVA_FUNCTION_GET + service_inter_name
        valid_flag = False
        for mtd in factory_mtd_list:
            if mtd_get_entity_service == mtd.get_method_name() and service_inter_name == mtd.get_method_output():
                valid_flag = True
        if not valid_flag:
            return False
        
        # initializeEntityDataset()
        entity_dataset_name = entityDTO.get_resourceDTO().get_view_parameters().get_table()
        mtd_initialize_entityDS = javaconstant.JAVA_FUNCTION_INITIALIZE + entity_dataset_name
        valid_flag = False
        for mtd in service_mtd_list:
            if mtd_initialize_entityDS == mtd.get_method_name():
                valid_flag = True
        if not valid_flag:
            return False
        
        # getMainTables()
        mtd_get_maintables = javaconstant.JAVA_FUNCTION_GET + main_table_inter_name + 's'
        valid_flag = False
        for mtd in container_mtd_list:
            if mtd_get_maintables == mtd.get_method_name() and main_table_inter_name in mtd.get_method_output():
                valid_flag = True
        if not valid_flag:
            return False
        
        # fetch parameters
        mtd_fetch_param_values = ''      # e.g. entity.getParam1(), entity.getParam2(), entity.getParam3()
        mtd_fetch_param_inputs = ''      # e.g. String param1, Integer param2, Integer param3
        mtd_fetch_param_calls = ''       # e.g. param1, param2, param3
        for mtd in service_mtd_list:
            # fetch method in qra service
            if javaconstant.JAVA_FUNCTION_FETCH == mtd.get_method_name():
                
                param_nbr = 0
                for param in mtd.get_method_inputs():
                    param_nbr = param_nbr + 1
                    
                    for tabMtd in maintable_mtd_list:
                        print(tabMtd.get_method_name())
                        if tabMtd == javaconstant.JAVA_FUNCTION_GET + param.get_parameter_name()[0:1].upper() + param.get_parameter_name()[1:]:
                            pass
                            
                    
                    if param_nbr == len(mtd.get_method_inputs()):
                        mtd_fetch_param_inputs = mtd_fetch_param_inputs + param.get_parameter_type() + ' ' + param.get_parameter_name()
                        mtd_fetch_param_calls = mtd_fetch_param_calls + param.get_parameter_name()
                    else:
                        mtd_fetch_param_inputs = mtd_fetch_param_inputs + param.get_parameter_type() + ' ' + param.get_parameter_name() + javaconstant.JAVA_SEPERATOR + ' '
                        mtd_fetch_param_calls = mtd_fetch_param_calls + param.get_parameter_name() + javaconstant.JAVA_SEPERATOR + ' '
                        if param_nbr % 5 == 0:
                            mtd_fetch_param_inputs = mtd_fetch_param_inputs + '\n'
                            mtd_fetch_param_calls = mtd_fetch_param_calls + '\n'
                            
                break
            
        # create file
        Path(filefullpath).touch()
        file = open(filefullpath, 'w')
        
        # ------------------------------------------------------- #
        # ----- write the class comments title -----
        # ------------------------------------------------------- #
        file.write(javaconstant.JAVA_ENTITY_TITLE)
        file.write('\n')
        
        # ------------------------------------------------------- #
        # ----- write the package -----
        # ------------------------------------------------------- #
        file.write(javaconstant.JAVA_KEY_PACKAGE + ' ' + pack_name + javaconstant.JAVA_END_MARK + '\n')
        file.write('\n')
        
        # ------------------------------------------------------- #
        # ----- write the imports -----
        # ------------------------------------------------------- #
        import_list = []
        for importcell in imports:
            file.write(javaconstant.JAVA_KEY_IMPORT + ' ' + importcell + javaconstant.JAVA_END_MARK + '\n')
            import_list.append(javaconstant.JAVA_KEY_IMPORT + ' ' + importcell + javaconstant.JAVA_END_MARK)
        
        if javaconstant.JAVA_SERVICE_IMPORT_SPRING_FRAME not in import_list:
            file.write(javaconstant.JAVA_SERVICE_IMPORT_SPRING_FRAME + '\n')
            import_list.append(javaconstant.JAVA_SERVICE_IMPORT_SPRING_FRAME)
        if javaconstant.JAVA_SERVICE_IMPORT_PRO_DATAGRAPH not in import_list:
            file.write(javaconstant.JAVA_SERVICE_IMPORT_PRO_DATAGRAPH + '\n')
            import_list.append(javaconstant.JAVA_SERVICE_IMPORT_PRO_DATAGRAPH)
        if javaconstant.JAVA_SERVICE_IMPORT_FIN_QRA_ENTITYSERVICE not in import_list:
            file.write(javaconstant.JAVA_SERVICE_IMPORT_FIN_QRA_ENTITYSERVICE + '\n')
            import_list.append(javaconstant.JAVA_SERVICE_IMPORT_FIN_QRA_ENTITYSERVICE)
        if javaconstant.JAVA_SERVICE_IMPORT_API_EXCEPTION not in import_list:
            file.write(javaconstant.JAVA_SERVICE_IMPORT_API_EXCEPTION + '\n')
            import_list.append(javaconstant.JAVA_SERVICE_IMPORT_API_EXCEPTION)
        if javaconstant.JAVA_SERVICE_IMPORT_CONNECTION_MANAGER not in import_list:
            file.write(javaconstant.JAVA_SERVICE_IMPORT_CONNECTION_MANAGER + '\n')
            import_list.append(javaconstant.JAVA_SERVICE_IMPORT_CONNECTION_MANAGER)
        if javaconstant.JAVA_SERVICE_IMPORT_CONTEXT not in import_list:
            file.write(javaconstant.JAVA_SERVICE_IMPORT_CONTEXT + '\n')
            import_list.append(javaconstant.JAVA_SERVICE_IMPORT_CONTEXT)
        if javaconstant.JAVA_SERVICE_IMPORT_HOLDER not in import_list:
            file.write(javaconstant.JAVA_SERVICE_IMPORT_HOLDER + '\n')
            import_list.append(javaconstant.JAVA_SERVICE_IMPORT_HOLDER)
        if javaconstant.JAVA_SERVICE_IMPORT_EXCEPTION_UTIL not in import_list:
            file.write(javaconstant.JAVA_SERVICE_IMPORT_EXCEPTION_UTIL + '\n')
            import_list.append(javaconstant.JAVA_SERVICE_IMPORT_EXCEPTION_UTIL)
        if javaconstant.JAVA_SERVICE_IMPORT_QRA_WORKSPACE_UTIL not in import_list:
            file.write(javaconstant.JAVA_SERVICE_IMPORT_QRA_WORKSPACE_UTIL + '\n')
            import_list.append(javaconstant.JAVA_SERVICE_IMPORT_QRA_WORKSPACE_UTIL)
        if javaconstant.JAVA_SERVICE_IMPORT_SUBMIT_RESULTANDDATA not in import_list:
            file.write(javaconstant.JAVA_SERVICE_IMPORT_SUBMIT_RESULTANDDATA + '\n')
            import_list.append(javaconstant.JAVA_SERVICE_IMPORT_SUBMIT_RESULTANDDATA)
        if javaconstant.JAVA_SERVICE_IMPORT_API_DATAGRAPH not in import_list:
            file.write(javaconstant.JAVA_SERVICE_IMPORT_API_DATAGRAPH + '\n')
            import_list.append(javaconstant.JAVA_SERVICE_IMPORT_API_DATAGRAPH)
        
        container_inter_package = javaconstant.JAVA_KEY_IMPORT + ' ' + entityDTO.get_entContInterDTO().get_class_package()[:-1] + javaconstant.JAVA_DOT_MARK + container_inter_name + javaconstant.JAVA_END_MARK
        if container_inter_package not in import_list:
            file.write(container_inter_package + '\n')   # import container interface
            import_list.append(container_inter_package)
        
        factory_inter_package = javaconstant.JAVA_KEY_IMPORT + ' ' + entityDTO.get_factoryInterDTO().get_class_package()[:-1] + javaconstant.JAVA_DOT_MARK + factory_inter_name + javaconstant.JAVA_END_MARK
        if factory_inter_package not in import_list:
            file.write(factory_inter_package + '\n')   # import factory interface
            import_list.append(factory_inter_package)
            
        container_qra_package = javaconstant.JAVA_KEY_IMPORT + ' ' + entityDTO.get_entContQraDTO().get_class_package()[:-1] + javaconstant.JAVA_DOT_MARK + container_qra_name + javaconstant.JAVA_END_MARK
        if container_qra_package not in import_list:
            file.write(container_qra_package + '\n')   # import container qra
            import_list.append(container_qra_package)
            
        factory_qra_package = javaconstant.JAVA_KEY_IMPORT + ' ' + entityDTO.get_factoryQraDTO().get_class_package()[:-1] + javaconstant.JAVA_DOT_MARK + factory_qra_name + javaconstant.JAVA_END_MARK
        if factory_qra_package not in import_list:
            file.write(factory_qra_package + '\n')   # import factory qra
            import_list.append(factory_qra_package)
        file.write('\n')
        
        # ------------------------------------------------------- #
        # ----- write the service annotation -----
        # ------------------------------------------------------- #
        tempStr = pack_name + javaconstant.JAVA_DOT_MARK + serviceimpl_name
        file.write(javaconstant.JAVA_ANNOTATION_SERVICE % tempStr + '\n')
        
        # ------------------------------------------------------- #
        # ----- write the class header -----
        # ------------------------------------------------------- #
        tempStr = javaconstant.JAVA_SERVICE_HEADER % (serviceimpl_name, container_inter_name, factory_inter_name)
        file.write(tempStr + '\n')
        file.write('\n')
        
        # ------------------------------------------------------- #
        # ----- write the override methods -----
        # ------------------------------------------------------- #
        for mtds in javaconstant.JAVA_SERVICEIMPL_OVERRIDE_METHODS:
            for lines in mtds:
                lines = javaconstant.JAVA_TAB + lines
                # replace container interface
                if javaconstant.JAVA_ENTITYCONST_CONTAINER_INTER in lines:
                    lines = lines.replace(javaconstant.JAVA_ENTITYCONST_CONTAINER_INTER, container_inter_name)
                # replace factory interface
                if javaconstant.JAVA_ENTITYCONST_FACTORY_INTER in lines:
                    lines = lines.replace(javaconstant.JAVA_ENTITYCONST_FACTORY_INTER, factory_inter_name)
                # replace container qra
                if javaconstant.JAVA_ENTITYCONST_CONTAINER_QRA in lines:
                    lines = lines.replace(javaconstant.JAVA_ENTITYCONST_CONTAINER_QRA, container_qra_name)
                # replace factory qra
                if javaconstant.JAVA_ENTITYCONST_FACTORY_QRA in lines:
                    lines = lines.replace(javaconstant.JAVA_ENTITYCONST_FACTORY_QRA, factory_qra_name)
                # replace entity holder
                if javaconstant.JAVA_ENTITYCONST_HOLDER in lines:
                    lines = lines.replace(javaconstant.JAVA_ENTITYCONST_HOLDER, entity_holder)
                # replace create container method
                if javaconstant.JAVA_ENTITYCONST_CRAET_CONTAINER_INTER in lines:
                    lines = lines.replace(javaconstant.JAVA_ENTITYCONST_CRAET_CONTAINER_INTER, mtd_create_entity_container)
                # replace get service method
                if javaconstant.JAVA_ENTITYCONST_GET_SERVICE_INTER in lines:
                    lines = lines.replace(javaconstant.JAVA_ENTITYCONST_GET_SERVICE_INTER, mtd_get_entity_service)
                # replace initialize entityDataset method
                if javaconstant.JAVA_ENTITYCONST_INITIAL_ENTITY_DATASET in lines:
                    lines = lines.replace(javaconstant.JAVA_ENTITYCONST_INITIAL_ENTITY_DATASET, mtd_initialize_entityDS)
                # replace main table interface
                if javaconstant.JAVA_ENTITYCONST_ENTITY_DATASET in lines:
                    lines = lines.replace(javaconstant.JAVA_ENTITYCONST_ENTITY_DATASET, main_table_inter_name)
                # replace get main table list method
                if javaconstant.JAVA_ENTITYCONST_GET_ENTITY_DATASET_LIST in lines:
                    lines = lines.replace(javaconstant.JAVA_ENTITYCONST_GET_ENTITY_DATASET_LIST, mtd_get_maintables)
                # replace fetch input parameters
                if javaconstant.JAVA_ENTITYCONST_FETCH_METHOD_PARAMS in lines:
                    lines = lines.replace(javaconstant.JAVA_ENTITYCONST_FETCH_METHOD_PARAMS, '%%%%%')
                
                
                
                if '\n' not in lines:
                    file.write(lines + '\n')
                else:
                    file.write(lines)
            
            file.write('\n')
        
        
        
        # ------------------------------------------------------- #
        # ----- write the class ender -----
        # ------------------------------------------------------- #
        file.write('\n' + javaconstant.JAVA_RIGHT_BRACE)
        file.close()
        
        return True
    
    
    @staticmethod
    def analysis_package_name(package_name):
        '''
        analysis the package name
        @return: serviceImpl_folder
        '''
        javaconstant = Java_constant()
        package_parent_name = None    # package parent name
        package_sub_name = None       # package self name
        if javaconstant.JAVA_IMPL_PACKAGE_PREFIX in package_name:
            temp_str = package_name[len(javaconstant.JAVA_IMPL_PACKAGE_PREFIX):]
            package_parent_name = temp_str[:temp_str.index('.')]
            package_sub_name = temp_str[temp_str.index('.')+1:].replace(javaconstant.JAVA_END_MARK,'')
        
        serviceImpl_folder = javaconstant.JAVA_ENTITY_SERVICEIMPL_PACKAGE % package_parent_name
        
        return serviceImpl_folder