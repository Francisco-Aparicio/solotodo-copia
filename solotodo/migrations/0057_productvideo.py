# Generated by Django 2.0.3 on 2019-07-22 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solotodo', '0056_auto_20190712_2019'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductVideo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('youtube_id', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=256)),
                ('conditions', models.CharField(max_length=256)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]