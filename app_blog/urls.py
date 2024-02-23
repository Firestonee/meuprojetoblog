from django.urls import path
from app_blog import views
urlpatterns = [
    path('',views.index, name='home'),
    path('login/', views.user_login,name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('post_admin/', views.post_admin, name='post_admin'),
    path('<slug:slug>/edit/', views.edit_admin, name='edit_admin'),
    path('<slug:slug>/delete/', views.delete_post, name='delete_post'),
]
