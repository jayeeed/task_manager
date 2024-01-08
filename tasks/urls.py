from django.urls import path
from .views import UserTasksView, TaskListCreateView, UserRegistrationView, UserLoginView

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task list'),
    path('tasks/<int:user_id>/', UserTasksView.as_view(), name='task-detail'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
]
