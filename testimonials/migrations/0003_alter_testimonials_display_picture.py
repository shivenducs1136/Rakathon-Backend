# Generated by Django 3.2.14 on 2022-07-20 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('testimonials', '0002_remove_testimonials_designation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimonials',
            name='display_picture',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
