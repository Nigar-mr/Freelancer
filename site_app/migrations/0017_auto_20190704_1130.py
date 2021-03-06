# Generated by Django 2.2.3 on 2019-07-04 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0016_remove_contactformmodel_contact_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactformmodel',
            name='text',
        ),
        migrations.AddField(
            model_name='contactformmodel',
            name='name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='contactformmodel',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='contactmodel',
            name='button',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='contactmodel',
            name='name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
