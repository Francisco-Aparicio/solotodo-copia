# Generated by Django 2.0 on 2018-02-12 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solotodo', '0017_country_flag'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='budget_ordering',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]