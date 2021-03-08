from django.db import models

# Create your models here.

class contact(models.Model):
    fname = models.CharField( max_length=50)
    email = models.CharField( max_length=50)
    phone = models.CharField( max_length=50)

    def __str__(self):
        return self.fname

class places(models.Model):
    photo = models.ImageField( upload_to='pics')
    desc = models.CharField( max_length=50)
    discription = models.TextField(("Description"))

    def __str__(self):
        return self.desc
