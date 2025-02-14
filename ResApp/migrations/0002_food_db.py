# Generated by Django 5.1.2 on 2024-10-17 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ResApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food_Db',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Style', models.CharField(blank=True, max_length=100, null=True)),
                ('Food_Name', models.CharField(blank=True, max_length=100, null=True)),
                ('Food_Description', models.CharField(blank=True, max_length=100, null=True)),
                ('Quantity', models.IntegerField(blank=True, null=True)),
                ('MRP', models.IntegerField(blank=True, null=True)),
                ('Image1', models.ImageField(blank=True, null=True, upload_to='Foods')),
                ('Image2', models.ImageField(blank=True, null=True, upload_to='Foods')),
            ],
        ),
    ]
