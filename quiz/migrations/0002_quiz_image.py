# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='image',
            field=models.CharField(default='cat.jpg', max_length=100),
            preserve_default=False,
        ),
    ]
