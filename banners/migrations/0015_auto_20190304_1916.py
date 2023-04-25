# Generated by Django 2.0.3 on 2019-03-04 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('banners', '0014_banner_destination_urls'),
    ]

    operations = [
        migrations.AddField(
            model_name='bannerupdate',
            name='message',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='bannerupdate',
            name='status',
            field=models.IntegerField(choices=[(1, 'In process'), (2, 'Success'), (3, 'Error')], default=1),
        ),
    ]