from django.urls import path
from .views import TaskListCreateView, UserRegistrationView, UserLoginView

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task list'),
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
]
