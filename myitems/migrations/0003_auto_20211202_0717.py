# Generated by Django 3.2.5 on 2021-12-02 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myitems', '0002_brandcategory_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='brandcategory',
            name='url',
            field=models.SlugField(default=''),
        ),
        migrations.AddField(
            model_name='products',
            name='url',
            field=models.SlugField(default=''),
        ),
    ]