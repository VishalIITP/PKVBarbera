# Generated by Django 3.2.3 on 2021-07-21 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_user_reviewsmodel_userrater'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewsmodel',
            name='rating',
            field=models.IntegerField(default=100),
        ),
    ]
