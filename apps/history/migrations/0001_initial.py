# Generated by Django 3.1 on 2020-08-23 15:34

from django.db import migrations, models
import django.db.models.manager


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='History',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=10)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name_plural': 'Histories',
            },
            managers=[
                ('sorted_history', django.db.models.manager.Manager()),
            ],
        ),
    ]