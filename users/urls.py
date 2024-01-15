from django.urls import path
from . import views

urlpatterns = [
    path("logout/", views.logout_view, name="logout"),
    path("signup/", views.sign_up, name="signup"),
    path("email_sent/", views.email_sent_page, name="email_sent"),
    
    # User Management
    
    path("", views.management, name='user_management')
]
