# Generated by Django 3.2.4 on 2021-07-01 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('professor_data', models.CharField(max_length=100)),
                ('subject_data', models.TextField(blank=True, max_length=300)),
                ('contact_data', models.TextField(blank=True, max_length=300)),
                ('email_data', models.TextField(blank=True, max_length=300)),
                ('social_data', models.TextField(blank=True, max_length=300)),
                ('up_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]