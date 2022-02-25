from django.contrib import admin
from django.urls import path
from Shortner import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('go',views.makeshorturl),
    path('<str:shorturl>',views.redirecturl)
]
