# Generated by Django 3.0.2 on 2020-02-26 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200221_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='photo',
            field=models.ImageField(default=None, null=True, upload_to='media'),
        ),
    ]
