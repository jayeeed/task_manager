from django.contrib import admin
from django.urls import path, include
from tasks.views import TaskListView

urlpatterns = [
    path('', TaskListView.as_view(), name='home'),
    path('admin/', admin.site.urls),
    path('tasks/', include('tasks.urls')),
]
