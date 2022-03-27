from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('UserInsertForm', views.UserInsertForm.as_view(), name='insert'),
    path('UpdateUserInfo/<int:pk>', views.UpdateUserInfo.as_view(), name='update-userinfo'),
    path('DeleteUserInfo/<int:pk>', views.DeleteUserInfo.as_view(), name='delete-userinfo'),
]
