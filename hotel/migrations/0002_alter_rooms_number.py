# Generated by Django 4.1.1 on 2022-09-10 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='Number',
            field=models.CharField(max_length=3, null=True),
        ),
    ]