# Generated by Django 4.0.4 on 2022-06-05 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ELEV8APP', '0009_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ELEV8APP.topic'),
        ),
    ]
