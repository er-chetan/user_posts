from django.db import models

class AddPost(models.Model):
    title=models.CharField(max_length=200)
    category=models.CharField(max_length=200)
    description=models.CharField(max_length=1000)


class Category(models.Model):
    addcategory=models.CharField(max_length=200)    
    description=models.CharField(max_length=200)    