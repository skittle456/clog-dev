from apis import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^blog_list',views.BlogList.as_view(),name='blog_list'),
    url(r'^post',views.InsourceList.as_view(),name='post'),
    url(r'^patch/(?P<blog_id>[0-9]+)$',views.InsourcePatch.as_view(),name='patch'),
    url(r'^blog_detail/(?P<blog_id>[0-9]+)$', views.BlogDetail.as_view()),
    url(r'^add_view/(?P<blog_id>[0-9]+)$', views.add_view,name='add_view'),
    url(r'^provider_list',views.ProviderList.as_view(),name='provider_list'),
    url(r'^feedback_list',views.FeedbackList.as_view(),name='feedback_list'),
    url(r'^pin/(?P<blog_id>[0-9]+)$', views.Pin.as_view()),
    url(r'^follow/(?P<provider_id>[0-9]+)$', views.Follow.as_view()),
    url(r'^like/(?P<blog_id>[0-9]+)$', views.Like.as_view()),
    url(r'^register', views.Register.as_view(),name='register'),
    url(r'^login', views.Login.as_view(), name='login'),
    url(r'^logout',views.Logout.as_view(), name='logout'),
]
