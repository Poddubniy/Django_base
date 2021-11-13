# Generated by Django 3.2.9 on 2021-11-13 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productcategory',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='productcategory',
            name='name',
            field=models.CharField(max_length=128, unique=True),
        ),
    ]
