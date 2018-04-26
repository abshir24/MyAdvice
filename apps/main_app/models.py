from __future__ import unicode_literals

from django.db import models
from ..logreg.models import User
# Create your models here.

class AnswersManager(models.Manager):
    def answerAdd(self,answerlist,user_id):
        creator = User.objects.get(id = user_id)
        for item in answerlist:
            self.create(user = creator, answer = item)

        return

class Answers(models.Model):
    answer = models.CharField(max_length= 45)
    user = models.ForeignKey(User,related_name = "answers")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = AnswersManager()
