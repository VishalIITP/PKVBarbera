# Generated by Django 3.2.3 on 2021-08-21 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0020_alter_barberaservices_servicecategory'),
    ]

    operations = [
        migrations.AlterField(
            model_name='barberaservices',
            name='serviceCategory',
            field=models.CharField(choices=[('men', 'Men'), ('women', 'Women'), ('wedding', 'Wedding'), ('kids', 'Kids')], default='men', max_length=50),
        ),
    ]