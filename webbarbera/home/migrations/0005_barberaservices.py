# Generated by Django 3.2.3 on 2021-07-26 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_alter_reviewsmodel_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='barberaServices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serviceID', models.CharField(max_length=50)),
                ('serviceCategory', models.CharField(max_length=50)),
                ('serviceSubCategory', models.CharField(max_length=50)),
                ('serviceImage', models.ImageField(upload_to='../static/images')),
                ('servicePrice', models.CharField(max_length=50)),
                ('serviceDesc', models.CharField(max_length=300)),
                ('serviceUploadTime', models.DateTimeField()),
            ],
        ),
    ]
