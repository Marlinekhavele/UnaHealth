from django.urls import  path
from .views import (UserListView,UserCreateView,UserDetailView)


urlpatterns = [
    path('user/create/', UserCreateView.as_view(), name='user-create'),
    path('user/', UserListView.as_view(), name='user-list'),
    path('user/<int:pk>/', UserDetailView.as_view(), name='user-detail'),
]
