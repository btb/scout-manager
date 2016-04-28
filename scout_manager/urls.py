from django.conf.urls import include, url
from scout_manager.views.api import Spot
# from django.contrib import admin
# admin.autodiscover()

from scout_manager.views import pages

urlpatterns = [
    # Examples:

    # /manager/
    url(r'^$', pages.home, name='home'),

    # /items/
    url(r'^items/$', pages.items, name='items'),
    url(r'^items/(?P<item_id>[0-9]{1,5})', pages.items_edit,
        name='items_edit'),
    url(r'^items/add/', pages.items_add, name='items_add'),

    # /spaces/
    url(r'^spaces/$', pages.spaces, name='spaces'),
    url(r'^spaces/(?P<spot_id>[0-9]{1,5})', pages.spaces_edit,
        name='spaces_edit'),
    url(r'^spaces/add/', pages.spaces_add, name='spaces_add'),
    url(r'^schedule/(?P<spot_id>[0-9]{1,5})', pages.schedule,
        name='schedule'),
    url(r'api/spot/(?P<spot_id>[0-9]{1,5})', Spot().run)

]
