# Generated by Django 3.2.18 on 2023-04-09 10:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BookingModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('created_on', models.DateField()),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('message', models.TextField(blank=True, max_length=400)),
                ('status', models.IntegerField(choices=[(0, 'Pending'), (1, 'Approved')], default=0)),
                ('admin_approved', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='booking', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]