from django.urls import path

from blog import views


# app_name='course'

urlpatterns = [
    path('', views.blog_index, name='blog_index'),
    path('<blog_slug>', views.blog_detail, name='blog_detail'),

]