from django.db import models
from django.utils import timezone
import datetime

# Create your models here.
# import the standard Django Model
# from built-in library
from django.db import models 
# declare a new model with a name "GeeksModel"
class Entry(models.Model):
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.description[:50]  # Return the first 50 characters of the description
    
    def was_published_recently(self):
        return self.created_at >= timezone.now() - datetime.timedelta(days=1)