# Generated by Django 4.0.4 on 2022-06-15 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('queries', '0009_alter_userqueryinfo_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserQueryInfo',
        ),
    ]