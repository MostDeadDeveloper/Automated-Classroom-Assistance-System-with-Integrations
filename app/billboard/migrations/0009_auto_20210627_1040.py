# Generated by Django 2.2.18 on 2021-06-27 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billboard', '0008_auto_20210627_1003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='subject_in',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
