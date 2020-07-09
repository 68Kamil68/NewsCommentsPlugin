from cms.apphook_pool import apphook_pool
from cms.app_base import CMSApp


@apphook_pool.register
class BlogAppHook(CMSApp):
    app_name = "djangocms_blog"
    name = "Blog"

    def get_urls(self, page=None, language=None, **kwargs):
        return ["app_name.urls"]
