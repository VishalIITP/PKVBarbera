# Generated by Django 3.2.3 on 2021-07-26 07:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_auto_20210726_0708'),
    ]

    operations = [
        migrations.RenameField(
            model_name='barberaservices',
            old_name='seviceName',
            new_name='serviceName',
        ),
        migrations.AlterField(
            model_name='barberaservices',
            name='serviceImage',
            field=models.ImageField(upload_to='home/images'),
        ),
    ]
