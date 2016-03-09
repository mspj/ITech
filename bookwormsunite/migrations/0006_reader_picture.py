# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookwormsunite', '0005_auto_20160302_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='reader',
            name='picture',
            field=models.ImageField(upload_to=b'profile_images', blank=True),
            preserve_default=True,
        ),
    ]
