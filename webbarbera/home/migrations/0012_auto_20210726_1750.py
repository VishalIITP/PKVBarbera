# Generated by Django 3.2.3 on 2021-07-26 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_auto_20210726_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewsmodel',
            name='rating',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='reviewsmodel',
            name='rating2',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='reviewsmodel',
            name='rating3',
            field=models.IntegerField(),
        ),
    ]
