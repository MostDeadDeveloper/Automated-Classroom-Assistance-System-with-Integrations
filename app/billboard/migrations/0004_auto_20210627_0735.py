# Generated by Django 2.2.18 on 2021-06-26 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('billboard', '0003_auto_20210627_0719'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_in', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email_in', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('professor_in', models.CharField(max_length=100)),
                ('published_date', models.DateField(blank=True, null=True)),
                ('contact_out', models.ManyToManyField(to='billboard.Contact')),
                ('email_out', models.ManyToManyField(to='billboard.Email')),
            ],
        ),
        migrations.CreateModel(
            name='Social',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('social_in', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_in', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Board',
        ),
        migrations.AddField(
            model_name='professor',
            name='social_out',
            field=models.ManyToManyField(to='billboard.Social'),
        ),
        migrations.AddField(
            model_name='professor',
            name='subject_out',
            field=models.ManyToManyField(to='billboard.Subject'),
        ),
    ]
