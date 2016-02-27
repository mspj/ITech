# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):
    dependencies = [
        ('bookwormsunite', '0003_auto_20160226_1538'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='icon',
            field=models.CharField(default=b'star', max_length=20),
            preserve_default=True,
        ),
    ]
