from django.db import models

from cms.models import CMSPlugin
from django_comments.models import Comment

class CommentPluginModel(CMSPlugin):
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE)
