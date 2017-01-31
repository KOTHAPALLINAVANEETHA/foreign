# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('image', models.ImageField(default=b'images/None/No-img.jpg', upload_to=b'images/')),
                ('published', models.DateTimeField(null=True, blank=True)),
                ('name', models.CharField(max_length=200)),
                ('subscribe', models.EmailField(max_length=254)),
                ('draft', models.BooleanField(default=False)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('highlighted', models.TextField()),
                ('comments', models.CharField(max_length=100)),
                ('owner', models.ForeignKey(related_name='posts', to=settings.AUTH_USER_MODEL)),
                ('subscibers', models.ManyToManyField(related_name='subscribers', to=settings.AUTH_USER_MODEL, blank=True)),
            ],
            options={
                'ordering': ['published', 'updated_date'],
            },
        ),
    ]
