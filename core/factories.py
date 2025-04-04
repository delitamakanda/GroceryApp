class BaseFactory:
    model = None
    
    @classmethod
    def create(cls, **kwargs):
        return cls.model.objects.create(**kwargs)