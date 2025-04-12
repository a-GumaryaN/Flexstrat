from ..constant import *

class IOC_manager :

    registered_dependency={
        API:{},
        VISUALIZER:{},
        INDICATORS:{},
        CORE:{},
    }

    def register(self,section,dependency_name,dependency_class):
        if section not in self.registered_dependency:
            self.registered_dependency[section]={}
        self.registered_dependency[section][dependency_name]=dependency_class

    def contain(self,section,dependency_name):
        if section not in self.registered_dependency:
            raise Exception("SECTION ",section," NOT EXIST IN DEPENDENCIES")
        if dependency_name not in self.registered_dependency[section]:
            error = "DEPENDENCY '" + dependency_name + "' NOT EXIST IN SECTION '" + section + "'"
            raise Exception(error)
        return self.registered_dependency[section][dependency_name]()
