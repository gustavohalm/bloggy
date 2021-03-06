# Generated by Django 2.0.4 on 2019-04-20 23:42

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(max_length=15)),
            ],
        ),
        migrations.AlterField(
            model_name='comment',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 20, 23, 42, 58, 798391, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='post',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 20, 23, 42, 58, 797408, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='blog.Gender'),
        ),
    ]
