from django.contrib import admin
from django.urls import path
from myproject.core import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('admin/', admin.site.urls),
]
