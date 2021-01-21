from django.urls import path, include
from . import views

urlpatterns = [
    path('',views.index, name='index'),
    path('search/<slug:keyword>/', views.sentence, name='sentence'),
    path('post/', views.sentence, name='sentence_post'),
    path('update/', views.update, name='update'),
    path('like/<int:sentence_id>/', views.like, name='like'),
    path('unlike/<int:sentence_id>/', views.unlike, name='unlike'),
    ]
