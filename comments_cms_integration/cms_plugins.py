from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from .models import CommentPluginModel
from django.utils.translation import ugettext as _


@plugin_pool.register_plugin  # register the plugin
class CommentPluginPublisher(CMSPluginBase):
    model = CommentPluginModel  # model where plugin data are saved
    module = _("django_comments")
    name = _("Comment Plugin")  # name of the plugin in the interface
    render_template = "comments/base.html"

    def render(self, context, instance, placeholder):
        context.update({'instance': instance})
        return context
