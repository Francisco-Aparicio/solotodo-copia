# Generated by Django 2.0.3 on 2019-07-12 19:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solotodo', '0054_auto_20190708_2038'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='uuid',
            field=models.CharField(blank=True, max_length=256, null=True),
        ),
    ]