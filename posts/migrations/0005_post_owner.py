# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('posts', '0004_remove_post_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='owner',
            field=models.ForeignKey(related_name='posts', to=settings.AUTH_USER_MODEL, null=True),
        ),
    ]
