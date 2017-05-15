from __future__ import unicode_literals

from django.db import models

import re, bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
# Create your models here.

class UserManager(models.Manager):
    def register_user(self,postData):
        errors = []
        if len(postData['username']) < 2:
            errors.append('User name must be at least 2 characters long')

        if len(postData['password']) < 8:
            errors.append('Password must be at least 8 characters long')

        if not postData['password']  == postData['confirm_password']:
            errors.append("Confirm Password doesn't match Password")

        if self.filter(username = postData['username']):
            errors.append('This user name already belongs to a user')

        response_to_views = {}
        if not errors:
            hashed_password = bcrypt.hashpw(postData['password'].encode(), bcrypt.gensalt())
            user = self.create(username = postData['username'], password = hashed_password)
            response_to_views['user'] = user
            response_to_views['status'] = True
        else:
            response_to_views['errors'] = errors
            response_to_views['status'] = False

        return response_to_views

    def login_user(self,postData):
        user = self.filter(username = postData['username'])
        response_to_views = {}

        if not user:
            response_to_views['status'] = False
            response_to_views['errors'] = 'User name not found'
        else:
            if bcrypt.checkpw(postData['password'].encode(), user[0].password.encode()):
                response_to_views['status'] = True
                response_to_views['user'] = user.first()
            else:
                response_to_views['status'] = False
                response_to_views['errors'] = 'Invalid Email/password combination'

        return response_to_views


class User(models.Model):
    username = models.CharField(max_length = 45)
    password = models.CharField(max_length = 255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()
