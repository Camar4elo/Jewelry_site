# Generated by Django 3.2.6 on 2021-08-17 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0014_alter_decorations_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decorations',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='', verbose_name='Изображение'),
        ),
    ]
