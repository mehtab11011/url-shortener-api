from django.db import models
import random,string

def generate_short_code():
    return "".join(random.choices(string.ascii_letters + string.digits , k=6))

class ShortendURLModel(models.Model):
    Original_URL=models.URLField(max_length=800)
    Short_URL=models.CharField(max_length=9,unique=True,default=generate_short_code)
    Access_Count=models.IntegerField(default=0)
    Created_At=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.Orignal_URL

# Create your models here.
 