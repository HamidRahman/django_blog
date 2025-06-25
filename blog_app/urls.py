from django.urls import path
from . import views

app_name = 'blog_app'

urlpatterns = [
    #post views
    path('', views.post_list, name='post_list'),
    path('post/<int:id>/', views.post_detail, name='post_detail')
]