from django.urls import path
from django.contrib import admin

from . import views

app_name = 'store'

urlpatterns = [
    path('admin/', admin.site.urls),
    #Index.as_view()
    path('', views.product_all, name='home'),
    #path('', views.Index.as_view(), name='home'),
    path('product/<slug:slug>', views.product_detail, name='product_detail'),
    path('shop/<slug:category_slug>/', views.category_list, name='category_list'),
]
