from django.urls import  path
from .views import (UserListView,UserCreateView,UserDetailView)


urlpatterns = [
    path('api/v1/user/create/', UserCreateView.as_view(), name='user-create'),
    path('api/v1/user/', UserListView.as_view(), name='user-list'),
    path('api/v1/user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]
