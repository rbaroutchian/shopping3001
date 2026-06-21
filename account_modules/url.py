from django.urls import path
from .import views


urlpatterns = [
    path('register/',views.RegistrationView.as_view(),name='register_page'),
    path('active-account/<email_active_code>/', views.ActiveAccountView.as_view(), name='active_page'),
    path('login/', views.LoginView.as_view(), name='login_page'),
    path('forgot/', views.ForgotPasswordView.as_view(),name='forgot_page'),
     path('verify-code/', views.VerifyCodeView.as_view(),name='verify_code_page'),
     path('reset-password/', views.ResetPasswordView.as_view(),name='reset_password_page'),
     path('logout/', views.LogoutView.as_view(),name='logout_page'),
]