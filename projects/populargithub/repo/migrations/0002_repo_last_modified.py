# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('repo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='repo',
            name='Last_Modified',
            field=models.DateTimeField(default=None, null=True),
            preserve_default=True,
        ),
    ]
