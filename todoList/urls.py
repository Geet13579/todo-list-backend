from django.urls import include, path

from rest_framework import routers

from .views import GeeksViewSet, UserRegistrationView,LoginAPIView,UserProfileView,TodoListView,TodoDetailView

router = routers.DefaultRouter()
router.register(r'geeks', GeeksViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationView.as_view(), name='user-registration'),
     path('login/', LoginAPIView.as_view(), name='login'),
     path('profile/', UserProfileView.as_view(), name='profile'),
    path('todo_task/', TodoListView.as_view(), name='user-todo'),
    path('todo_task/<int:pk>/', TodoListView.as_view(), name='todo-detail'),
    path('todo_detail/<int:pk>/', TodoDetailView.as_view(), name='todo-detail'),
    path('api-auth/', include('rest_framework.urls')),
]
