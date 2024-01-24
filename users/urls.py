from django.urls import path
from . import views

urlpatterns = [
    path("/logout", views.logout_view, name="logout"),
    path("/signup", views.sign_up, name="signup"),
    path("/email_sent", views.email_sent_page, name="email_sent"),
    
    # User Management
    
    path("/", views.management, name='user_management'),
    path("/new_user", views.new_user_page, name='new_user'),
    path("/update_user/<int:id>", views.update_user_page, name='update_user'),
]
