from django.urls import path
from . import views 
app_name='confession'

urlpatterns = [
    path('make/', views.post_create, name='creation'),
    path('', views.post_list, name='listing'),
    path('<p_id>/', views.post_detail, name='detail'),
    path('<p_id>/like/', views.post_like, name='like'),
    path('<p_id>/dislike/', views.post_dislike, name='dislike'),
    path('<p_id>/comment/', views.post_comment, name='comment'),


]