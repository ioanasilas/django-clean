from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('form/', views.contact, name='form'),
    path('footer/', views.contact, name='footer'),
    path('header/', views.contact, name='header'),
    path('gallery/', views.gallery, name='gallery'),
    path('post/<int:post_id>/', views.post_detail, name='post_detail'),
    path('submit-review/', views.submit_review, name='submit_review')
]
