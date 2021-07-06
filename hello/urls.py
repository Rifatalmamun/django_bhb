
from django.contrib import admin
from django.urls import path
from first_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.welcome,name='welcome'),
    path('index/',views.index,name='index'),
    path('home',views.home,name='home'),
]
