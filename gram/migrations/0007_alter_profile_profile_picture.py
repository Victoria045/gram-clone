# Generated by Django 3.2.9 on 2021-12-04 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gram', '0006_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='default.png', upload_to='images/'),
        ),
    ]
