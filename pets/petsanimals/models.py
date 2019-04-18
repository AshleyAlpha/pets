from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

class Pet(models.Model):
    image = models.ImageField(upload_to = 'viva/',null=True)
    pet_name = models.CharField(max_length=30)
    pet_sex = models.CharField(max_length=30)
    pet_age = models.CharField(max_length=30)
    pet_details = models.CharField(max_length=30,null=True)
    pet_price = models.CharField(max_length=30,null=True)

class Client(models.Model):
    First_name = models.CharField(max_length=30)
    Last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    pet= models.ForeignKey(Pet)

    def __str__(self):
        return self.first_name

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def get_profile(cls):
        profiles = cls.objects.all()
        return profiles

    @classmethod
    def search_by_username(cls,search_term):
        profiles = cls.objects.filter(first_name__icontains=search_term)
        return profiles

class NewsLetterRecipients(models.Model):
    name = models.CharField(max_length = 30)
    email = models.EmailField()



