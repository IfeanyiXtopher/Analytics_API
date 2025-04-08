from django.db import models

###################################################################################################################################
class Visit(models.Model):
    DEVICE_CHOICES = [
        ('mobile', 'Mobile'),
        ('desktop', 'Desktop'),
    ]

    ip_address = models.GenericIPAddressField()
    page_url = models.URLField()
    country = models.CharField(max_length=100)
    device_type = models.CharField(max_length=10, choices=DEVICE_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.ip_address} visited {self.page_url}"

