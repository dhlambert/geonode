# -*- coding: utf-8 -*-


from django.db import migrations, models
import jsonfield.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('monitoring', '0007_monitoring_exception_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='MetricNotificationCheck',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('min_value', models.DecimalField(default=None, null=True, max_digits=16, decimal_places=4, blank=True)),
                ('max_value', models.DecimalField(default=None, null=True, max_digits=16, decimal_places=4, blank=True)),
                ('max_timeout', models.DurationField(help_text='Max timeout for given metric before error should be raised', null=True, blank=True)),
                ('active', models.BooleanField(default=True)),
                ('label', models.ForeignKey(blank=True, to='monitoring.MetricLabel', null=True)),
                ('metric', models.ForeignKey(related_name='checks', to='monitoring.Metric')),
            ],
        ),
        migrations.CreateModel(
            name='NotificationCheck',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('user_threshold', jsonfield.fields.JSONField(default={}, help_text='Threshold definition')),
            ],
        ),
        migrations.AddField(
            model_name='metricnotificationcheck',
            name='notification_check',
            field=models.ForeignKey(related_name='checks', to='monitoring.NotificationCheck'),
        ),
        migrations.AddField(
            model_name='metricnotificationcheck',
            name='ows_service',
            field=models.ForeignKey(blank=True, to='monitoring.OWSService', null=True),
        ),
        migrations.AddField(
            model_name='metricnotificationcheck',
            name='resource',
            field=models.ForeignKey(blank=True, to='monitoring.MonitoredResource', null=True),
        ),
        migrations.AddField(
            model_name='metricnotificationcheck',
            name='service',
            field=models.ForeignKey(related_name='checks', to='monitoring.Service'),
        ),
        migrations.AddField(
            model_name='metricnotificationcheck',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
