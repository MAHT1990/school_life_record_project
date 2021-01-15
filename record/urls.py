from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('<slug:keyword>/', views.sentence, name='sentence'),
    path('post/', views.sentence, name='sentence_post')
    ]
