# Generated by Django 2.0.5 on 2018-05-08 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('leaning_logs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
