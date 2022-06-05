from distutils.command.upload import upload
from django.db import models
from datetime import datetime
from turtle import title
from django.forms import DateTimeField
from django.contrib.auth.models import User


# Create your models here.
class Topic(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=200)
    body=models.TextField(blank=True)
    date_created=models.DateTimeField(auto_now_add=True)
    image = models.ImageField( upload_to = 'blog_image',blank=True) 
    # body=models.TextField()

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-id']

class content_post(models.Model):
    title=models.CharField(max_length=200)
    body=models.TextField(blank=True)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
    class Meta:
        ordering = ['-id']
        
        
class Comment(models.Model):
    post = models.ForeignKey(Topic,on_delete=models.CASCADE)
    body=models.TextField(blank=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.body[:50]}...'



# class Header(models.Model):
#     header=models.CharField(max_length=200)
#     date_created=models.DateTimeField(auto_now_add=True)

#     def __str__(self):
#         return self.header
