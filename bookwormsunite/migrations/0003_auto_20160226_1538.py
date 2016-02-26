# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookwormsunite', '0002_readathon_readers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='challenge',
            old_name='readathon_id',
            new_name='readathon',
        ),
    ]
