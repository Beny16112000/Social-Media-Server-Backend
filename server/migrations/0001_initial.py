# Generated by Django 4.1.5 on 2023-01-04 00:17

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
            name='ProfileWork',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workplace', models.CharField(max_length=255)),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('detail', models.TextField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '2. Profile - Work',
            },
        ),
        migrations.CreateModel(
            name='ProfileStudy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('institution', models.CharField(max_length=255)),
                ('start', models.TimeField()),
                ('end', models.TimeField()),
                ('detail', models.TextField(blank=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '3. Profile - Academic',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('public', models.BooleanField(default=False)),
                ('gender', models.CharField(choices=[('men', 'men'), ('women', 'women'), ('none', 'none')], default='none', max_length=5)),
                ('birthday', models.DateField()),
                ('phone', models.IntegerField()),
                ('living', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': '1. Profile',
            },
        ),
    ]