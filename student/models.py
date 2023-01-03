from django.db import models

class studentclass(models.Model):
      name=models.CharField( max_length=50)
      grade=models.CharField(max_length=1)
      
def __str__(self) :
            return self.name
