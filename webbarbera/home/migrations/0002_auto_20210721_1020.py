# Generated by Django 3.2.3 on 2021-07-21 10:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='toDoModel',
            new_name='reviewsModel',
        ),
        migrations.DeleteModel(
            name='registeredUsers',
        ),
    ]
