# Generated by Django 3.2.3 on 2021-08-12 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0013_auto_20210812_0848'),
    ]

    operations = [
        migrations.RenameField(
            model_name='barberaservices',
            old_name='serviceCategoryDiscount',
            new_name='serviceCategory',
        ),
        migrations.AddField(
            model_name='barberaservices',
            name='serviceCategory1Discount',
            field=models.IntegerField(default='0', max_length=50),
        ),
    ]
