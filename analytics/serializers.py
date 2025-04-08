from rest_framework import serializers
from .models import Visit

###################################################################################################################################
class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        fields = ['id', 'ip_address', 'page_url', 'country', 'device_type', 'timestamp']
        read_only_fields = ['id', 'timestamp']

