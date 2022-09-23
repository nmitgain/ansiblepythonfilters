class FilterModule:
    
    def filters(self):
        return {
            'helloworld': self.helloWorld,
            'list2inclause': self.list2inclause
        }
        
    def helloWorld(self, hostname):
        return f"Hello from Role { hostname }"

    def list2inclause(self, yamllist):
        # putting in the "()" as well for good measure
        return "(" + ",".join(["'" + x + "'" for x in yamllist ]) + ")"
