# Generated by Django 3.2.18 on 2023-04-11 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField(blank=True, max_length=400)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AlterField(
            model_name='bookingmodel',
            name='name',
            field=models.CharField(max_length=40),
        ),
    ]