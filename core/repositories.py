from django.db.models import QuerySet

class BaseRepository:
    model = None
    
    def get_queryset(self) -> QuerySet:
        return self.model.objects.all()
    
    def get_by_id(self, id) -> object:
        return self.model.objects.filter(id=id).first()
    
    def create(self, **kwargs) -> object:
        return self.model.objects.create(**kwargs)
    
    def update(self, instance, **kwargs) -> object:
        for key, value in kwargs.items():
            setattr(instance, key, value)
        instance.save()
        return instance
    
    def delete(self, instance) -> None:
        instance.delete()