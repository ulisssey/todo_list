from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', RegisterPage.as_view(), name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),

    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='tasksdetail'),
    path('create-task/', TaskCreate.as_view(), name='taskcreate'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name='tasksupdate'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name='tasksdelete'),
]