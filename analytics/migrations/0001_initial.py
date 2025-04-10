# Generated by Django 4.2.20 on 2025-04-08 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip_address', models.GenericIPAddressField()),
                ('page_url', models.URLField()),
                ('country', models.CharField(max_length=100)),
                ('device_type', models.CharField(choices=[('mobile', 'Mobile'), ('desktop', 'Desktop')], max_length=10)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
