from django.urls import  path
from .views import (GlucoseLevelCreateView,GlucoseLevelListView,GlucoseLevelDetailView)


urlpatterns = [
    path('levels/create/', GlucoseLevelCreateView.as_view(), name='glucose-level-create'),
    path('levels/', GlucoseLevelListView.as_view(), name='glucose-level-list'),
    path('levels/<int:pk>/', GlucoseLevelDetailView.as_view(), name='glucose-level-detail'),
]
