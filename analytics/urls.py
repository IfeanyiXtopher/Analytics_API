from django.urls import path
from .views import VisitCreateView, VisitStatsView

urlpatterns = [
    path('visits/', VisitCreateView.as_view(), name='visit-create'),
    path('visits/stats/', VisitStatsView.as_view(), name='visit-stats'),
]

