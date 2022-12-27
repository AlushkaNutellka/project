from django.db import models

# class Person(models.Model):
#     first_name = models.CharField(max_length=30)
#     last_name = models.CharField(max_length=30)
#     slug = models.SlugField()  # == text in postgres

# CREATE TABLE app_name_person(id primary key,
# first_name varchar(30),
# last_name varchar(30),)

class Category(models.Model):
    title = models.CharField(max_length=40,unique=True)

class Post(models.Model):
    title = models.CharField(max_length=80)
    text = models.TextField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    reated_at = models.DateTimeField(
        auto_now_add=True)
    