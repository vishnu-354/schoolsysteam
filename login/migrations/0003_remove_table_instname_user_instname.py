# Generated by Django 4.1.3 on 2023-02-26 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_table_user_orgname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='table',
            name='instname',
        ),
        migrations.AddField(
            model_name='user',
            name='instname',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]