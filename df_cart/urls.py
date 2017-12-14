from django.conf.urls import url
from df_cart import views


urlpatterns = [
    url(r'^$', views.cart, name='cart'),
    url(r'^add(\d+)_(\d+)', views.add, name='add'),
]