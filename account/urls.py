from django.urls import path
from .views import CustomLoginView, RegisterView, ForgetPasswordView, ResetPasswordView, activate
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('confirmation/<str:uidb64>/<str:token>/', activate, name='confirmation'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('forget_password/', ForgetPasswordView.as_view(), name='forget_password'),
    path('reset_password/<str:uidb64>/<str:token>/',
        ResetPasswordView.as_view(), name="reset_password"),
]
