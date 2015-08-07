# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_quiz_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(related_name='questions', to='quiz.Quiz'),
        ),
    ]
