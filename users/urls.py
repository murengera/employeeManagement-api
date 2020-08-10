from django.contrib import admin
from django.urls import path, include
from users.views import UserList, manager_register, login, email_confirmation, update_groups

urlpatterns = [
path('users/',UserList.as_view()),
path("manager_register/", manager_register,),
    path("login/", login, name="login"),
    path("activate/<slug:user_id>", email_confirmation),
    path('update-groups/', update_groups),

]
