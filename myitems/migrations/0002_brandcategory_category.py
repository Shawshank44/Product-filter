# Generated by Django 3.2.5 on 2021-12-02 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myitems', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brandcategory',
            name='category',
            field=models.CharField(choices=[('M', 'MOBILE'), ('L', 'LAPTOP'), ('TW', 'Top wear'), ('BW', 'Bottom wear')], default='', max_length=2),
        ),
    ]
