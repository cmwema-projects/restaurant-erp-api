# Generated by Django 4.2.5 on 2023-10-02 08:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_review_product_review'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='review',
        ),
        migrations.DeleteModel(
            name='Review',
        ),
    ]
