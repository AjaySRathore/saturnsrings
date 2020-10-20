# Generated by Django 3.1.2 on 2020-10-20 20:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Ringer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.CharField(blank=True, max_length=500, verbose_name='Bio')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PastJob',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('position', models.CharField(max_length=100, verbose_name='Position')),
                ('company', models.CharField(max_length=100, verbose_name='Company')),
                ('description', models.CharField(blank=True, max_length=500, verbose_name='Descripiton')),
                ('ringer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ringer.ringer', verbose_name='Ringer')),
            ],
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Title')),
                ('description', models.CharField(blank=True, max_length=200, verbose_name='Descripiton')),
                ('ringer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ringer.ringer', verbose_name='Ringer')),
            ],
        ),
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('authority', models.CharField(max_length=150, verbose_name='Issuing Authority')),
                ('description', models.CharField(blank=True, max_length=250, verbose_name='Descripiton')),
                ('ringer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ringer.ringer', verbose_name='Ringer')),
            ],
        ),
    ]
