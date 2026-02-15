from django.contrib import admin
from django.urls import path
from firstapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
        path('', views.home, name='home'),
            path('add', views.add, name='add'),
            # In urlpatterns list
            path('form/', views.my_form_view, name='my_form'),
            
            ]

