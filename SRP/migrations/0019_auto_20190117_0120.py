# Generated by Django 2.1.3 on 2019-01-17 00:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SRP', '0018_auto_20190116_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupa',
            name='id_Praktyki',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='SRP.Praktyki'),
        ),
    ]
