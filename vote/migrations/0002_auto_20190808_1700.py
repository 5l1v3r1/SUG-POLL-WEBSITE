# Generated by Django 2.2.4 on 2019-08-08 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='matric_number',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='votecategory',
            name='name',
            field=models.CharField(max_length=225, unique=True),
        ),
    ]
