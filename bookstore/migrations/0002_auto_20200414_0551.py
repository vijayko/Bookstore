# Generated by Django 3.0.5 on 2020-04-14 05:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='label',
            field=models.CharField(choices=[('G', 'good'), ('N', 'new'), ('A', 'acceptable')], max_length=1),
        ),
    ]