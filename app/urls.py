from django.urls import  path
from .views import (GlucoseRecordCreateView,GlucoseRecordListView,GlucoseRecordDetailView)


urlpatterns = [
    path('levels/create/', GlucoseRecordCreateView.as_view(), name='glucose-record-create'),
    path('levels/', GlucoseRecordListView.as_view(), name='glucose-record-list'),
    path('levels/<int:pk>/', GlucoseRecordDetailView.as_view(), name='glucose-record-detail'),
]
