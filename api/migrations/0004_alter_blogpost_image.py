# Generated by Django 4.2.2 on 2023-06-13 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_rename_categorie_blogpost_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='image',
            field=models.ImageField(upload_to='blogs/'),
        ),
    ]
