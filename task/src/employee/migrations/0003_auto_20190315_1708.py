# Generated by Django 2.1.7 on 2019-03-15 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_auto_20190315_1702'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
