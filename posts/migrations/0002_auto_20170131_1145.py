# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default=b'Images/None/No-img.jpg', upload_to=b'images/'),
        ),
        migrations.AlterField(
            model_name='post',
            name='owner',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
        ),
    ]
