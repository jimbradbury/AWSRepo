from __future__ import unicode_literals

from django.db import models

class UserManager(models.Manager):
    def add_user(self, postData):
        print postData
        print postData['first_name']
        # add postData data validations
        # author = Author.objects.get(id=postData['author_id'])
        # self.create(title = postData['title'], author = author)
    def test_function(self, testvar):
        print testvar

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()
