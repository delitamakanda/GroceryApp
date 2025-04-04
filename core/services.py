class BaseService:
    repository_class = None
    
    def __init__(self):
        self.repository = self.repository_class()
    
    def get_by_id(self, id):
        return self.repository.get_by_id(id)
    
    def create(self, **kwargs):
        return self.repository.create(**kwargs)
    
    def update(self, id, **kwargs):
        instance = self.repository.get_by_id(id)
        if instance:
            return self.repository.update(instance, **kwargs)
        return None
    
    def delete(self, id):
        instance = self.repository.get_by_id(id)
        if instance:
            self.repository.delete(instance)
            return True
        return False