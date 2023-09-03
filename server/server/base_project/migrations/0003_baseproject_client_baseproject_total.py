# Generated by Django 4.2.4 on 2023-09-01 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0001_initial'),
        ('base_project', '0002_remove_baseproject_client_remove_baseproject_docs_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseproject',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='client.client'),
        ),
        migrations.AddField(
            model_name='baseproject',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True),
        ),
    ]
