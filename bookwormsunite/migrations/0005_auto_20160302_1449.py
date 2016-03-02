# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookwormsunite', '0004_activity_icon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reader',
            name='img',
            field=models.URLField(blank=True),
            preserve_default=True,
        ),
    ]
