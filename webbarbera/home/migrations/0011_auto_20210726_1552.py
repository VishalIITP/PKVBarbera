# Generated by Django 3.2.3 on 2021-07-26 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_alter_barberaservices_serviceid'),
    ]

    operations = [
        migrations.AddField(
            model_name='reviewsmodel',
            name='rating2',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='reviewsmodel',
            name='rating3',
            field=models.IntegerField(default=10),
        ),
        migrations.AlterField(
            model_name='reviewsmodel',
            name='rating',
            field=models.IntegerField(default=5),
        ),
    ]
