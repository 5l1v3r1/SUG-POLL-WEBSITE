# Generated by Django 2.2.4 on 2019-08-09 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vote', '0002_auto_20190808_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='middle_name',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='votecategory',
            name='name',
            field=models.CharField(max_length=225),
        ),
    ]
