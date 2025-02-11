"""clog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from apis import views
from django.views.generic.base import RedirectView
from django.conf.urls.static import static
from django.conf import settings
favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apis/',include('apis.urls')),
    url(r'^oauth/', include('social_django.urls', namespace='social')), 
    url(r'^favicon\.ico$', favicon_view),
    url(r'^$',views.index,name='index'),
    url(r'^category/(?P<category_title>[\w]+)$',views.list_by_category,name='list_by_category'),
    url(r'^category/(?P<category_title>[\w]+)/tag/(?P<tag_name>[\w]+)/$', views.list_by_category_tag, name='list_by_provider_category_tag'),
    url(r'^tag/(?P<tag_name>[\w]+)$',views.list_by_tag,name='list_by_tag'),
    url(r'^mypin',views.list_by_pin,name='list_by_pin'),
    url(r'^myfollow',views.list_by_follow,name='list_by_follow'),
    url(r'^blog/(?P<slug>.*)/$', views.get_insource_blog, name='get_insource_blog'),
    url(r'^provider/(?P<provider>[\w]+)/$', views.list_by_provider, name='list_by_provider'),
    url(r'^provider/(?P<provider>[\w]+)/tag/(?P<tag_name>[\w]+)/$', views.list_by_provider_tag, name='list_by_provider_tag'),
    url(r'^provider/(?P<provider>[\w]+)/category/(?P<category_title>[\w]+)/$', views.list_by_provider_category, name='list_by_provider_category'),
    url(r'^clog/(?P<blog_id>[0-9]+)/(?P<slug>.*)/$', views.get_insource_unique, name='get_insource_unique'),
    url(r'^editor',views.editor,name='editor'),
    url(r'^load_editor/(?P<blog_id>[0-9]+)$', views.load_editor, name='load_editor'),
    url(r'^provider_editor', views.provider_editor, name='provider_editor'),
    url(r'^terms/privacy',views.privacy_policy,name='privacy_policy'),
    url(r'^writer_registration',views.register_writer, name='register_writer'),
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)