# Generated by Django 5.1.2 on 2024-11-20 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0003_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
