from django.db.models import Count
from django.db.models.functions import TruncDate
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Visit
from .serializers import VisitSerializer

###################################################################################################################################
class VisitCreateView(generics.CreateAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer

###################################################################################################################################
class VisitStatsView(APIView):
    def get(self, request):
        total = Visit.objects.count()
        by_country = Visit.objects.values('country').annotate(count=Count('id'))
        by_device = Visit.objects.values('device_type').annotate(count=Count('id'))
        by_day = Visit.objects.annotate(day=TruncDate('timestamp')).values('day').annotate(count=Count('id')).order_by('day')

        return Response({
            'total_visits': total,
            'visits_by_country': list(by_country),
            'visits_by_device': list(by_device),
            'visits_by_day': list(by_day),
        }, status=status.HTTP_200_OK)