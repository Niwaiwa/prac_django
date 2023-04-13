from django.contrib import admin
from django.urls import path

from core.views import index, contract

urlpatterns = [
    path('', index, name='index'),
    path('contract/', contract, name='contract'),
    path('admin/', admin.site.urls),
]
