# Generated by Django 2.2 on 2020-04-08 08:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog_detail',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 8, 8, 55, 52, 549669, tzinfo=utc)),
        ),
    ]