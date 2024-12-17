from django.urls import path
from . import views
urlpatterns =[
  path('profile/', views.admin_profile_view, name='profile'),
  path('user_profile/', views.user_profile_view, name='user_profile'),
  path('settings/', views.settings_view, name='settings'),
  path('',views.login_view,name="login_page"),
  path('login/',views.login_F,name="login"),
  path('logout/',views.logout_view,name="logout"),
  path('all_users/',views.all_users_view,name="all_users"),
  path('edit_user/<int:user_id>/',views.edit_user_view,name="edit_user"),
  path('user/<int:user_id>/delete/', views.delete_user, name='delete_user'),
  path('signup/',views.signup_view,name="signup"),
]