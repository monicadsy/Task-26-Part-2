from django.db import models

"""
Model representing a bulletin board post.

Fields:
- name: CharField for the post title with a maximum length of 40 characters,
- sets: Small Integer Field for the post
- description: TextField for the post content
- creator: CharField representing the creator of the post.

Methods:
- No specific methods are defined in this model.
:param models.Model: Django's base model class.
"""


class Stickynote(models.Model):
    name = models.CharField(max_length=40)
    sets = models.SmallIntegerField(default=0, null=True, blank=True)
    description = models.TextField()
    creator = models.CharField(max_length=30)
