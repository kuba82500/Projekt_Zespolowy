# Generated by Django 2.1.3 on 2019-01-12 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SRP', '0002_auto_20190112_1640'),
        ('accounts', '0004_auto_20190112_1542'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Firma',
        ),
        migrations.AddField(
            model_name='user',
            name='firma',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='nazwafirmy',
            field=models.CharField(blank=True, max_length=255, null=True, unique=True),
        ),
    ]
