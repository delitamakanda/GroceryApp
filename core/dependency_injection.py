class DependencyInjector:
    _instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.dependencies = {}
        return cls._instance
    
    def register(self, key, dependency):
        self.dependencies[key] = dependency
        
    def resolve(self, key):
        if key not in self.dependencies:
            raise KeyError(f"Dependency '{key}' not found")
        return self.dependencies[key]
    
injector = DependencyInjector()
