# Generated by Django 2.1.3 on 2019-01-12 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_user_student'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nrindeks',
            field=models.CharField(blank=True, max_length=6, null=True, unique=True),
        ),
    ]
