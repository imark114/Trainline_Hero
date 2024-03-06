from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.SignUpView, name='signup'),
    path('login/', views.UserLoginView.as_view(), name='login'),
    path('active/<uid64>/<token>/', views.activate, name='activae'),
    path('logout/', views.UserLogoutView.as_view(), name='logout'),
    path('update_profile/<int:id>/', views.ProfileView.as_view(), name='profile'),
    path('change_password', views.PassChangeView.as_view(), name='pass_change'),
]
