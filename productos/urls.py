from django.urls import path
from django.conf.urls import url, include
from django.views.decorators.csrf import csrf_exempt

from . import views

urlpatterns = [
    url(r'^$', views.index,name='index'),
    url(r'base_layout',views.base_layout,name='base_layout'),
    url(r'getdata',views.getdata,name='getdata'),

    url(r'^productos/', views.ProductoList,name='productoList'),
    url(r'^productocreate/$', csrf_exempt(views.ProductoCreate), name='productoCreate'),
    url(r'^productoupdate/(?P<pk>\d+)/$', csrf_exempt(views.ProductoUpdate), name='productoUpdate'),
    url(r'^ventas/', views.VentaList, name='ventaList'),
    url(r'^ventacreate/$', csrf_exempt(views.VentaCreate), name='ventaCreate'),
    path('', include('django.contrib.auth.urls')),
    path('', include('social_django.urls')),
]
