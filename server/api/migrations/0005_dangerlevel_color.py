# Generated by Django 3.0.7 on 2020-12-25 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='dangerlevel',
            name='color',
            field=models.CharField(blank=True, max_length=15),
        ),
    ]
