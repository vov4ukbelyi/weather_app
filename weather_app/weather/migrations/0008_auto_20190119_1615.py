# Generated by Django 2.1.5 on 2019-01-19 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('weather', '0007_auto_20190119_1531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
    ]
