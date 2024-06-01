from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_resize_image, name='upload_resize_image'),
]