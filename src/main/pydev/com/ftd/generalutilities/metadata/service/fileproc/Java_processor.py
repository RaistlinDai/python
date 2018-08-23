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
    def read_java_file(srcfile):
        '''
        read and analysis the java file, output the information in JavaDTO
        NOTE: this is a light weight reador for java file. Generally we should use java reflection
        @param srcfile: the java file
        '''
        if not File_processor.verify_dir_existing(srcfile):
            return False, "File not exist!", None
        
        javaconstant = Java_constant()
        javaDTO = JavaDTO()
        
        # marks
        class_type = None
        class_line_nbr = 0
        class_start_mark = False
        class_block_startln = -1
        class_end_mark = False
        method_start_mark = False
        method_end_mark = False
        method_block_startln = -1
        method_block_count = 0
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
            cells = eachline.split(' ')
            
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
                class_start_mark = True
                class_type = javaconstant.JAVA_KEY_CLASS
                
                value = cells[cells.index(javaconstant.JAVA_KEY_CLASS)+1]
                if javaconstant.JAVA_LEFT_BRACE in value:
                    subcells = value.split(javaconstant.JAVA_LEFT_BRACE)
                    javaDTO.set_class_name(subcells[0])
                    
                    # class start line
                    class_block_startln = class_line_nbr
                else:
                    javaDTO.set_class_name(value)
                
                javaDTO.set_class_type(javaconstant.JAVA_KEY_CLASS)
            
            # interface name
            if javaconstant.JAVA_KEY_INTERFACE in cells:
                #marks
                class_start_mark = True
                class_type = javaconstant.JAVA_KEY_INTERFACE
                
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
                if not method_start_mark and not method_end_mark:
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
                                
                                return_type = subcells[-1]
                                new_method.set_method_output(return_type)
                                
                            # -- parameters
                            if method_param_startIdx > 0 and method_param_endIdx > 0:
                                method_param_block = eachline[method_param_startIdx+1:method_param_endIdx]
                                subcells = method_param_block.split(javaconstant.JAVA_SEPERATOR)
                                
                                for subparam in subcells:
                                    internalcells = subparam.lstrip().split(' ')
                                    if len(internalcells) > 0:
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
    def create_service_impl(filefullpath, filename, entityDTO):
        '''
        create the serviceImpl file
        @param filefullpath: the serviceImpl file full path
        '''
        javaconstant = Java_constant()
        fileconstant = File_constant()
        
        # get the package name
        pack_name = Java_processor.analysis_package_name(entityDTO.get_serviceInterDTO().get_class_package())
        # get the serviceImpl name
        service_name = filename.replace(fileconstant.JAVA_SUFFIX, '')
        # get the container interface name
        container_inter_name = entityDTO.get_entContInterDTO().get_class_name()
        # get the factory interface name
        factory_inter_name = entityDTO.get_factoryInterDTO().get_class_name()
        
        # retrieve the imports in api package
        imports = entityDTO.get_serviceInterDTO().get_class_imports()        
        
        Path(filefullpath).touch()
        file = open(filefullpath, 'w')
        
        # ----- write the class comments title -----
        file.write(javaconstant.JAVA_ENTITY_TITLE)
        file.write('\n')
        
        # ----- write the package -----
        file.write(javaconstant.JAVA_KEY_PACKAGE + ' ' + pack_name + javaconstant.JAVA_END_MARK + '\n')
        file.write('\n')
        
        # ----- write the imports -----
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
        
        file.write('\n')
        
        
        # ----- write the service annotation -----
        tempStr = pack_name + javaconstant.JAVA_DOT_MARK + service_name
        file.write(javaconstant.JAVA_SERVICE_ANNOTATION % tempStr + '\n')
        
        # ----- write the class header -----
        tempStr = javaconstant.JAVA_SERVICE_HEADER % (service_name, container_inter_name, factory_inter_name)
        file.write(tempStr + '\n')
        
        
        
        # ----- write the class ender -----
        file.write(javaconstant.JAVA_RIGHT_BRACE)
        file.close()
        
    
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