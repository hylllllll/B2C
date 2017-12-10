from django.conf.urls import url
from df_user import views
urlpatterns = [
    url(r'^register/$', views.register, name='register'),
]