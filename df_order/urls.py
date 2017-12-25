from django.conf.urls import url
from df_order import views


urlpatterns = [
    url(r'^$', views.order, name='order'),
]