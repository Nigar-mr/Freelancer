# Generated by Django 2.2.3 on 2019-07-05 15:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('site_app', '0020_iconmodel_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='iconmodel',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='site_app.InfoModel'),
        ),
    ]