from . import views
from django.urls import path


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('tasks/', views.user_tasks, name='tasks'),
    path('completed_tasks/', views.CompletedTaskView.as_view(), name='completed_tasks'),
    path('create_task/', views.CreateTaskView.as_view(), name='create_task'),
    path('update_task/<slug:pk>/', views.UpdateTaskView.as_view(), name='update_task'),
    path('delete_task/<slug:pk>/', views.DeleteTaskView.as_view(), name='delete_task'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='user_logout'),
]