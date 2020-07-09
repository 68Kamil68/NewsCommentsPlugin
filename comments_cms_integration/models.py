from django.db import models

from cms.models import CMSPlugin
from django_comments_xtd.models import XtdComment


class CommentPluginModel(CMSPlugin):
    comment = models.ForeignKey(XtdComment, on_delete=models.CASCADE)
