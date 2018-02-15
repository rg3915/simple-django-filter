from django.contrib import admin
from django.urls import path
from myproject.core import views


urlpatterns = [
    path('search/', views.search, name='search'),
    path('search/cbv/', views.search_cbv, name='search_cbv'),
    path('admin/', admin.site.urls),
]
