# Generated by Django 2.2.18 on 2021-06-27 01:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('billboard', '0006_auto_20210627_0945'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subject',
            old_name='subject_in',
            new_name='subject_out',
        ),
        migrations.RemoveField(
            model_name='professor',
            name='subject_out',
        ),
        migrations.AddField(
            model_name='subject',
            name='professor_out',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='billboard.Professor'),
        ),
    ]
