# Generated by Django 2.0.3 on 2019-07-03 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('solotodo', '0052_auto_20190628_1648'),
        ('wtb', '0008_auto_20171206_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='wtbbrand',
            name='brand',
            field=models.ForeignKey(default=848, on_delete=django.db.models.deletion.PROTECT, to='solotodo.Brand'),
            preserve_default=False,
        ),
    ]