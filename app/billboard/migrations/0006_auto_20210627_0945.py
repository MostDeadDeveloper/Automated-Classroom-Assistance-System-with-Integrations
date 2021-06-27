# Generated by Django 2.2.18 on 2021-06-27 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billboard', '0005_auto_20210627_0825'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='professor',
            name='subject_out',
        ),
        migrations.AddField(
            model_name='professor',
            name='subject_out',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='billboard.Subject'),
        ),
    ]
