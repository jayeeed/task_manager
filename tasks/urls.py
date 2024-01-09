from django.urls import path, include
from rest_framework import routers
from .views import TaskListView, TaskDetailView, TaskCreateView, TaskUpdateView, TaskDeleteView, TaskViewSet, photo_to_task, delete_photo

router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)

urlpatterns = [
    path('', TaskListView.as_view(), name='list'),
    path('<int:pk>/', TaskDetailView.as_view(), name='details'),
    path('create/', TaskCreateView.as_view(), name='create'),
    path('<int:pk>/update/', TaskUpdateView.as_view(), name='update'),
    path('<int:pk>/delete/', TaskDeleteView.as_view(), name='delete'),
    path('<int:pk>/add_photo/', photo_to_task, name='add_photo'),
    path('delete_photo/<int:pk>/', delete_photo, name='delete_photo'),
    path('api/', include(router.urls)),
]
