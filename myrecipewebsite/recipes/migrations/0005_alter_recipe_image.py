# Generated by Django 5.0.6 on 2024-06-26 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_alter_recipe_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.ImageField(default='recipes/default_image.jpg', upload_to='recipes/'),
        ),
    ]
