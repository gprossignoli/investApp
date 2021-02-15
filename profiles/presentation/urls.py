from django.urls import path

from profiles.presentation import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='user_login'),
    path('logout/', views.user_logout, name='user_logout'),
    path('user/', views.user_profile, name='user_profile'),
    path("user/delete/<int:pk>/", views.DeleteUserProfile.as_view(), name="delete_user_profile"),
    path("user/update/<int:pk>/", views.UpdateUserProfile.as_view(), name="update_user_profile")
]
