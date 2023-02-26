from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    phone = models.CharField(max_length=10)
    desc = models.TextField()

    def __str__(self):            #added so that we can see different entries in our db tables by names instead of "Contact(1) , Contact(2) etc"
        return self.name + " - " + self.email