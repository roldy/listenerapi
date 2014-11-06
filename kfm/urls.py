from django.conf.urls import patterns, include, url
from filebrowser.sites import site
from rest_framework import routers
from radio import views
from django.conf import settings
from django.conf.urls.static import static


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'lineup', views.LineUpViewSet)
router.register(r'days', views.DaysViewSet)
router.register(r'events', views.EventViewSet)

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'kfm.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')), # rest_framework URLS
    # url(r'^lineup/', views.LineUpViewSet.as_view(), name='lineup-list'),
    url(r'^admin/filebrowser/', include(site.urls)), # filebrowser URLS
    url(r'^grappelli/', include('grappelli.urls')), # grappelli URLS
    url(r'^tinymce/', include('tinymce.urls')),     # tinymce URLS
    url(r'^admin/', include(admin.site.urls)),
) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
