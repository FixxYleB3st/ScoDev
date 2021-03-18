from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class a_description(models.Model):
    description = models.CharField(max_length=1000, unique=True)
    avaible = models.BooleanField(default=True)
    
    def __str__(self):
        return self.description 