from django.urls import path
from . import views

urlpatterns = [
    path('', views.signup, name='signup-page'),
    path('loginn/', views.loginn, name='login-page'),
    path('home/', views.home, name='home'),
    path('newpost/', views.newPost, name='new-post'),
    path('mypost/', views.myPost, name='my-post'),
    path('post/<int:pk>/', views.post_detail, name='post-detail'),
    path('post/<int:pk>/edit/', views.edit_post, name='post-edit'),
    path('post/<int:pk>/delete/', views.delete_post, name='post-delete'),
    path('myprofile/', views.myProfile, name='my-profile'),
    path('update-profile/', views.update_profile, name='update-profile'),
    path('profile/delete/', views.delete_profile, name='delete-profile'),
    path('signout/', views.signout, name='signout-btn'), 
]
