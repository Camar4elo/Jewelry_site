# Generated by Django 3.2.6 on 2021-08-17 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_alter_decorations_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='decorations',
            name='description',
            field=models.CharField(blank=True, help_text='Описание', max_length=1500, null=True),
        ),
    ]