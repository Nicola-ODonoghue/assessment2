from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
    name = models.CharField(max_length=30, unique=True)#Enforce uniqueness of the field at the database level
    description = models.CharField(max_length=100)

    def __str__(self):
    	return self.name


class Topic(models.Model):
    subject = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='topics')#ForeignKey tells Django that a 'topic' instance relates to only one 'Board' instance
    starter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topics')#related_name creates a reverse relationship where the 'board' instances will have access a list of 'Topic' instances that belong to it


class Post(models.Model):
    message = models.TextField(max_length=4000)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name='posts')
    created_at = models.DateTimeField(auto_now_add=True)#INstructs Django to set the current date adn time when a 'Post' object is created 
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='+')#Instructs Django that we dont need this reverse relationship