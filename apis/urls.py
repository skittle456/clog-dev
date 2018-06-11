from apis import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^blog_list',views.BlogList.as_view(),name='blog_list'),
    url(r'^provider_list',views.ProviderList.as_view(),name='provider_list'),
    url(r'^feedback_list',views.FeedbackList.as_view(),name='feedback_list'),
    url(r'^pin/(?P<blog_id>[\w]+)$', views.Pin.as_view()),
]
