class FilterModule:
    
    def filters(self):
        return {
            'helloworld': self.helloWorld
        }
        
    def helloWorld(self, hostname):
        return f"Hello from host { hostname }"

# if you move this file up to the ansible/filter_plugins-Directory, the global Filter 
# will be used and all definitions with this name in individual roles will be overwritten!
