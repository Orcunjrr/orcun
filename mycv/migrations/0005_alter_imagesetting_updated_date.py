# Generated by Django 5.0.3 on 2024-05-14 18:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mycv', '0004_alter_imagesetting_options_imagesetting_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagesetting',
            name='updated_date',
            field=models.DateTimeField(auto_now=True, verbose_name='Updated Date'),
        ),
    ]
