from django.urls import  path
from .views import (GlucoseLevelCreateView,GlucoseLevelListView,GlucoseLevelDetailView)


urlpatterns = [
    path('api/v1/levels/create/', GlucoseLevelCreateView.as_view(), name='glucose-level-create'),
    path('api/v1/levels/', GlucoseLevelListView.as_view(), name='glucose-level-list'),
    path('api/v1/levels/<int:pk>/', GlucoseLevelDetailView.as_view(), name='glucose-level-detail'),
]
