from apis import views
from django.conf.urls import url

urlpatterns = [
    url(r'^signin',views.signin,name='signin'),
]
