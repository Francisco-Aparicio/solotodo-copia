# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-11-23 15:26
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wtb', '0006_wtbbrand_website'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='wtbbrand',
            options={'ordering': ('name',), 'permissions': [('view_wtb_brand', 'Can view the WTB brand'), ('is_wtb_brand_staff', 'Is staff of this WTB brand'), ('backend_view_wtb', 'Display the WTB menu in the backend')]},
        ),
    ]