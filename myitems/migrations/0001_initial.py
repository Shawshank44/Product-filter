# Generated by Django 3.2.5 on 2021-12-02 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BrandCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('image', models.ImageField(upload_to='img')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('desc', models.TextField()),
                ('image', models.ImageField(upload_to='productimg')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myitems.brandcategory')),
            ],
        ),
    ]