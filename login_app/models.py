from django.db import models

class Login_Model(models.Model):
    id=models.IntegerField(max_length=10,auto_created=True,primary_key=True)
    name=models.CharField(max_length=20)
    pwd=models.CharField(max_length=20)
    def __unicode__(self):
        return self.id,self.name,self.pwd