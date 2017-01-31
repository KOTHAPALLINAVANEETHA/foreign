# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20170131_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='owner',
            field=models.ForeignKey(related_name='posts', to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
